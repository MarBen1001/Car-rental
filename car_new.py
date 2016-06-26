
class Car(object):

    
    def __init__(self):                 # car object implementation
    
        self.seating_capacity ='?'
        self.engine_size ='?'
        self.__make ='?'
        self.__mileage =0
        self.__number ='?'
        self.__transmission ='?'
        
        
    def getMake(self):
        return self.__make
        
    def getMileage(self):
        return self.__mileage
        
    def getNumber(self):
        return self.__number
        
    def getTransmission(self):
        return self.__transmission
        
    def setMake (self,make):
        self.__make = make
    
    def setMileage(self,mileage):
        self.__mileage = mileage
        
    def setNumber(self,number):
        self.__number = number
        
    def setTransmission(self,transmission):
        self.__transmission = transmission
        
    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
        
    def assignmake(self, make): #shouldnt need this
        self.__make = model
        return self.__model
    

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.engine_type=''              # 4 stroke, 2 stroke
        self.__engine_charge=''            # Turbo, Super
        self.make =''                      # Mercedes E350 BlueTEC, Volkswagen Passat TDI
        
        
        
        
        
class Mercedes(Car):
    def __init__(self):
        Car.__init__(self)
        self.model='E350 BlueTEC'
        self.colour=''
        self.transmission=''
        self.fuel_type=''
    
class Volkswagen_Passat_TDI(DieselCar):

    def __init__(self):
        DieselCar.__init__(self)
        self.colour=''
        self.transmission=''


class ElectricCar(Car):  
                 
    def __init__(self):
        Car.__init__(self)
        self.__number_fuel_cells = 1
        self.__battery_type =''         #Lithium-ion, Lead_acid, Zebra, Nickel
        #self.__make                      #, Lada Ellada, Toyota iQ EV




# When the term hybrid vehicle is used, it most often refers to a Hybrid electric vehicle. 
class HybridCar(ElectricCar):

    def __init__(self):
        ElectricCar.__init__(self)
        self.__hybrid_type =''          # Mild parallel(Honda Civic Hybrid), series-parallel hybrid (Toyota Prius), Series hybrid (BMW i3)
        #self.__make''                    # Honda Civic Hybrid,Toyota Prius, BMW i3




class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__cylinders =''           # 4, 6, 8 cylinders
        self.make=''                     # Opel Zafira, Citroen Picasso, Volvo XC90
    
    
    
    
def move(self,distance):
    print ('New Mileage' +str(distance)+'kms.') 
    self.__mileage=self.__mileage +distance
    
    
    
    
    
    

