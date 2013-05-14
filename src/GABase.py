"""@package GABase
Base package for everything. This is a bridge between GAMApp and GData.
"""
import gdata.apps.groups.service as gdataserv
from gdata.service import BadAuthentication
from ga_bases import *
from ga_bases.GAExceptionBase import AuthenticationError

class GABase(object):
    """
    Base class for everything. This is a bridge between GAMApp and GData.
    """
    def __init__(self, **kwargs):
        """
        Constructor for GABase. **kwargs is used for dynamic variable handling. 
        There can be variable count variables depending on, where does it 
        initialized. So instead of putting every possibility in definition, 
        declaration-time variable definition is preferred.
        """
        self.username = kwargs.get("username") # Username for authentication
        self.password = kwargs.get("password") # Password for authentication
        self.domain_name = kwargs.get("domain_name") # Domain Name for auth
        self.group = kwargs.get("group") # For GASearchBase.search_group()
        self.user = kwargs.get("user")   # For GASearchBase.search.user()
        # Holds all groups, that is came from get_all_groups()-more like a cache
        self.all_groups = kwargs.get("all_groups")         
        #TODO 
        pass
    
    def ga_authenticate_groups_service(self, params):
        """
        Authentication handler for groups service
        """
        self.username = params['username']
        self.password = params['password']
        self.domain_name = params['domain_name']
        # Create a loginnable object that is used for authentication in future
        self.gservice = gdataserv.GroupsService(email=self.username, 
                                                domain=self.domain_name, 
                                                password=self.password)
        try:
            # Try to login   
            self.gservice.ProgrammaticLogin()
        except BadAuthentication:
            raise AuthenticationError("Login",
                                      "Login Failed - Incorrect username or password")
        
        return self.gservice

    def get_group(self, gservice):
        """
        Rerieves the group
        """
        return gservice.RetrieveGroup(self.group.group_id)

    def get_all_groups(self, gservice):
        """
        Retrieves all groups in a domain. 
        An already authenticated object (gservice) is used.
        """
        # This does the magic for retrieving all groups. And it holds the groups
        # as the object member to be used in future  - as a temporary cache 
        self.all_groups = gservice.RetrieveAllGroups()      
        return self.all_groups

    def get_member_from_group(self, gservice, member, group):
        """
        Retrieve member from group
        """
        return gservice.RetrieveMember(member, group)
        
    def check_is_member(self, gservice, member, group, groups_user_in=None):
        """
        Check to see if the member is already in the group
        """
        is_member = False
        if gservice.IsMember(member, group):
            is_member = True

        if groups_user_in is None:
            if is_member:   
                groups_user_in.append(group)
            else:
                return is_member

