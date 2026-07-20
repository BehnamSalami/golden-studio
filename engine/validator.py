class Validator:

    @staticmethod
    def convert(value, value_type):

        if value_type == "integer":

            return int(value)

        if value_type == "float":

            return float(value)

        if value_type == "boolean":

            return value.lower() == "true"

        return value