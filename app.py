from flask import Flask, jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_login import LoginManager
from models.users import UserModel
from models.posts import PostModel
from models.comments import CommentModel
from models.categories import CategoryModel
from utils.file_upload import setup_file_uploads

app = Flask(__name__)

# Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/blog_app"
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["SECRET_KEY"] = "your_secret_key"

# MongoDB
mongo = PyMongo(app)

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize models
user_model = UserModel(mongo.db)
post_model = PostModel(mongo.db)
comment_model = CommentModel(mongo.db)
category_model = CategoryModel(mongo.db)

# Setup file uploads
setup_file_uploads(app)

# Register routes
user_model.register_routes(app)
post_model.register_routes(app)
comment_model.register_routes(app)
category_model.register_routes(app)

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return UserModel(user["_id"], user["username"])
    return None

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Blog API!"})

if __name__ == "__main__":
    app.run(debug=True)
