from GABase import GABase
from ga_bases.GAValidatorBase import GAValidator

class GAUserMan(GABase):

        def __init__(self,auth=None):
                super(GABase,self).__init__()
                self.authentication=auth

	def add(self,usr,grps=None):
		try:
			is_username_valid_email=GAValidator(what=usr,based_on="EMAIL").validate();
		except EmailValidationError ,ex:
			print str(ex)
		gservice=self.authentication.gservice
		if grps:
			for grp in grps:
				self.adding_result=self.add_user_to_group(gservice,usr,grp)
				print self.adding_result
                else:
			self.all_groups=self.get_all_groups(gservice)
			for grp in self.all_groups:
				self.adding_result=self.add_user_to_group(gservice,usr,grp)
				print self.adding_result
                
