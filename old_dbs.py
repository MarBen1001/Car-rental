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
        
        
        
        
        
    