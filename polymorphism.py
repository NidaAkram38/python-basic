#class Ni:
  #  def displayinfo(self,name=""):  #overloading
   #     print("I am NIDA"+ name)
        
#obj=Ni()
#obj.displayinfo()        
#obj.displayinfo("Python")     


class Ni:                            #overriding
    def displayinfo(self):  
        print("I am NIDA")
        

class Wi(Ni):                         
    def displayinfo(self):  
        super().displayinfo()                       #for calling parent function super is used buz of same func name
        print("I am WARISHA")
        
obj=Wi()
obj.displayinfo()