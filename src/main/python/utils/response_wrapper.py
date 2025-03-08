from flask import jsonify


class R:
    @staticmethod
    def success(data=None, message="success"):
        return jsonify({
            "code": 200,
            "message": message,
            "data": data
        })

    @staticmethod
    def fail(code=400, message="fail"):
        return jsonify({
            "code": code,
            "message": message,
            "data": None
        }), code