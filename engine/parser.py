import ast


class PythonParser:
    """
    تحلیل کننده کد پایتون
    """

    def parse(self, code: str):

        tree = ast.parse(code)

        for node in tree.body:

            if isinstance(node, ast.FunctionDef):

                return self._parse_function(node)

        raise Exception("هیچ تابعی در کد پیدا نشد.")

    def _parse_function(self, node):

        parameters = []

        for arg in node.args.args:

            parameter = {

                "name": arg.arg,

                "type": self._get_type(arg.annotation)

            }

            parameters.append(parameter)

        return {

            "name": node.name,

            "parameters": parameters

        }

    def _get_type(self, annotation):

        if annotation is None:
            return "str"

        if isinstance(annotation, ast.Name):
            return annotation.id

        return "str"