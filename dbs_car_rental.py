from car_new import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

 
    
class  CarRental(object):  




    def __init__(self):
    
        self.cars={}
        self.cars_petrol={}           #reads in Cars from excel sheet to process - may not read backout!
        self.cars_electric={}
        self.cars_diesel={}
        self.cars_hybrid={}
       
        self.rented = []              #fifo append returns to end - borrow from beginning - keep cars turning over
        self.carlist1 =[]
        self.petrol_list =[]
        self.diesel_list =[]
        self.hybrid_list =[]
        self.electric_list =[]
        
        

        
    def get_list_of_cars(self):   # get list of cars and process into categories
        filehandle = open('carlist.csv') #get list of cars from excel file
        for line in filehandle:
            carline = line.rstrip()
            
            print '______________________________________'
            print carline
            print '______________________________________'
            self.carlist1.append(carline)
        
            
            word = carline.split(',')
            fuel = word[0]
            
            
         
            # counting dictionaries
            self.cars[fuel] = self.cars.get(fuel,0)+1
            if fuel == 'Petrol':
                self.cars_petrol[fuel] = self.cars_petrol.get(fuel,0)+1
            if fuel == 'Electric':
                self.cars_electric[fuel] = self.cars_electric.get(fuel,0)+1
            if fuel == 'Diesel':
                self.cars_diesel[fuel] = self.cars_diesel.get(fuel,0)+1   
            if fuel == 'Hybrid':
                self.cars_hybrid[fuel] = self.cars_hybrid.get(fuel,0)+1              
                
            #self.list = list()

        #return num_p_cars
        #print num_p_cars    
            
            

        print self.cars
        print self.cars_petrol
        print self.cars_electric
        print self.cars_diesel
        print self.cars_hybrid
          
          
        #print '\n\n',self.petrollist,'\n\n' ,self.diesellist,'\n\n',self.hybridlist,'\n\n',self.electriclist,'\n\n'
        

        self.carlist = list()
        for key,value in self.cars.items():
            print self.carlist.append((value, key)),'\n\n\n\n'

       
        input =5
        self.cars_petrol[fuel] = self.cars_petrol.get(fuel,0)- input # cars out
        

        input2= 3
        self.cars_petrol[fuel] = self.cars_petrol.get(fuel,0) + input2 # cars in



        carback = 'car'
        self.carlist.append(carback)
        print self.carlist1,'\n\n\n '

        for i in range(5):

            carout = self.carlist1.pop() 
            self.rented.append(carout)
            
            print '\n',carout,'\n'  #car being rented
            place = carout.split(',')

            print place [1] # unique id of car being rented

    
        print self.carlist1, '\n\n\n'
        print self.rented, 'end'
        print len(self.rented)

        
        returnlist = len(self.rented)  #cannot add more cars than available
                                        #check car out before adding back

        self.carlist1.insert(0,carout) #error - adds last car out 5 times - user input here
        
            
    
        print self.carlist1,'\n\n\n'
        print self.rented

        carout = HybridCar()

        carout.setMake = ('Honda Civic Hybrid') #check re inheritance down the line Car..ElectricCar..HybridCar

        print carout.setMake       
        
        
        
        
        
        
        
        
    
    def rental_transmission_menu(self):
        print ' 1:  Automatic'
        print ' 2:  Manual'
        self.handle_choices()
        
    
    def rental_fuel_menu(self):
        print ' 1:  Petrol Car'
        print ' 2:  Electric Car'
        print ' 3:  Diesel Car'
        print ' 4:  Hybrid Car'
        
        choice = raw_input('Enter Number(1 or 2 or ... etc) of Required Selection\n\n>') 
        return choice

        
    def rental_petrol_car(self):
        print 'pello'
        for key,value in self.cars_petrol.items():
            self.petrol_list.append((value, key))
        num_p_cars = self.petrol_list[0]

        print num_p_cars
        if num_p_cars>1:
            how_many = int(raw_input ('how many petrol cars would you like?\n>'))
        print how_many
        if how_many<num_p_cars:
            print 'sorry ',how_many,'petrol cars in not stock'
        else:
            num_p_cars = num_p_cars - how_many
            print num_p_cars
            
            
    def rental_electric_car(self):
        print 'ello'
        
    def rental_diesel_car(self):
        print 'dello'
        
    def rental_hybrid_car(self):
        print 'hello'
        
    def rental_welcome_menu(self):
    
        print ' 1: Browse'
        print ' 2: Rental'  
        print ' 3: Extend Rental Due Date'
        print ' 4: Return Car'  
        
         
        greeting = raw_input('Enter Number(1 or 2 or ... etc) of Required Selection\n\n>') 
        return greeting

            
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
                                
      
      
    def rent_a_car(self):
        print 'rent'
           
    def renew_a_rental(self):
        print ' renew'
        
        
    def return_a_car(self):
        print 'return'
      
      

if __name__ == '__main__':

    
    #words = open('carlist.txt').readlines()
    #print map(lambda x: x.strip(), words)
    
    
    carrental = CarRental()

    carrental.get_list_of_cars()
    
    
    
    
    greetings = carrental.rental_welcome_menu()
    
    if greetings == '1':
        print 'here'
        carrental.browse()
    elif greetings == '2':
        carrental.rent_a_car()
    elif greetings == '3':
        carrental.renew_a_rental()
    elif greetings == '4':
        carrental.return_a_car()
    else:
        print 'Invalid Choice'    
        
      
      
        
    choices = carrental.rental_fuel_menu()
    
    if choices == '1':
        carrental.rental_petrol_car()
    elif choices == '2':
        carrental.rental_electric_car()
    elif choices == '3':
        carrental.rental_diesel_car()
    elif choices == '4':
        carrental.rental_hybrid_car()
    else:
        print 'Invalid Choice'   
   
        
        

    
    
    
        
         
    input = raw_input ("Enter 'y' to proceed to Main Menu")      # call Main Menu function
    
    if not input =='y' and not input =='Y' and not input == '':  # accept y,Y,return to proceed
        exit()                                                   # and if not program ends



# add 40 cars from today

#enter todays date todays date

#check car availability by checking date?

#rental return date

