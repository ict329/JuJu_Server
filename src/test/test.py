class A:
    
    svar = "hello static var!!"
    def __init__(self):
        self.a = 'hello a'

    def func(self):
        print self.a

    @staticmethod
    def sta():
        print "Static Method!!!"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = "hello b"

    def func(self):
        print self.b

a = A()

print a.svar;
print A.svar;
print a.__dict__
