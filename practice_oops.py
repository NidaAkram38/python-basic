class Vechile:
    model=2024
    make="in china"
    def startengine(self):
      print("start car and goooo!!")
        
class Car(Vechile):
    num_doors=4
    def startengine(self):
      print("this car willnever let you down")
    
obj=Car()
obj.startengine()