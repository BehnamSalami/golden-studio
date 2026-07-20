class PythonRunner:
    """
    اجرای تابع پایتون
    """

    def execute(self, code, function_name, values):

        namespace = {}

        exec(code, namespace)

        if function_name not in namespace:
            raise Exception("تابع پیدا نشد.")

        function = namespace[function_name]

        return function(**values)