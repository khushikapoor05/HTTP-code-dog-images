from app import app, db, User

with app.app_context():
    users = User.query.all()
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")
