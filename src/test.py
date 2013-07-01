import model.model

from pbmodel.basic_pb2 import PBLocation

def testcls(cls):
    cl = cls()
    cl.contury_code = 1243
    print cl


class Test(object):
    def __init__(self):
        self.a = 1
        self.aa = 4
        self.aaa= 6


test = Test()
print test.__dict__
test.b = 2
print test.__dict__
