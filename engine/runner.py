import traceback


class PythonRunner:

    def __init__(self):

        self.namespace = {}

    def load(self, source_code):

        self.namespace = {}

        exec(source_code, self.namespace)

    def execute(self, function_name, arguments):

        try:

            function = self.namespace.get(function_name)

            if function is None:

                return {

                    "success": False,

                    "result": None,

                    "error": "Function not found"

                }

            result = function(**arguments)

            return {

                "success": True,

                "result": result,

                "error": None

            }

        except Exception:

            return {

                "success": False,

                "result": None,

                "error": traceback.format_exc()

            }