
class URLValidationError(Exception):
	def __init__(self, what, how):
		self.expr = what # TODO
		self.msg = "%s is not valid based on %s" % (what, how)
	
	def __str__(self):
		return repr(self.msg)

class EmailValidationError(Exception):
	def __init__(self, what, how):
		self.expr = what #TODO 
		self.msg = "%s is not valid based on %s" % (what, how)
	
	def __str__(self):
		return repr(self.msg)
	
class AuthenticationError(Exception):
	def __init__(self, expr, msg):
		self.expr = expr
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)

class UserNotFoundError(Exception):
	def __init__(self, expr, msg):
		self.expr = expr
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)

class MultipleKeyError(Exception):
	def __init__(self, expr, msg):
		self.expr = expr
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)
