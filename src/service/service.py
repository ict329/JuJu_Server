from flask import request

class JJService(object):
    def __init__(self):
        self.code = 0
        self.data = None

    def parse_data(self, request):
        return True
    
    def handle_data(self):
        return self.__class__.__name__ 
