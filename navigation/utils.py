class UpperCaseConverter:
    regex = "[a-zA-Z0-9]+"

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value
