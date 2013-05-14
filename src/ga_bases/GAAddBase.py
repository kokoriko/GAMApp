from GABase import GABase

class GAAdd(GABase):
        def __init__(self,auth=None,usr=None,grps=None):
                super(GABase,self).__init__()
                self.authentication=auth
                self.user=usr
                self.groups=grps
        def Add(self):
                gservice=self.authentication.gservice
                add_user_to_groups(gservice,self.user,self.groups)
