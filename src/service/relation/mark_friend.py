from service.service import JJService 

class MarkFriendService(JJService):
    def __init__():
        JJService.__init__()

    def parse_data(self, request):
        flag = JJService.parse_data(self, request)
        if flag:
            return True

        return False
    
    def handle_data(self):
        return self.__class__.__name__ 
