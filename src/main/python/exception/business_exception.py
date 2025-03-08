from .error_code import ErrorCode

class BusinessException(Exception):
    """
    自定义业务异常类，模仿 Java 的 BusinessException
    :author: Lytton Yang
    :from: https://www.weilanx.com
    """
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

    @classmethod
    def from_error_code(cls, error_code: ErrorCode, message: str = None):
        """从 ErrorCode 创建异常实例"""
        return cls(error_code.code, message or error_code.message)