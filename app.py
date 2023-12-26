from database import db
from database.user import *

if __name__ == "__main__":
    db.generate_mapping(create_tables=True)

    # user = create_user("balakrishnan")
    # print(user)

    # user = update_user(1, 12345)
    # print(user)

    # users = read_all_users()
    # for user in users:
    #     print(user.id, user.name, user.phone, user.company)

    # user = read_user_by_id(1)
    # print(user)

    # user = delete_user(1)
    # print(user)