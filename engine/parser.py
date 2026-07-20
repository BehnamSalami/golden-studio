import ast


class FunctionParser:

    def __init__(self, code: str):
        self.code = code

    def get_functions(self):
        tree = ast.parse(self.code)

        functions = []

        for node in tree.body:

            if isinstance(node, ast.FunctionDef):

                args = []

                for arg in node.args.args:
                    args.append(arg.arg)

                functions.append({
                    "name": node.name,
                    "args": args
                })

        return functions