


class Car(object)

    def __init__(self):
    
    
        self.seating_capacity =''
        self.engine_size = ''
        self.__make = ''
        self.__mileage = 0
        self.__number_plate = ''
        self.__gearbox+''





class DieselCar(Car)

        def __init__(self):
        Car.__init__(self)
        self.engine_type ''              # 4 stroke, 2 stroke
        self.engine_charge ''            # Turbo, Super



class ElectricCar(Car)                   #fiat 500e, Lada Ellada, Toyota iQ EV
    def __init__(self):
        Car.__init__(self)
        self.__number_fuel_cells = 1
        self.__battery_type = ''         #Lithium-ion, Lead_acid, Zebra, Nickel




# When the term hybrid vehicle is used, it most often refers to a Hybrid electric vehicle. 
class HybridCar(ElectricCar)
    def __init__(self):
        ElectricCar.__init__(self)
        self.__hybrid_type = ''          # Mild parallel(Honda Civic Hybrid), series-parallel hybrid (Toyota Prius), Series hybrid (BMW i3)






class PetrolCar(Car)
    def __init__(self):
        Car.__init__(self)
        self.__cylinders = ' '
    
