
############  Mary Hennessy 10345121    

############  CA 2  ################  



class Car(object):

    
    def __init__(self):                 # car object implementation
    
        self.seating_capacity =''
        self.engine_size =''
        self.__make =''
        self.__mileage =0
        self.__number =''
        self.__transmission =''
        self.__colour=''
        
    def getColour(self):
        return self.__colour
    
    def getMake(self):
        return self.__make
        
    def getMileage(self):
        return self.__mileage
        
    def getNumber(self):
        return self.__number
        
    def getTransmission(self):
        return self.__transmission
    
    def setColour(self,colour):
        self.__colour = colour
    
    def setMake (self,make):
        self.__make = make
    
    def setMileage(self,mileage):
        self.__mileage = mileage
        
    def setNumber(self,number):
        self.__number = number
        
    def setTransmission(self,transmission):
        if self.__transmission == 'Manual' or self.__transmission == 'Automatic':
            self.__transmission = transmission
        else:
            print 'Error - Manual or Automatic only'
            
        
    def move(self, distance):
        if distance>0:
            self.__mileage = self.__mileage + distance
            return self.__mileage
        else:
            print ' distance must be > 0'
            return 
        
    def assignmake(self, make): #shouldnt need this
        self.__make = model
        return self.__model
    

class DieselCar(Car):                       # car object implementation
                                            # Mercedes E350 BlueTEC, Volkswagen Passat TDI
    def __init__(self):
        Car.__init__(self)
        self.engine_type=''              # 4 stroke, 2 stroke
        self.__engine_charge=''            # Turbo, Super
                    
              
          
    def getEngineType(self):
        return self.__engine_type
        
    def setEngineType(self,engine_type):
        self.__engine_type = engine_type  
        
             
    def getEngineCharge(self):
        return self.__engine_charge
        
    def setEngineCharge(self,engine_charge):
        self.__engine_charge = engine_charge  
                


class ElectricCar(Car):  
                 
    def __init__(self):
        Car.__init__(self)
        self.__number_fuel_cells = 1
        self.__battery_type =''         #Lithium-ion, Lead_acid, Zebra, Nickel
        self.__make = ''                     #, Lada Ellada, Toyota iQ EV



    def getBatteryType(self):
        return self.__battery_type
        
    def setBatteryType(self,battery_type):
        self.__battery_type = battery_type


    def getNumberFuelCells(self):
        return self.__number_fuel_cells
        
    def setNumberFuelCells(self,number_fuel_cells):
        self.__number_fuel_cells = number_fuel_cells
        
        

# When the term hybrid vehicle is used, it most often refers to a Hybrid electric vehicle(wikipedia). 

class HybridCar(ElectricCar):  # Honda Civic Hybrid,Toyota Prius, BMW i3

    def __init__(self):
        ElectricCar.__init__(self)
        self.__hybrid_type =''          # Mild parallel(Honda Civic Hybrid), series-parallel hybrid (Toyota Prius), Series hybrid (BMW i3)

    def getHybridType(self):
        return self.__hybrid_type
        
    def setHybridType(self,hybrid_type):
        self.__hybrid_type = hybrid_type
 


class PetrolCar(Car):                   # Opel Zafira, Citroen Picasso, Volvo XC90

    def __init__(self):
        Car.__init__(self)
        self.__cylinders =''           # 4, 6, 8 cylinders
                            
    
    
    def getCylinders(self):
        return self.__cylinders
        
    def setCylinders(self,cylinders):
        self.__cylinders = cylinders
 
    

    
    

