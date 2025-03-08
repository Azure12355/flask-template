from flask import Flask
from ..common.result_utils import ResultUtils
from .error_code import ErrorCode
from .business_exception import BusinessException
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_exception_handler(app: Flask):
    """
    初始化全局异常处理器
    :author: Lytton Yang
    :from: https://www.weilanx.com
    """
    @app.errorhandler(BusinessException)
    def handle_business_exception(e):
        logger.error(f"BusinessException: {e.message}", exc_info=True)
        return ResultUtils.error(e.code, e.message)

    @app.errorhandler(Exception)
    def handle_runtime_exception(e):
        logger.error("RuntimeException", exc_info=True)
        return ResultUtils.error(ErrorCode.SYSTEM_ERROR.code, ErrorCode.SYSTEM_ERROR.message)