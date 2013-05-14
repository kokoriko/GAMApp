"""@GAAuhtentication
For authentication with GData
"""
from GABase import GABase

class GAAuthentication(GABase):
    """
    Authentication object.
    Takes care of where to be logined (groups or other services).
    """
    def __init__(self, domain_name=None, username=None, password=None):
        super(GABase, self).__init__()
        self.domain_name = domain_name
        self.username = username
        self.password = password
    
    def authenticate_groups_service(self):
        """
        For authenticating with GoogleApps Groups
        """
        self.params = {"username": self.username,
                       "password": self.password,
                       "domain_name": self.domain_name}
        # All the magic goes here
        self.gservice = self.ga_authenticate_groups_service(self.params)
    
    def authenticate_blah_service(self):
        """
        BLABLA
        """
        self.params = {"username": self.username,
                       "password": self.password,
                       "domain_name": self.domain_name}
        self.gservice = self.ga_authenticate_blah_service(self.params)
    

