class FormEngine:
    """
    تبدیل خروجی Parser به فرم قابل نمایش
    """

    def build(self, function):

        form = {
            "title": function["name"],
            "fields": []
        }

        for parameter in function["parameters"]:

            field = {
                "label": parameter["name"],
                "type": parameter["type"],
                "required": True,
                "value": ""
            }

            form["fields"].append(field)

        return form