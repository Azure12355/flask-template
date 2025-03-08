class BaseResponse:
    def __init__(self, code, data=None, message=''):
        self.code = code
        self.data = data
        self.message = message

    def to_dict(self):
        return {
            'code': self.code,
            'data': self.data,
            'message': self.message
        }