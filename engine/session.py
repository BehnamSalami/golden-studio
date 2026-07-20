class Session:
    """
    نگهداری اطلاعات پروژه جاری
    """

    def __init__(self):

        self.project = None
        self.code = ""
        self.function = None
        self.form = None
        self.inputs = {}
        self.result = None

    def clear(self):

        self.project = None
        self.code = ""
        self.function = None
        self.form = None
        self.inputs = {}
        self.result = None