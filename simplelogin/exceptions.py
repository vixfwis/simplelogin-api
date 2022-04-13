
class BaseError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.msg}>'

    def __repr__(self):
        return self.__str__()

class APIError(BaseError):
    pass

class ClientError(BaseError):
    pass
