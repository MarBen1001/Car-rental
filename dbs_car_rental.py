############  Mary Hennessy 10345121    

############  CA 2  ################  

#### When you start program - prompt will ask you to 'Y/N' import cars from  attached excel file  ###



from car import Car, DieselCar, ElectricCar, HybridCar, PetrolCar

    #prompts and if answer is yes: reads in Cars from excel sheet to process 
class  CarRental(object):  


    def __init__(self):
    
        self.cars={}
        self.cars_petrol={}           
        self.cars_electric={}
        self.cars_diesel={}
        self.cars_hybrid={}
       
        self.petrol_rented = []              
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
        self.colour_list = []
        
    #####################################################################
        
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
       
                    self.cars[car_details] = self.cars.get(car_details,0)+1                  # counting dictionaries
                    
                    if car_details == 'Petrol  ':
                        self.petrol_list.append(carline)
                        self.cars_petrol[car_details] = self.cars_petrol.get(car_details,0)+1
                    if car_details == 'Electric':
                        self.electric_list.append(carline)
                        self.cars_electric[car_details] = self.cars_electric.get(car_details,0)+1
                    if car_details == 'Diesel  ':
                        self.diesel_list.append(carline)
                        self.cars_diesel[car_details] = self.cars_diesel.get(car_details,0)+1   
                    if car_details == 'Hybrid  ':
                        self.hybrid_list.append(carline)
                        self.cars_hybrid[car_details] = self.cars_hybrid.get(car_details,0)+1              
            print '\nPETROL CARS:',self.cars_petrol,'\n',self.petrol_list, '\nTotal number of Petrol Cars available =',len(self.petrol_list),'\n'  
            print 'ELECTRIC CARS:',self.cars_electric,'\n',self.electric_list, '\nTotal number of Electric Cars available =',len(self.electric_list) ,'\n' 
            print 'DIESEL CARS:',self.cars_diesel,'\n',self.diesel_list, '\nTotal number of Diesel Cars available =',len(self.diesel_list), '\n' 
            print 'HYBRID CARS:',self.cars_hybrid,'\n',self.hybrid_list, '\nTotal number of Hybrid Cars available =',len(self.hybrid_list),'\n' 
            print 'TOTAL NUMBER OF CARS:\n', self.cars, '\n'

            self.rental_welcome_menu()
        else:
            print 'List already exists'
            self.rental_welcome_menu()  
       

############# PETROL ###################

        #car rental
    def rent_petrol_car(self):
    
        print 'Rent Petrol car'
        self.car_type='Petrol'
        self.this_list= self.petrol_list
        self.this_rented_list = self.petrol_rented
        self.choices()  
        print 'cars available =',self.this_list
        self.car_processing_out()
        return
        
        #car return
    def return_petrol_car(self):
        self.car_type='Petrol'
        self.this_rented_list = self.petrol_rented
        self.this_list= self.petrol_list
        print 'Return',self.car_type,' Car'
        for key in self.this_rented_list:
            print  key                  #self.this_rented_list
        self.car_processing_in()
        return
         

############## ELECTRIC  ##################

         #car rental    
    def rent_electric_car(self):
    
        self.car_type='Electric'
        self.this_list= self.electric_list
        self.this_rented_list = self.electric_rented
        print 'Rent', self.car_type ,'Car'
        self.choices()                          
        print 'cars available =',self.this_list
        self.car_processing_out()
        return
        
        #car return
    def return_electric_car(self):
        self.car_type='Electric'
        self.this_rented_list = self.electric_rented
        self.this_list= self.electric_list
        print 'Return',self.car_type,'Car'
        for key in self.this_rented_list:
            print  key
        self.car_processing_in()
        return
     

