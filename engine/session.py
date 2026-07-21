class Session:
    """
    نگهداری وضعیت فعلی موتور
    """

    def __init__(self):

        self.current_project = None

        self.code = ""

        self.function = None

        self.result = None

    def reset(self):

        self.current_project = None

        self.code = ""

        self.function = None

        self.result = None