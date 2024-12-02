class A:
    def hablar(self):
        print("Desde A")


class B:
    def hablar(self):
        print("Desde B")


class C(B):
    def hablar(self):
        print("Desde C")


class D(A):
    def hablar(self):
        print("Desde D")


class E(D, C):
    def hablar(self):
        print("Desde E")


e = E()
print(E.mro())

print("-------------------------")
d = D()

C.hablar(d)
