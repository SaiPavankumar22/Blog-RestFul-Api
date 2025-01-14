from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_login import UserMixin
from utils.auth import generate_token, verify_token, login_required, admin_required
from datetime import datetime


class UserModel(UserMixin):
    def __init__(self, db):
        self.collection = db.users

    def register_routes(self, app):
        @app.route("/register", methods=["POST"])
        def register_user():
            data = request.json
            if not data.get("username") or not data.get("password"):
                return jsonify({"error": "Username and password are required"}), 400
            if self.collection.find_one({"username": data["username"]}):
                return jsonify({"error": "Username already exists"}), 400

            hashed_password = generate_password_hash(data["password"])
            user = {
                "username": data["username"],
                "email": data.get("email"),
                "password": hashed_password,
                "role": "viewer",
                "bio": "",
                "profile_pic": "",
                "followers": [],
                "following": [],
                "created_at": datetime.utcnow(),
            }
            self.collection.insert_one(user)
            return jsonify({"message": "User registered successfully"}), 201

        @app.route("/login", methods=["POST"])
        def login_user():
            data = request.json
            user = self.collection.find_one({"username": data["username"]})
            if not user or not check_password_hash(user["password"], data["password"]):
                return jsonify({"error": "Invalid credentials"}), 401
            token = generate_token(str(user["_id"]), user["role"])
            return jsonify({"token": token}), 200

        @app.route("/profile", methods=["GET", "PUT"])
        @login_required
        def profile(user_id):
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            if not user:
                return jsonify({"error": "User not found"}), 404

            if request.method == "GET":
                user["_id"] = str(user["_id"])
                del user["password"]
                return jsonify(user), 200

            data = request.json
            self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
            return jsonify({"message": "Profile updated successfully"}), 200

        @app.route("/users/<string:user_id>/follow", methods=["POST"])
        @login_required
        def follow(user_id, follow_id):
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            follow_user = self.collection.find_one({"_id": ObjectId(follow_id)})

            if not user or not follow_user:
                return jsonify({"error": "User not found"}), 404

            if follow_id in user["following"]:
                return jsonify({"message": "Already following"}), 400

            self.collection.update_one(
                {"_id": ObjectId(user_id)}, {"$addToSet": {"following": follow_id}}
            )
            self.collection.update_one(
                {"_id": ObjectId(follow_id)}, {"$addToSet": {"followers": user_id}}
            )

            return jsonify({"message": "Followed successfully"}), 200

        @app.route("/users/<string:user_id>/unfollow", methods=["POST"])
        @login_required
        def unfollow(user_id, unfollow_id):
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            unfollow_user = self.collection.find_one({"_id": ObjectId(unfollow_id)})

            if not user or not unfollow_user:
                return jsonify({"error": "User not found"}), 404

            if unfollow_id not in user["following"]:
                return jsonify({"message": "Not following this user"}), 400

            self.collection.update_one(
                {"_id": ObjectId(user_id)}, {"$pull": {"following": unfollow_id}}
            )
            self.collection.update_one(
                {"_id": ObjectId(unfollow_id)}, {"$pull": {"followers": user_id}}
            )

            return jsonify({"message": "Unfollowed successfully"}), 200
