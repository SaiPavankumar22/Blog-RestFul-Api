# Blog Restful API

A Flask-based RESTful API for a blogging platform with user management, post creation, comment handling, and more. It integrates MongoDB for database operations and follows modular design for scalability and maintainability.

## Features

- **User Management**: Register, login, profile management, and user follow/unfollow.
- **Post Management**: CRUD operations, like/unlike posts, and search functionality.
- **Commenting**: Add comments to posts with nested replies support.
- **Categories**: Organize posts into categories.
- **Analytics**: Admin-only insights like total posts and average views.

## Project Structure

```
restful-blog-api/
├── app.py                  # Main entry point of the application
├── models/                 # Contains data models
│   ├── __init__.py
│   ├── categories.py       # Categories-related logic
│   ├── comments.py         # Comments-related logic
│   ├── posts.py            # Posts-related logic
│   ├── users.py            # Users-related logic
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── auth.py             # Authentication and role-based access control
│   ├── validation.py       # Validation utilities
│   ├── file_upload.py      # File upload handling
├── static/
│   └── uploads/            # Uploaded files
│       ├── posts/          # Post images
│       ├── profiles/       # User profile images
├── requirements.txt        # Python dependencies
├── config.py               # Application configuration
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SaiPavankumar22/Blog-RestFul-Api.git
   cd Blog-RestFul-Api
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB**:
   - Set up a MongoDB instance locally or in the cloud.
   - Update the connection string in `app.py`:
     ```python
     app.config["MONGO_URI"] = "mongodb://localhost:27017/blog_app"
     ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the API**:
   - Navigate to `http://127.0.0.1:5000` in your browser or use an API testing tool like Postman.

## API Endpoints

### Users
- `POST /register` - Register a new user.
- `POST /login` - Log in a user.
- `GET/PUT /profile` - View or update user profile.
- `POST /users/<user_id>/follow` - Follow a user.
- `POST /users/<user_id>/unfollow` - Unfollow a user.

### Posts
- `POST /posts` - Create a new post.
- `GET /posts` - Get all posts.
- `GET /posts/<post_id>` - Retrieve a specific post.
- `PUT/DELETE /posts/<post_id>` - Update or delete a post.
- `POST /posts/<post_id>/like` - Like/unlike a post.
- `GET /posts/search?q=<query>` - Search posts by title.

### Comments
- `POST /posts/<post_id>/comments` - Add a comment to a post.
- `GET /posts/<post_id>/comments` - View comments on a post.

### Categories
- Endpoints for category management can be added to organize posts.

### Analytics (Admin Only)
- `GET /analytics` - Get insights about posts.

## Authentication & Authorization

- **JWT Authentication**: Tokens are generated during login and validated for protected routes.
- **Role-Based Access Control**:
  - `viewer`: Can perform general operations.
  - `admin`: Access to analytics and advanced features.

## Deployment

To deploy this API:
1. Use a production WSGI server like Gunicorn.
2. Set up a reverse proxy (e.g., Nginx) for better performance.
3. Use a cloud database for MongoDB (e.g., MongoDB Atlas).

## Contribution

Feel free to submit pull requests or report issues to improve the project!

## License

This project is licensed under the MIT License.
