from service import JJService

def handle_request(request, service):

    flag = service.parse_data(request)
    response = None

    if flag:
        response = service.handle_data()
    else:
        code = service.code
    #TODO set response with the error code
    return response 
