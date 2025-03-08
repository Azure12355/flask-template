from .business_exception import BusinessException
from .error_code import ErrorCode

class ThrowUtils:
    """
    异常抛出工具类，模仿 Java 的 ThrowUtils
    :author: Lytton Yang
    :from: https://www.weilanx.com
    """
    @staticmethod
    def throw_if(condition: bool, exception: Exception):
        """如果条件为真，则抛出指定异常"""
        if condition:
            raise exception

    @staticmethod
    def throw_if_error(condition: bool, error_code: ErrorCode):
        """如果条件为真，则抛出基于 ErrorCode 的异常"""
        ThrowUtils.throw_if(condition, BusinessException.from_error_code(error_code))

    @staticmethod
    def throw_if_error_message(condition: bool, error_code: ErrorCode, message: str):
        """如果条件为真，则抛出基于 ErrorCode 和自定义消息的异常"""
        ThrowUtils.throw_if(condition, BusinessException.from_error_code(error_code, message))