############## DIESEL ####################
        
         #car rental 
    def rent_diesel_car(self):
        self.car_type='Diesel'
        self.this_list= self.diesel_list
        self.this_rented_list = self.diesel_rented
        print 'Rent', self.car_type ,'Car'
        self.choices()                  
        print 'cars available =',self.this_list
        self.car_processing_out()

        #car return
    def return_diesel_car(self):
        self.car_type='Diesel'
        self.this_rented_list = self.diesel_rented
        self.this_list= self.diesel_list
        print 'Return',self.car_type,'Car'
        for key in self.this_rented_list:
            print  key
        self.car_processing_in()
        return



############# HYBRID ###################
        
    def rent_hybrid_car(self):
        self.car_type='Hybrid'
        self.this_list= self.hybrid_list
        self.this_rented_list = self.hybrid_rented
        print 'Rent', self.car_type ,'Car'
        self.choices()                  
        print 'cars available =',self.this_list
        self.car_processing_out()
        return
        
        #car return
    def return_hybrid_car(self):
        self.car_type='Hybrid'
        self.this_rented_list = self.hybrid_rented
        self.this_list= self.hybrid_list
        print 'Return',self.car_type,'Car'
        for key in self.this_rented_list:
            print  key
        self.car_processing_in()
        return
    
    ##################################################################
      
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
        
    #################################################################  
      
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
        
     ############################################################## 
           
    def browse(self):
        filehandle = open('carlist.csv')
        for line in filehandle:
            carline = line.rstrip()
            print carline
            print '___________________________________'
          
        self.rentalandreturn_fuel_menu()
        return    
    
    ##############################################################
    
    def choices(self):
        try:
            self.customer_number = raw_input ('enter you customer number\n>')    # formality only  - not processed further - accepts any input
            self.cars_needed = int(raw_input (' how many cars do you want?\n>'))
        except:
            print 'invalid input'
        self.customer_record.append(self.customer_number)                        # formality only  - not processed further
        return 
        
    ##############################################################
    
    def messages(self):
        print '\nThe above is a list of your rental car(s)'  
        print '\n\nThank you for renting:',self.number,'car(s)'
        print '\n\n ',self.car_type,' Cars now available = ',self.this_list,'\n'
        return

    ##############################################################
                       
    def car_processing_out(self):
        if len(self.this_list)>=self.cars_needed:
            self.number = 0
            for i in range(self.cars_needed):
                self.carout = self.this_list.pop()                  #car borrowed from end of list, returned to start of list
                self.number = self.number+1
                self.this_rented_list.append(self.carout)               
                self.customer_record.append(self.carout)
                if self.car_type == 'Hybrid':                                        #hybrid different as can colour- too messy to colour all the cars
                    self.cartaken =self.carout
                    self.carout = HybridCar()                                       # carout =as Car/subCar class setCol wont work without this line
                    colour= raw_input('what colour is this car?\n>')
                    self.colour_list.append(colour)
                    self.carout.setColour = (colour)                                #check re inheritance down the line Car..ElectricCar..HybridCar
                    print '\nYour', self.cartaken[12:], 'is', self.carout.setColour ,'\n'
                else:
                    print '\nRented:',self.carout[12:]
            if self.car_type == 'Hybrid':
                print '\n\nThank you for renting:',self.number,'Hybrid Car(s)'                
                print '\n\nHybrid Cars now available = ',self.hybrid_list ,'\n' 
            else: 
                    self.messages() 
        else: 
            print'Sorry only',len(self.this_list), self.car_type, 'Cars available'
        return
    
    #############################################################
            
    def car_processing_in(self):
        try:
            self.car_returned = int(raw_input(' Enter list position?\n>'))-1 #as list starts[0]
        except:
            return
        if len(self.this_rented_list)>0:
            self.carin = self.this_rented_list[self.car_returned]
            self.this_rented_list.pop(self.car_returned)
            print '\nYou have just returned:',self.carin,'\n'
            self.this_list.insert (0,self.carin)                   # car borrowed from end of list, returned to start of list
        else:
            print 'No',self.car_type,'cars out'
            return 
        print  self.this_list, '\nTotal number of',self.car_type,'Cars available =',len(self.this_list), '\n'     
        return
        
    ###############################################################    
      
   ############### Program starts here ###########################
   
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




