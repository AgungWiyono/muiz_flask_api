class JsonReturn:
    @staticmethod
    def success(data, statusCode=200):
        assert(type(data) is dict)
        return {
            'status': 'success',
            'data': data
        }, statusCode

    @staticmethod
    def fail(msg, statusCode=400):
        return {
            'status': 'fail',
            'data': msg
        }, statusCode

    @staticmethod
    def error(message, statusCode=500):
        return {
            'status': 'error',
            'message': message
        }, statusCode