from flask import request
from common.utils.strutil import *

class JJService(object):
    def __init__(self, request):
        self.code = 0
        self.data = None
        self.request = request
   
#protected methods, to be override
    def _parse_request(self):
        return True
    
    def _check_parameters(self):
        return True

    def _authenticate(self):
        return True

    def _handle_data(self):
        return self.__class__.__name__ 

    def _handle_error(self):
        return self.__class__.__name__ 


#should not be override!!
    def handle(self):
        self._parse_request()

        if self._check_parameters() and self._authenticate():
            return self._handle_data()
        else:
            return self._handle_error()
 
