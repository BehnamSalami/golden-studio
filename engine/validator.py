class Validator:
    """
    بررسی و تبدیل مقادیر ورودی
    """

    def validate(self, value, value_type):

        if value_type == "int":
            return int(value)

        if value_type == "float":
            return float(value)

        if value_type == "bool":
            if str(value).lower() in ["true", "1", "yes"]:
                return True
            return False

        return str(value)