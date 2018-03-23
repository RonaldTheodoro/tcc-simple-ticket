class BaseConverter:
    regex = r''

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return f'{value}'


class UidConverter(BaseConverter):
    regex = r'[0-9A-Za-z_\-]+'
 

class TokenConverter(BaseConverter):
    regex = r'[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}'
