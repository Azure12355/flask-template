from flask import Blueprint

from ..common.result_utils import ResultUtils
from ..exception.error_code import ErrorCode
from ..exception.thorw_utils import ThrowUtils

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.route('/', methods=['GET'])
def get_users():
    return ResultUtils.success(data=["小米手机", "小米汽车", "小米家电"])


@product_bp.route('/exception/params', methods=['GET'])
def test_params1():
    return ResultUtils.error(ErrorCode.PARAMS_ERROR.code, ErrorCode.PARAMS_ERROR.message)

@product_bp.route('/exception/if', methods=['GET'])
def test_params2():
    return ThrowUtils.throw_if_error((2 > 1), ErrorCode.OPERATION_ERROR)

@product_bp.route('/exception/global', methods=['GET'])
def test_params3():
    a = 1 / 0