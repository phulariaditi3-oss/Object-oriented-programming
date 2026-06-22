class co:
    def dept(self,stdN,stdC,stdP):
        self.stdN1=stdN
        self.stdC1=stdC
        self.stdP1=stdP

    def show(self):
        print("student info:",self.stdC1,self.stdP1,self.stdN1)

c1=co()
c1.dept(101,"computer",92)
c1.show()