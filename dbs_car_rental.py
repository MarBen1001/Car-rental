############  Mary Hennessy 10345121    

############  CA 2  ################  





from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

    #reads in Cars from excel sheet to process - may not read backout!
class  CarRental(object):  


    def __init__(self):
    
        self.cars={}
        self.cars_petrol={}           
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
        self.customer_list =[]
        
    def get_list_of_cars(self):   # get list of cars and process into categories
        if len(self.petrol_list)==0 and len(self.electric_list)==0:
            if len(self.diesel_list)==0 and len(self.hybrid_list)==0:
                filehandle = open('carlist.csv') #get list of cars from excel file
                for line in filehandle:
                    carline = line.rstrip()
                    car_details = carline.split(',')
                    self.carlist1.append(carline) # use this to check returns
                    print '___________________________________________________________________ \n'
           
                    print 'Car Number Identifer =',car_details[1:3]
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
            print '\nPETROL CARS:\n',self.petrol_list, '\nTotal number of Petrol Cars available =',len(self.petrol_list),'\n'  
            print 'ELECTRIC CARS:\n',self.electric_list, '\nTotal number of Electric Cars available =',len(self.electric_list) ,'\n' 
            print 'DIESEL CARS:\n',self.diesel_list, '\nTotal number of Diesel Cars available =',len(self.diesel_list), '\n' 
            print 'HYBRID CARS:\n',self.hybrid_list, '\nTotal number of Hybrid Cars available =',len(self.hybrid_list),'\n' 
        

            carrental.rental_welcome_menu()
        else:
            print 'List already exists'
            carrental.rental_welcome_menu()  
       
###################
#############PETROL
        
    def rent_petrol_car(self):
        print 'Rent car'
        try:
            customer_number = raw_input ('enter you customer number\n>')
            cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
           
        self.customer_record.append(customer_number) #acreate customer record
        
        for i in range(cars_needed):                #number of cars required
            if len(self.petrol_list)>=cars_needed:
                carout = self.petrol_list.pop()     #take last car from petrol list
                self.petrol_rented.append(carout)   #add car to petrol rented list
                self.customer_record.append(carout) #add car to customer record
            else: 
                print'Sorry only',len(self.electric_list),'Petrol Cars available'
                return
        
        print   '\n self.customer_list'        
        print   '\n\nlistof petrol cars rented =',self.petrol_rented
        print  '\n\nThank you for renting:',self.customer_record,'\n\n'
            
        print  self.petrol_list, '\nTotal number of Petrol Cars available =',len(self.petrol_list), '\n' 
        
        return
        
        #car return
    def return_petrol_car(self):
        print 'Return Car'
        print self.petrol_rented
        try:
            car_returned = int(raw_input(' Enter list position?\n>'))-1 #as list starts[0]
        except:
            return
        if len(self.petrol_rented)>0:
            carin = self.petrol_rented[car_returned]
            self.petrol_rented.pop(car_returned)
            print carin
            self.petrol_list.insert (0,carin)
        else:
            print 'No cars out'
            return 

        print  self.petrol_list, '\nTotal number of Petrol Cars available =',len(self.petrol_list), '\n'     
         
        return
         
###################
#########ELECTRIC   
  
     
            
    def rent_electric_car(self):
    
        print 'Rent car'
        try:
            customer_number = raw_input ('enter you customer number\n>')
            cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
        
        self.customer_record.append(customer_number)
        
        for i in range(cars_needed):
            if len(self.electric_list)>=cars_needed:
                carout = self.electric_list.pop() 
                self.electric_rented.append(carout)
                self.customer_record.append(carout) 
            else: 
                print'Sorry only',len(self.electric_list),'Petrol Cars available'
                return
                    
        print   '\n\n',self.electric_rented
        print  '\n\nThank you for renting:',self.customer_record,'\n\n'
            
        print  self.electric_list, '\nTotal number of Electric Cars available =',len(self.electric_list), '\n' 
        
        return
        
        #car return
    def return_electric_car(self):
        print 'Return Car'
        print self.electric_rented
        try:
            car_returned = int(raw_input(' Enter list position?\n>'))-1 #as list starts[0]
        except:
            return
        if len(self.electric_rented)>0:
            carin = self.electric_rented[car_returned]
            self.electric_rented.pop(car_returned)
            print carin
            self.electric_list.insert (0,carin) 
        else:
            print 'No cars out'
            return 

        print  self.electric_list, '\nTotal number of Electric Cars available =',len(self.electric_list), '\n' 
            
        return
        
###################
#############DIESEL
        
    def rent_diesel_car(self):
        print 'Rent car'
        try:
            customer_number = raw_input ('enter you customer number\n>')
            cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
           
        self.customer_record.append(customer_number)
        
        for i in range(cars_needed):
            if len(self.diesel_list)>=cars_needed:
                carout = self.diesel_list.pop() 
                self.diesel_rented.append(carout)
                self.customer_record.append(carout)
            else: 
                print'Sorry only',len(self.diesel_list),'Diesel Cars available'
                return
         
        print   '\n\n',self.diesel_rented
        print  '\n\nThank you for renting:',self.customer_record,'\n\n'
            
        print  self.diesel_list, 'Total number of Diesel Cars available =',len(self.diesel_list), '\n' 
        
        return
        
        #car return
    def return_diesel_car(self):
        print 'Return Car'
        print self.diesel_rented
        try:
            car_returned = int(raw_input(' Enter list position?\n>'))-1 #as list starts[0]
        except:
            return
        if len(self.diesel_rented)>0:
            carin = self.diesel_rented[car_returned]
            self.diesel_rented.pop(car_returned)
            print carin
            self.diesel_list.insert (0,carin) 
        else:
            print 'No cars out'
            return 
 
            
        
        print  self.diesel_list, 'Total number of Diesel Cars available =',len(self.diesel_list), '\n'  

        return


