__author__ = 'cmotevasselani'

from abc import abstractmethod, ABCMeta


class Byah:

    __metaclass__ = ABCMeta

    @abstractmethod
    def fix_me(self):
        raise NotImplemented("Fix me!")



class ByahFixed(Byah):


    def fix_me(self):
        print "Fixed"


class NotFixed(Byah):

    def blah(self):
        print "hey"

byahFixed = ByahFixed()
byahFixed.fix_me()

# Will fail
# notFixed = NotFixed()