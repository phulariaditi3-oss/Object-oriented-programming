class a:
    def show1(self):
      print("hii")

class b:
    def show2(self):
      print("hello")

class c(a,b):
   pass
   
obj=c()
obj.show1()
obj.show2()
