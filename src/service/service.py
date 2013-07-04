from flask import request
from common.utils.strutil import *

class JJService(object):
    def __init__(self, request):
        self.code = 0
        self.data = None
        self.request = request
    
    def parse_request(self):
        return True
    
    def handle_data(self):
        return self.__class__.__name__ 

    def check_parameters(self):
        return True

    def authenticate(self):
        return True

    def handle(self):

