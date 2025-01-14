# Blog Restful API

A Flask-based RESTful API for a blogging platform with user management, post creation, comment handling, and more. It integrates MongoDB for database operations and follows modular design for scalability and maintainability.

### **Core Features and Functionalities**
1. **User Authentication**  
   - Users should be able to register, login, and logout securely.
   - Role-based access control (admin, author, viewer).
   - Password reset functionality.
2. **User Profile Management**  
   - Allow users to manage their profiles, including updating bio and profile pictures.
3. **Blog Post Management**  
   - Users should be able to create, read, update, and delete (CRUD) blog posts.
   - Post views counter for analytics.
4. **Comment Management**  
   - Users should be able to create, read, update, and delete (CRUD) comments on blog posts.
   - Support for nested comments (threaded replies).
5. **Post Categorization**  
   - Blog posts should be categorizable.
   - Support for tagging posts with keywords.
6. **Search Functionality**  
   - Users should be able to search for blog posts by title, content, category, or tags.
   - Advanced search filters (e.g., by date, author).
8. **Social Features**  
   - Like/unlike blog posts and comments.
   - Follow/unfollow authors.
   - Display a feed of posts from followed authors.
10. **Post Analytics**  
    - Track views, likes, and shares per post.
11. **File Uploads**  
    - Support for uploading images to posts.
12. **Admin Dashboard**  
    - Manage users, posts, comments, categories, and tags.
    - Access site-wide analytics (e.g., total users, posts, comments).

---
### **API Endpoints**
#### **Blog Post Endpoints**
1. GET /posts: Retrieve a list of all blog posts.  
2. GET /posts/{id}: Retrieve a single blog post by ID.  
3. POST /posts: Create a new blog post.  
4. PUT /posts/{id}: Update an existing blog post.  
5. DELETE /posts/{id}: Delete a blog post.  
6. GET /posts/popular: Retrieve top-trending posts.  
7. GET /posts/recent: Retrieve the most recent posts.  
8. GET /posts/{id}/likes: Retrieve the number of likes on a post.  
9. POST /posts/{id}/like: Like a blog post.  
10. DELETE /posts/{id}/like: Unlike a blog post.  
11. GET /posts/drafts: Retrieve all unpublished posts (authors only).
---
#### **Comment Endpoints**
1. GET /comments: Retrieve a list of all comments. 
3. POST /comments: Create a new comment on a blog post.  
4. PUT /comments/{id}: Update an existing comment.  
5. DELETE /comments/{id}: Delete a comment. 
8. GET /comments/{id}/replies: Retrieve all replies to a comment.
10. DELETE /comments/{id}/reject: Reject a comment (admin and authors only).
---
#### **Category Endpoints**
1. GET /categories: Retrieve a list of all categories.  
2. GET /categories/{id}: Retrieve a single category by ID.  
3. POST /categories: Create a new category(only admin).  
4. PUT /categories/{id}: Update an existing category(only admin).  
5. DELETE /categories/{id}: Delete a category(only admin).  
6. GET /categories/{id}/posts: Retrieve all posts in a category.
---
#### **Tag Endpoints**
1. GET /tags: Retrieve a list of all tags.  
2. GET /tags/{id}: Retrieve a single tag by ID.  
3. POST /tags: Create a new tag.  
4. PUT /tags/{id}: Update an existing tag.  
5. DELETE /tags/{id}: Delete a tag.  
6. GET /tags/{id}/posts: Retrieve all posts with a specific tag.
---
#### **Search Endpoint**
1. GET /search: Retrieve a list of blog posts matching the search query.  
   - Filters: ?title=, ?content=, ?tags=, ?category=, ?author=.
---
#### **Authentication Endpoints**
1. POST /register: Register a new user(with unique user name).  
2. POST /login: Login an existing user.  
3. POST /logout: Logout the current user.  
4. GET /profile: Retrieve the current user's profile.  
5. PUT /profile: Update the current user's profile.  
6. POST /password-reset: Request a password reset link.  
7. POST /password-reset/confirm: Confirm password reset with token.
---
#### **User Following Endpoints**
1. GET /users/{id}/followers: Retrieve all followers of a user.  
2. GET /users/{id}/following: Retrieve all users followed by a user.  
3. POST /users/{id}/follow: Follow a user.  
4. DELETE /users/{id}/unfollow: Unfollow a user.
---
#### **Admin Endpoints**
1. GET /admin/users: Retrieve all users (admin only).  
2. PUT /admin/users/{id}/role: Update a user's role (admin only).  
3. DELETE /admin/users/{id}: Delete a user (admin only).  
4. GET /admin/analytics: Retrieve site-wide analytics (admin only).  
---

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
