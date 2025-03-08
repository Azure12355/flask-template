from .base_dao import BaseDAO
from ..model.entity.user import User

class UserDAO(BaseDAO):
    def __init__(self):
        super().__init__(User)