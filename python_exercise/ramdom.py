class car():
    
    def __init__(self,name,color):
        self.name=name   
        self.color= color
        
    def print_self(self) :
        print(self)
        print(self.name)
        print(self.color)
        print('/n')
    
      
        
bmw=car('bmw','black')
bmw.print_self()

obj2=car('audi','white')
obj2.print_self()

obj3=car('nano','red')
obj3.print_self()

class maruti(car):
    def print_nam(self):
        print('fgf')
        
class bmw(maruti):
    def print_hii(self):
        print('fgf') 
        
obj4=bmw('nav','blue')    
obj4.print_self()       

class harsh(maruti,car):
    def lakshita(self):
        print("hello lakhsita sinha")

obj5=harsh('harsh','sharma')
obj5.print_nam()
obj5.print_self()         

