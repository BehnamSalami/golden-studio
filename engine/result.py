from datetime import datetime


class Result:

    def __init__(self, success, result, error):

        self.success = success

        self.result = result

        self.error = error

        self.created_at = datetime.now()

    def to_dict(self):

        return {

            "success": self.success,

            "result": self.result,

            "error": self.error,

            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")

        }