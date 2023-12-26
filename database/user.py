from .entities import User
from pony.orm import db_session, commit, delete, select

# Function to create (insert) a new user
@db_session
def create_user(name, phone=None, company="pony_test"):
    user = User(name=name, phone=phone, company=company)
    commit()
    return user

# Function to read (select) a user by ID
@db_session
def read_user_by_id(user_id):
    return User.get(id=user_id)

# Function to read (select) users by a certain condition
@db_session
def read_all_users():
    return User.select()[:]
    
# Function to update a user's information
@db_session
def update_user(user_id, new_phone):
    user = User.get(id=user_id)
    if user:
        user.phone = new_phone
        commit()
        return user
    return None

# Function to delete a user by ID
@db_session
def delete_user(user_id):
    user = User.get(id=user_id)
    if user:
        user.delete()
        commit()
        return True
    return False
