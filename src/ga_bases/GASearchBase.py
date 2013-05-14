from GABase import GABase
from threading import Thread
from ga_bases.GAExceptionBase import UserNotFoundError, MultipleKeyError
groups_user_in = []

class GASearchThreadPool(Thread):
    """
    A Thread pool for searching all groups
    """
    def __init__(self, gservice=None, user=None, groups=None, check_is_member_func=None):
        Thread.__init__(self)
        self.gservice = gservice
        self.user = user
        self.groups = groups
        self.check_is_member_func = check_is_member_func

    def run(self):
        for group in self.groups:
            find_thread = Thread(target=self.check_is_member_func,
                                 args=(self.gservice,# Service module, used as bridge
                                       self.user, # user we are looking for
                                       group['groupId'], # group we are looking in
                                       groups_user_in, # list of all groups which user is in.
                                       )
                                )
            find_thread.start()


class GASearch(GABase):
    def __init__(self, auth=None, user=None, group=None):
        super(GABase, self).__init__()
        self.authentication = auth
        self.user = user
        self.group = group

    def search(self):
        if self.user is None and self.group is None:
            self.all_groups = self.get_all_groups(gservice)
        elif self.user is None:
            return self.search_group() 
        elif self.group is None:
            return self.search_user()
        else:
            raise MultipleKeyError("Multiple Key Passed",
                                   "Cannot pass both user and group arguments to `find`")
  
    def search_user(self):
        gservice = self.authentication.gservice
        self.all_groups = self.get_all_groups(gservice)
        groups_user_in = []
        thread_pool = GASearchThreadPool(gservice,
                                         self.user,
                                         self.all_groups,
                                         self.check_is_member,
                                         )
        thread_pool.start()
        thread_pool.join()

        if not groups_user_in:
            raise UserNotFoundError("User Not Found",
                                    "User is not in any of the groups")

        print "User %(usr)s is in these groups:" % {'usr':self.user}
        for item in groups_user_in:
            print item

    def search_group(self):
        gservice = self.authentication.gservice
        if self.group is None:
            self.all_groups = self.get_all_groups(gservice)
            return self.all_groups
        else:
            return self.get_group(gservice)
    
    def show_results(self):
        pass

