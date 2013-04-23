from GABase import GABase


class GASearch(GABase):
	def __init__(self, auth=None, usr=None):
		super(GABase, self).__init__()
		self.authentication = auth
		self.user = usr
	
	def search(self):
		gservice = self.authentication.gservice
		self.all_groups = self.get_all_groups(gservice)
		print self.all_groups
	
	def show_results(self):
		pass

