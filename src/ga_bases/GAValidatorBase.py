from GABase import GABase
from GAExceptionBase import URLValidationError, EmailValidationError
import re

class GAValidator(GABase):
	def __init__(self, what, based_on):
		super(GABase, self).__init__()
		self.what = what
		self.based_on = based_on
		if self.based_on == "URL":
			self.regex = "./*" # TODO  - URL Validation Regex
		elif self.based_on == "EMAIL":
			self.regex = "./*" #TODO - EMAIL Validation Regex
	
	def validate(self):
		is_valid = re.match(self.regex, self.what)
		if is_valid:
			return True
		else:
			if self.based_on == "URL":
				raise URLValidationException(what, how)
			elif self.based_on == "EMAIL":
				raise EmailValidationExcetion(what, how)
		
