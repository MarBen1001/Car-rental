#from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

    
    
    
class  CarRental(object):  


    def __init__(self):
        self.diesel_cars = []
        self.electric_cars = []
        self.hybrid_cars = []
        self.petrol_cars = [] #fifo append returns to end - borrow from beginning - keep cars turning over
        
    
    def rental_transmission_menu(self):
        print ' 1:  Automatic'
        print ' 2:  Manual'
        self.handle_choices()
        
    
    def rental_fuel_menu(self):
        print ' 1:  Diesel Car'
        print ' 2:  Electric Car'
        print ' 3:  Hybrid Car'
        print ' 4:  Petrol Car'
        self.handle_choices()
        
        
    def rental_size_menu(self):
        print ' 1: Economy'
        print ' 2: Mid-range'
        print ' 3: Large'
        print ' 4: 7 seater'
        self.handle_choices()
    
        
    def rental_welcome_menu(self):
        print ' 1: Browse'
        print ' 2: Rental'  
        print ' 3: Extend Rental Due Date'
        print ' 4: Return Car'   
        self.handle_choices()
        print 'here'
        self.rental_welcome_choice()
       
    
    def rental_welcome_choice(self):
    
        if self.handle_choices == 1:
            self.browse()
        elif self.greeting == 2:
            self.rent_a_car()
        elif self.greeting == 3:
            self.renew_a_rental()
        elif self.greeting == 4:
            self.return_a_car()
            
        #else: print 'error'     # not valid choices handled by handle_choices
        
    def browse(self):
        
        filehandle = open('carlist.csv')
        for line in filehandle:
            carline = line.rstrip()
            print carline
        
    def rental_selection_banner(self):    
        print  ' Car Fuel  Menu\n\n '
        print  ' Car Size  Menu\n\n '
        print  ' Car Transmission  Menu\n\n ' 
        print  ' Car ' 
        self.handle_choices()   
                                
      
    def handle_choices(self):  # for use with menus for data entry
        try:
            greeting = raw_input('Enter Number(1 or 2 or ... etc) of Required Selection\n\n>') 
            #print greeting 
                    
        except:
            print 'Invalid Choice'
            
#reads in Cars from excel sheet
    def import_cars(self):
        cars={}

        filehandle = open('carlist.csv')
        for line in filehandle:
            line = line.rstrip()
            print line
            word = line.split(',')
            fuel = word[1]
            cars[fuel] = cars.get(fuel,0)+1

        carlist = list()
        for key,value in cars.items():
                carlist.append((value, key))

        carlist.sort()
        print carlist
        input = raw_input('select car')
        number = input
        numbers = ('1','2','3','4','5','6','7','8','9')
        if isinstance (number, numbers):
            print number
            

       

if __name__ == '__main__':

    
    #words = open('carlist.txt').readlines()
    #print map(lambda x: x.strip(), words)
    
    
    carrental = CarRental()
    
    while True:
        #carrental.import_cars()
        carrental.rental_welcome_menu() 
        input = raw_input ("Enter 'y' to proceed to Main Menu")      # call Main Menu function
    
        if not input =='y' and not input =='Y' and not input == '':  # accept y,Y,return to proceed
            exit()                                                   # and if not program ends



# add 40 cars from today

#enter todays date todays date

#check car availability by checking date?

#rental return date

