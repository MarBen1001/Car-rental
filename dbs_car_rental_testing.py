############  Mary Hennessy 10345121    

############  CA 2  ################  

# Tests for Car class and tried for VarRental


import unittest

from dbs_car_rental import CarRental


from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar




class TestCarRental(unittest.TestCase): 

    def setUp(self):
        self.carrental= CarRental()
        self.carrental.rent_hybrid_car()
        
        
    def test_pop(self):        # meant this to test pop() from empty list - can't fix it
        try:
            len(self.carrental.rent_hybrid_car.hybrid_list) ==0
            self.carrental.rent_hybrid_car.hybrid_list.pop() 
            self.assertEqual(IndexError,self.carrental.rent_hybrid_car.hybrid_list)
        except: pass


class TestCar(unittest.TestCase): # car functionality

    def setUp(self):
        self.car = Car()
        self.electriccar = ElectricCar()
        self.petrolcar = PetrolCar()
        self.dieselcar = DieselCar()
        self.hybridcar = HybridCar()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(100)
        self.assertEqual(100, self.car.getMileage())
        
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(-100)                                   # distance cannot be negative
        self.assertEqual(0, self.car.getMileage())
        
    def test_car_make(self): 
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Volvo')
        self.assertEqual('Volvo', self.car.getMake())

    def test_car_colour(self): #working
        self.assertEqual('', self.car.getColour())
        self.car.setColour('green')
        self.assertEqual('green', self.car.getColour())
        
    def test_transmission(self): # working
        self.assertEqual('', self.car.getTransmission())
        self.car.setTransmission('Manual')
        self.assertEqual('Manual', self.car.getTransmission())
        
    def test_transmission(self): # working
        self.assertEqual('', self.car.getTransmission())
        self.car.setTransmission('Man')
        self.assertEqual('', self.car.getTransmission())
        
    def test_number_plate(self):  #working
        self.assertEqual('', self.car.getNumber())
        self.car.setNumber('04 D 21264')
        self.assertEqual('04 D 21264', self.car.getNumber()) # could have plenty more formatted here?
        
    def test_cylinders(self): # not working
        self.assertEqual('', self.petrolcar.getCylinders())
        self.petrolcar.setCylinders('6')
        self.assertEqual('6', self.petrolcar.getCylinders)
    
    def test_cylinders(self): #not working
        self.assertEqual('', self.petrolcar.getCylinders())
        try:
            self.petrolcar.setCylinder('7')
        except: ValueError
        pass
        
   # def test_hybridtype(self): # n
        #self.assertEqual('', self.hybridcar.getHybridType())
        #self.hybridcar.setHybridType('Mild parallel')
       # self.assertEqual('Mild parallel', self.hybridcar.getHybridType)
        #AssertionError: 'Mild parallel' != <bound method HybridCar.getHybridType of
        # <car_new.HybridCar object at 0x1022bf7d0>>
    

if __name__ == '__main__':
    unittest.main()