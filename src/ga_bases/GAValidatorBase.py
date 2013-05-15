from GABase import GABase
from GAExceptionBase import URLValidationError, EmailValidationError
import re

class GAValidator(GABase):
        def __init__(self, what, based_on):
                super(GABase, self).__init__()
                self.what = what
                self.based_on = based_on
                if self.based_on == "URL":
                        self.regex = "^([a-zA-Z0-9-_]+(?<!-|\.)\.)+[a-z]{2,6}$"
                elif self.based_on == "EMAIL":
                        self.regex = "^([a-zA-Z0-9-]+((?<!-|\.)\.)?)+(?<!-|\.)@([a-zA-Z0-9-_]+(?<!-|\.)\.)+[a-z]{2,6}$"
        
        def validate(self):
                is_valid = re.match(self.regex, self.what)
                if is_valid:
                        return True
                else:
                        if self.based_on == "URL":
                                raise URLValidationError(self.what, self.based_on)
                        elif self.based_on == "EMAIL":
                                raise EmailValidationError(self.what, self.based_on)

