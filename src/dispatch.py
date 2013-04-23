import cmd, getpass, signal, sys
from ga_bases.GASearchBase import GASearch
from ga_bases.GAAuthenticationBase import GAAuthentication
from ga_bases.GAValidatorBase import GAValidator
from ga_bases.GAExceptionBase import URLValidationError, EmailValidationError, AuthenticationError
from GABase import GABase

class GACLIClient(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "GAMApp>"
		self.authentication = GAAuthentication()

	def my_preloop(self):
		print "GAMApp CLI Initializing..."
		print "GAMApp CLI Initialized"

	def postloop(self):
		print "Bye bye"

	def do_authenticate(self, e):
		domain_name = raw_input("Domain Name: ")
		username = raw_input("Username: ")
		password = getpass.getpass("Password: ")

		try:
			is_domain_name_valid = GAValidator(what=domain_name, based_on="URL").validate()
			is_username_valid_email = GAValidator(what=username, based_on="EMAIL").validate()
		except URLValidationError, ex:
			#TODO - Log the details
			print "Domain Name not validated"
		except EmailValidationError, ex:
			#TODO - Log the Details
			pass
			
		self.authentication.domain_name = domain_name
		self.authentication.password = password
		if not is_username_valid_email:
			self.authentication.username = username
		else:
			self.authentication.username = "%(username)s@%(domainname)s" % {'username': username,
																			'domainname': domain_name}
		
		try:
			self.authentication.authenticate_groups_service()
			print "Login Succeded"
		except AuthenticationError, ex:
			print str(ex)
			return
		
		
	def do_find(self, usr):
		ga_search = GASearch(auth=self.authentication, usr=usr)
		ga_search.search()
		return ga_search.show_results()
	
	def do_addusertogroups(self, usr, grp=None):
		pass
	
	def do_deleteuserfromgroup(self, usr, grp=None):
		pass
	
	def do_addgroup(self, grpName):
		pass
	
	def do_emptyline(self, e):
		pass

	def cmdloop(self):
		try:
			
			cmd.Cmd.cmdloop(self)
		except KeyboardInterrupt as e:
			print ""
			self.cmdloop()


if __name__ == "__main__":
	cli = GACLIClient()
	cli.my_preloop()
	cli.cmdloop()
		
