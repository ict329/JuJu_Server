from pbmodel.basic_pb2 import *


class JJField(object):
    def __init__(self, db_field, pb_field, value):
       self.db_field = db_field
       self.pb_field = pb_field
       self.value = value

    def update_proto(self, proto_model)
        if hasattr(proto_model, self.pb_field):
            setattr(proto_model, self.pb_field, value)

    


class JJModel(object):

    def __init__(self):
        pass
        
    def __init__(self, oid):
        self.oid = oid

    def __init__(self, cursor):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def to_proto(self, cls):
        proto = cls()
        for k, v in self.proto_dict():
            if hasattr(proto, k):
               setattr(proto, k, v) 

    def table_name(self):
        return "" 

    def orm_key_list(self): 
        return ()

    def proto_key_list(self):
        return ()
    
    def proto_dict(self):
        return self.items() 

