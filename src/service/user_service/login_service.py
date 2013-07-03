from service.service import JJService 

class LoginService(JJService):
    def __init__(self):
        JJService.__init__(self)

    def parse_data(self, request):
        return True
    
    def handle_data(self):
        return self.__class__.__name__
   

