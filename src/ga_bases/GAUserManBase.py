from GABase import GABase

class GAUserMan(GABase):
    def __init__(self, auth=None):
        super(GABase,self).__init__()
        self.authentication = auth

    def add(self, usr, grps=None):
        gservice=self.authentication.gservice
        listOfEmpties = ["", [], {}, None]
        if isinstance(grps, basestring):
            self.adding_result = self.add_user_to_group(gservice, 
                                                        usr, 
                                                        grps)
        elif isinstance(grps, list):
            for grp in grps:
                self.adding_result = self.add_user_to_group(gservice,
                                                            usr, 
                                                            grp)
                print self.adding_result
        elif grps in listOfEmpties:
            self.all_groups = self.get_all_groups(gservice)
            for grp in self.all_groups:
                self.adding_result = self.add_user_to_group(gservice, 
                                                            usr, 
                                                            grp)
                print self.adding_result
        else:
            print "Please provide valid group(s)\n"
