from service.service import JJService 

class RegisterService(JJService):
    def __init__(self, request):
        JJService.__init__(self, request)

    
    def _handle_data(self):
        return "HAHA" 
