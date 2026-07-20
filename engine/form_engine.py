from engine.parser import FunctionParser


class FormEngine:

    def __init__(self, source_code):

        self.source_code = source_code

        self.parser = FunctionParser(source_code)

    def build(self):

        functions = self.parser.get_functions()

        if len(functions) == 0:

            return None

        function = functions[0]

        form = {

            "title": function["name"],

            "fields": []

        }

        for parameter in function["parameters"]:

            form["fields"].append({

                "label": parameter["name"],

                "type": parameter["type"],

                "value": ""

            })

        return form