###################
#############HYBRID
        
    def rent_hybrid_car(self):
        print 'Rent car'
        try:
            customer_number = raw_input ('enter you customer number\n>')
            cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
           
        self.customer_record.append(customer_number)
        
        for i in range(cars_needed):
            if len(self.hybrid_list)>=cars_needed:
                carout = self.hybrid_list.pop() 
                self.hybrid_rented.append(carout)
                self.customer_record.append(carout)
                carout = HybridCar()
                colour= raw_input('what colour is this car?\n>')
                carout.setColour = (colour) #check re inheritance down the line Car..ElectricCar..HybridCar         
            else: 
                print'Sorry only',len(self.electric_list),'Hybrid Cars available'
                return
                      
        print   '\n\n',self.hybrid_rented,'Your Car Colour is', carout.setColour 
        print  '\n\nThank you for renting:',self.customer_record,'\n\n'
            
        print  self.hybrid_list, 'Total number of Hybrid Cars available =',len(self.hybrid_list), '\n' #cars left
        
        return
        
        #car return
    def return_hybrid_car(self):
        print 'Return Car'
        print self.hybrid_rented
        try:
            car_returned = int(raw_input(' Enter list position?\n>'))-1 #as list starts[0]
        except:
            return
        if len(self.hybrid_rented)>0:
            carin = self.hybrid_rented[car_returned]
            self.hybrid_rented.pop(car_returned)
            print carin
            self.hybrid_list.insert (0,carin)
             
        else:
            print 'No cars out'
            return 
            
        
        print  self.hybrid_list, 'Total number of Hybrid Cars available =',len(self.hybrid_list), '\n'  

        return
        
    #######################################
      
    
    def rentalandreturn_fuel_menu(self):
        
        print ' 1:  Petrol Car'
        print ' 2:  Electric Car'
        print ' 3:  Diesel Car'
        print ' 4:  Hybrid Car'
        
        print 'to rent or return a car select from following menu 1,2,3 or 4'
        
        choice = raw_input('Enter Number(1 or 2 or ... etc) of Required Selection\n\n>') 

        if choice == '1' :
            print 'Petrol Car'
            choice2 = raw_input('Enter 1 for CAR RENTAL : Enter 2 for CAR RETURN\n>')
            if choice2 == '1':
                    self.rent_petrol_car()
            elif choice2 =='2':
                    self.return_petrol_car()
            else:
                print 'Invalid Selection'
            return
        elif choice == '2' :
            print 'Electric Car'
            choice2 = raw_input('Enter 1 for CAR RENTAL : Enter 2 for CAR RETURN\n>')
            if choice2 == '1':
                    self.rent_electric_car()
            elif choice2 =='2':
                    self.return_electric_car()
            else:
                print 'Invalid Selection'
            return
        elif choice == '3' :
            print 'Diesel Car'
            choice2 = raw_input('Enter 1 for CAR RENTAL : Enter 2 for CAR RETURN\n>')
            if choice2 == '1':
                    self.rent_diesel_car()
            elif choice2 =='2':
                    self.return_diesel_car()
            else:
                print 'Invalid Selection'
            return
       
        elif choice == '4' :
            print 'Hybrid Car'
            choice2 =raw_input('Enter 1 for CAR RENTAL : Enter 2 for CAR RETURN\n>')
            if choice2 == '1':
                    self.rent_hybrid_car()
            elif choice2 =='2':
                    self.return_hybrid_car()
            else:
                print 'Invalid Selection'
            return
        
        else:
            print 'Invalid Selection'
        return
        
    def rental_welcome_menu(self):
    
        print ' 1: Browse'
        print ' 2: Rental'  
        print ' 3: Return Car'  
        
        greeting = raw_input('Enter Number(1 or 2 or ... etc) of Required Selection\n\n>') 
            
        if greeting == '1':
            self.browse()
        elif greeting == '2':
            self.rentalandreturn_fuel_menu()
        elif greeting == '3':
            self.rentalandreturn_fuel_menu()
        else:
            print 'Invalid Choice' 
        return 
            
    def browse(self):
        filehandle = open('carlist.csv')
        for line in filehandle:
            carline = line.rstrip()
            print carline
            print '___________________________________'
            
        self.rentalandreturn_fuel_menu()
        return              


 ################################     
      

if __name__ == '__main__':
 
    carrental = CarRental()
    
    input = raw_input('Welcome - do you need list of cars imported? \n >Y or N:  ') 
    if  input == 'Y' or input == 'y': 
        carrental.get_list_of_cars()     
    else:  
        carrental.rental_welcome_menu()
        
    while True:
        
        input = raw_input ("Enter 'y': Rental Menu or 'get': Import Car List ")      # call Main Menu function
    
       
        if input =='y' or input =='Y' or input == '':  # accept y,Y,return to proceed
            carrental.rental_welcome_menu()
        elif input== 'get':
            carrental.get_list_of_cars()
        else:
            exit()                                                   # and if not program ends




