__author__ = 'cmotevasselani'

from abc import abstractmethod, ABCMeta


class AbstractMethodSample:

    __metaclass__ = ABCMeta

    @abstractmethod
    def fix_me(self):
        raise NotImplemented("Fix me!")



class AbstractMethodSamplesFixed(AbstractMethodSample):


    def fix_me(self):
        print "Fixed"


class AbstractMethodSamplesNotFixed(AbstractMethodSample):

    def blah(self):
        print "hey"

byahFixed = AbstractMethodSamplesFixed()
byahFixed.fix_me()

# Will fail
# notFixed = NotFixed()
