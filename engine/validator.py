class InputValidator:
    """
    اعتبارسنجی و تبدیل ورودی‌های تابع
    """

    def validate(self, function, values):
        """
        function.parameters : لیست پارامترهای تابع
        values : دیکشنری مقادیر وارد شده توسط کاربر
        """

        validated = {}

        for parameter in function.parameters:

            name = parameter.name
            value_type = parameter.type

            value = values.get(name)

            validated[name] = self._convert(
                value,
                value_type
            )

        return validated

    def _convert(self, value, value_type):

        if value_type == "int":
            return int(value)

        if value_type == "float":
            return float(value)

        if value_type == "bool":

            if str(value).lower() in (
                "true",
                "1",
                "yes",
                "on"
            ):
                return True

            return False

        return str(value)