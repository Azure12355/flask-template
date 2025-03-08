from enum import Enum

class ErrorCode(Enum):
    """
    错误码枚举类
    :author: Lytton Yang
    :from: https://www.weilanx.com
    """
    SUCCESS = (0, "ok")
    PARAMS_ERROR = (400, "请求参数错误")
    NOT_LOGIN_ERROR = (401, "未登录")
    NO_AUTH_ERROR = (402, "无权限")
    NOT_FOUND_ERROR = (404, "请求数据不存在")
    FORBIDDEN_ERROR = (403, "禁止访问")
    SYSTEM_ERROR = (500, "系统内部异常")
    OPERATION_ERROR = (501, "操作失败")

    def __init__(self, code: int, message: str):
        self._value_ = code
        self.message = message

    @property
    def code(self) -> int:
        return self.value

    @property
    def msg(self) -> str:
        return self.message

# 示例使用

if __name__ == "__main__":
    print(ErrorCode.SUCCESS.code)  # 输出 0
    print(ErrorCode.SUCCESS.msg)   # 输出 ok
    print(ErrorCode.NOT_FOUND_ERROR.code)  # 输出 404
    print(ErrorCode.NOT_FOUND_ERROR.msg)   # 输出 请求数据不存在
