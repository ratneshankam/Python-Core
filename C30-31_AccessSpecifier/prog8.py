class A:
    def fun(self):
        print("A:fun")

class B:
    def fun(self):
        print("B:fun")

class C:
    def fun(self):
        print("C:fun")

class D(A,B):
    def fun(self):
        print("D:fun")
        super().fun()

class E(B,C):
    def fun(self):
        print("E:fun")
        super().fun()

class F(D,E):
    def fun(self):
        print("F:fun")
        super().fun()

obj = F()
obj.fun()
print(F.mro())