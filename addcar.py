
#
from car_new import Car,HybridCar,ElectricCar


cars={}           #reads in Cars from excel sheet to process - may not read backout!
carlist1 =[]
petrollist =[]
diesellist =[]
hybridlist =[]
electriclist =[]

filehandle = open('carlist.csv')
for line in filehandle:
        carline = line.rstrip()
        #float(carline[0])
        #carline.sort()
       
        #print carline
        carlist1.append(carline)
        
        word = carline.split(',')
        
        #print word
        fuel = word[0]
        cars[fuel] = cars.get(fuel,0)+1
print cars
while not True:   # keep from printing for now    
    if fuel == 'Petrol':
        petrollist.append(word)
        print petrollist
        for car in petrollist:
            print car [1:3]      #car unique number and name
            
    elif fuel=='Diesel':
        diesellist.append(word)
        print diesellist
    elif fuel=='Hybrid':
        hybridlist.append(word)
        print hybridlist
    elif fuel == 'Electric':
        electriclist.append(word)
        print electriclist
        
print '\n\n',petrollist,'\n\n' ,diesellist,'\n\n',hybridlist,'\n\n',electriclist,'\n\n'
        

carlist = list()
for key,value in cars.items():
    carlist.append((value, key))

carlist.sort()

#print carlist1
#print carlist
#print cars
input =5
cars[fuel] = cars.get(fuel,0)- input

#print cars
input2= 3
cars[fuel] = cars.get(fuel,0) + input2
#print cars



#print carlist1[4]

carback = 'car'
carlist.append(carback)
carlist.sort()

print carlist1,'\n\n\n '

for i in range(5):

    carout = carlist1.pop() 
    print '\n',carout,'\n'  #car being rented
    place = carout.split(',')

    print place [1] # unique id of car being rented

    
print carlist1, '\n\n\n'

for i in range(5):

    #cannot add more cars than available
    #check car out before adding back

    carlist1.insert(0,carout) #error - adds last car out 5 times - user input here

    
print carlist1,'\n\n\n'

carout = HybridCar()

carout.setMake = ('Honda Civic Hybrid') #check re inheritance down the line Car..ElectricCar..HybridCar

print carout.setMake

