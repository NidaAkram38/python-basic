class Democlass:
    a=10
    b=20
    
    def __init__(self):
        print("TU PHIR KAISE HAIN APP LOGG??")
    
    def showvalue(self):   #using function
        print(self.a)
        print(self.b)
        self.c=self.a*self.b
        print(self.c)
              
    def showvalue1(self,e,f):   #using function
        print(e*f)
        
Demoobject=Democlass()
Demoobject.showvalue()    #using function
print(Demoobject.a)       #using simple oops
print(Demoobject.b)
Demoobject.showvalue1(6,4)    #using function

