#from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

    
    
    
class  Car_Rental(object):  


    def __init__(self):
        self.diesel_cars = []
        self.electric_cars = []
        self.hybrid_cars = []
        self.petrol_cars = []
        
#fifo append returns to end - borrow from beginning - keep cars turning over
    
    
    def rent_a_car_menu(self):
    
    
    
        print '      Car Selection Menu\n\n '
        print ' 1:  Diesel Car'
        print ' 2:  Electric Car'
        print ' 3:  Hybrid Car'
        print ' 4:  Petrol Car'
        
    
    
        q_2 = raw_input('What Kind of Car Do You Want? Enter 1, 2, 3,or 4 from Menu above\n>>')
        return
        
        
    def greetings(self):
        
        q_1 = raw_input('Do you want to rent a car? Enter "y" or "n" \n>>')

        if q_1 == 'y':
            self.rent_a_car_menu()
            
        elif q_1 == 'n':

            q_3 = raw_input('Do you want to renew your rental? Enter "y" or "n"\n>>')
        
            if q_3 == 'y':
                #will change path here - requires Numberplate to find specific car to renew
                self.rent_a_car_menu()    
            
            elif q_3 == 'n':     
                q_4 = raw_input('Ok - goodbye - please Enter "y" to start again') 
                self.farewell()
        else:
            print 'Only valid selections are "y" or "n"'
            return
    
    def farewell(self):
        print 'happy motoring'

rental = Car_Rental()
if __name__ == '__main__':


    rental.greetings()
    
    rental.farewell()
   
    
        
        
    

                
            
                
                
                
                
            
                











# add 40 cars from today

#enter todays date todays date

#check car availability by checking date?

#rental return date

