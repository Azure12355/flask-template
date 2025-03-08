from ..dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def get_all_users(self):
        users = self.dao.get_all()
        return [user.to_dict() for user in users]