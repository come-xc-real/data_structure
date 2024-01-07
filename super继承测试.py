class A:
    def disp(self):
        print("A")


class B(A):
    def disp(self):
        print("B")
        super().disp()
        print("B")


class C(A):
    def disp(self):
        print("C")
        super().disp()
        print("C")


class D(B):
    def disp(self):
        print("D")
        super().disp()
        print("D")


if __name__ == '__main__':
    d = D()
    d.disp()

    b = B()
    b.disp()
