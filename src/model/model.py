from pbmodel.basic_pb2 import *

class JJModel(object):

    def __init__(self):
        pass
        
    def __init__(self, oid):
        self.oid = oid

    def save(self):
        pass

    def delete(self):
        pass

    def to_proto(self):
        pass
    
    def table_name(self):
        return "" 

    def orm_key_list(self): 
        return ()

    def proto_key_list(self):
        return ()

