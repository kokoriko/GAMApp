"""@GAMApp
The dispatcher for whole CLI.
"""
import subprocess,sys, cmd, getpass, signal
from ga_bases.GASearchBase import GASearch
from ga_bases.GAAuthenticationBase import GAAuthentication
from ga_bases.GAValidatorBase import GAValidator
from ga_bases.GAExceptionBase import URLValidationError, EmailValidationError, AuthenticationError
from GABase import GABase


class GACLIClient(cmd.Cmd):
	"""Holds all routing rules for dispather and Python Cmd.
	"""
	def __init__(self):
		"""Constructor for GACLIClient.
		Contructs the CLI and what's necessary for the rest of the app. 
		For ex: holds authentication object to further use it in everywhere.
		"""
		cmd.Cmd.__init__(self)
		self.prompt = "GAMApp>"
		self.authentication = GAAuthentication()

	def my_preloop(self):
		"""This is called before the cmd initialized.
		"""
		print "GAMApp CLI Initializing..."
		print "GAMApp CLI Initialized"

	def postloop(self):
		"""When exiting from the CLI, this function will be executed.
		"""
		print "Bye bye"

	def do_authenticate(self, e):
		"""Promtps user for domain_name, username, and password in order to create
		an authentication object to be used in neccessary places.
		"""
		domain_name = raw_input("Domain Name: ")
		username = raw_input("Username: ") # Username or Email - Will be controlled in next step
		password = getpass.getpass("Password: ")

		try:
			is_domain_name_valid = GAValidator(what=domain_name, based_on="URL").validate() # If the URL is actually a valid one
			is_username_valid_email = GAValidator(what=username, based_on="EMAIL").validate() # Checking if the user entered his/her email, or only username
		except URLValidationError, ex:
			#TODO - Log the details
			print "Domain Name not validated"
		except EmailValidationError, ex:
			#TODO - Log the Details
			pass
			
		self.authentication.domain_name = domain_name
		self.authentication.password = password
		if not is_username_valid_email: # If username is a valid email, use it as it is.
			self.authentication.username = username
		else: # if not, concatenate it with @ and the domain_name
			self.authentication.username = "%(username)s@%(domainname)s" % {'username': username,
																			'domainname': domain_name}
		
		try:
			# Trying to authenticate with GoogleApps
			self.authentication.authenticate_groups_service()
			print "Login Succeded"
		except AuthenticationError, ex:
			print str(ex)
			return
		
		
	def do_find(self, usr):
		"""
		If prompted without any parameter, retrieves all groups. (FOR NOW)
		"""
		#TODO - Find users or groups
		ga_search = GASearch(auth=self.authentication, usr=usr)
		ga_search.search()
		return ga_search.show_results()
	
	def do_addusertogroups(self, usr, grp=None):
		"""
		Add usr to grp. If no grp provided, it'll add the usr to all the groups
		"""
		pass
	
	def do_deleteuserfromgroup(self, usr, grp=None):
		"""
		Deletes usr from grp. If no grp is provided, it'll search for usr in all groups, and delete from all of them. 
		"""
		pass
	
	def do_addgroup(self, grpName):
		"""
		Adds a group with grpName
		"""
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
	cli.cmdloop() # Initialize the CLI
		
