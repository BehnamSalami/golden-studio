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

                    function["parameters"].append(

                        {

                            "name": arg.arg,

                            "type": "text"

                        }

                    )

                functions.append(function)

        return functions