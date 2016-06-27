      
from car_new import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

    
class  CarRental(object):  


    def __init__(self):
    
        self.cars={}
        self.cars_petrol={}           #reads in Cars from excel sheet to process - may not read backout!
        self.cars_electric={}
        self.cars_diesel={}
        self.cars_hybrid={}
       
        self.petrol_rented = []              #fifo append returns to end - borrow from beginning - keep cars turning over
        self.electric_rented = []  
        self.diesel_rented = []  
        self.hybrid_rented = []  
        self.carlist1 =[]
        self.petrol_list =[]
        self.diesel_list =[]
        self.hybrid_list =[]
        self.electric_list =[]
        self.customer_record = []

        
    def get_list_of_cars(self):   # get list of cars and process into categories
        filehandle = open('carlist.csv') #get list of cars from excel file
        for line in filehandle:
            carline = line.rstrip()
            car_details = carline.split(',')
            self.carlist1.append(carline) # use this to check returns
            print '___________________________________________________________________ \n'
           
            print 'Car Number Identifer =',car_details[1],'for to rent',car_details[2]
            print '___________________________________________________________________'
            
         
            
            car_details = car_details[0]
            
            # counting dictionaries
            self.cars[car_details] = self.cars.get(car_details,0)+1
            
            if car_details == 'Petrol':
                self.petrol_list.append(carline)
                self.cars_petrol[car_details] = self.cars_petrol.get(car_details,0)+1
        
            if car_details == 'Electric':
                self.electric_list.append(carline)
                self.cars_electric[car_details] = self.cars_electric.get(car_details,0)+1
            if car_details == 'Diesel':
                self.diesel_list.append(carline)
                self.cars_diesel[car_details] = self.cars_diesel.get(car_details,0)+1   
            if car_details == 'Hybrid':
                self.hybrid_list.append(carline)
                self.cars_hybrid[car_details] = self.cars_hybrid.get(car_details,0)+1              
        print self.petrol_list, 'Total number of Petrol Cars available =',len(self.petrol_list),'\n'  
        print self.electric_list, 'Total number of Electric Cars available =',len(self.electric_list) ,'\n' 
        print self.diesel_list, 'Total number of Diesel Cars available =',len(self.diesel_list), '\n' 
        print self.hybrid_list, 'Total number of Hybrid Cars available =',len(self.hybrid_list),'\n' 
        
        print car_details 
        #input =5
        #while input>0:
           # carout = self.petrol_list.pop()     #rented car
            #self.petrol_rented.append(carout)   #add rented car to rented petrol list
            #input = input-1
        #print  self.petrol_list, 'Total number of Petrol Cars available =',len(self.petrol_list), '\n' 
        
        
        
        



        #carback = 'car'
        #self.petrol_list.append(carline)
        #print self.carlist1,'\n\n\n '
        next = self.rent_petrol_car()
        
    def rent_petrol_car(self):
        print 'Rent car'
        try:
            cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
            
        for i in range(cars_needed):

            carout = self.petrol_list.pop() 
            self.petrol_rented.append(carout)
            self.customer_record.append(carout)
            print '\n',carout,'\n'  #car being rented
            
        print   '\n\n',self.petrol_rented
        print  '\n\nThank you for renting:',self.customer_record,'\n\n'
            
        print  self.petrol_list, 'Total number of Petrol Cars available =',len(self.petrol_list), '\n' 
        
        
        #car return
    def return_car():
        print 'Return Car'
        print self.petrol_rented
        car_returned = int(raw_input (' enter ID of car you want to return?\n>'))
        if self.petrol_list.find(car_returned):
            print found
        for word in self.petrol_rented:
            print 'hello'
            if car_returned == word[1]:
                print ' successful'
                self.petrol_list.insert(0,carout)
            else:
                print'unsuccessful'
                
        print  self.petrol_list, 'Total number of Petrol Cars available =',len(self.petrol_list), '\n' 
            
        
        
            #place = carout.split(',')

            #print place [1] # unique id of car being rented

    
        #print self.carlist1, '\n\n\n'
        #print self.rented, 'end'
        #print len(self.rented)

        
        #returnlist = len(self.rented)  #cannot add more cars than available
                                        #check car out before adding back

        #self.carlist1.insert(0,carout) #error - adds last car out 5 times - user input here
        
            
    
        #print self.carlist1,'\n\n\n'
        #print self.rented

        #carout = HybridCar()

        #carout.setMake = ('Honda Civic Hybrid') #check re inheritance down the line Car..ElectricCar..HybridCar

        #print carout.setMake 
        
        
        
        
        
        
        
    
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

    input = raw_input('Welcome - do you need list of cars imported? \n >Y or N:  ')
    
    if  input == 'Y' or input == 'y':
    
        carrental.get_list_of_cars()
        
    else:
     
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
        carrental.rent_petrol_car()
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

