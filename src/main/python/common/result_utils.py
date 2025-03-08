from flask import jsonify

from .base_response import BaseResponse

class ResultUtils:
    @staticmethod
    def success(data=None):
        return jsonify(BaseResponse(0, data, 'ok').to_dict()), 200

    @staticmethod
    def error(code, message):
        return jsonify(BaseResponse(code, None, message).to_dict()), 200