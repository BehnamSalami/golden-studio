import ast


class FunctionParser:

    def __init__(self, source_code: str):

        self.source_code = source_code

        self.tree = ast.parse(source_code)

    def get_functions(self):

        functions = []

        for node in self.tree.body:

            if isinstance(node, ast.FunctionDef):

                function = {

                    "name": node.name,

                    "parameters": [],

                    "docstring": ast.get_docstring(node),

                    "line": node.lineno

                }

                for arg in node.args.args:

    parameter_type = "text"

    if arg.annotation:

        if isinstance(arg.annotation, ast.Name):

            annotation = arg.annotation.id

            if annotation == "int":
                parameter_type = "integer"

            elif annotation == "float":
                parameter_type = "float"

            elif annotation == "str":
                parameter_type = "text"

            elif annotation == "bool":
                parameter_type = "boolean"

    function["parameters"].append(
        {
            "name": arg.arg,
            "type": parameter_type
        }
    )

                functions.append(function)

        return functions