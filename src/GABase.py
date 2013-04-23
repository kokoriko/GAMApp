import gdata.apps.groups.service as gdataserv
from gdata.service import BadAuthentication
from ga_bases import *
from ga_bases.GAExceptionBase import *

class GABase(object):
	def __init__(self, *args, **kwargs):
		self.username = kwargs.get("username")
		self.password = kwargs.get("password")
		self.domain_name = kwargs.get("domain_name")
		self.all_groups = kwargs.get("all_groups")
		#TODO 
		pass
	
	def ga_authenticate_groups_service(self, params):
		self.username = params['username']
		self.password = params['password']
		self.domain_name = params['domain_name']
		self.gservice = gdataserv.GroupsService(email=self.username, 
														   domain=self.domain_name, 
														   password=self.password)
		try:
			self.gservice.ProgrammaticLogin()
		except BadAuthentication, ex:
			raise AuthenticationError("Login","Login Failed - Incorrect username or password")
		
		return self.gservice

	def get_all_groups(self, gservice):
		self.all_groups = gservice.RetrieveAllGroups()
		return self.all_groups
		
