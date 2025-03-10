from flask import Blueprint, jsonify
from ..service.user_service import UserService
from ..common.result_utils import ResultUtils

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = UserService().get_all_users()
    return ResultUtils.success(users)