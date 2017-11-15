

class ValidatorService:

    def validate(self, data):

        if 'author' not in data:
            return False
        elif 'title' not in data:
            return False
        else:
            return True
