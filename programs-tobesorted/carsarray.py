import decimal
# create 4 empty lists
lstCarFile = []

for i in range(0,2):
        lstCar = []
        
        make = input('make ')
        #add make to start of car list
        lstCar.append(make)
        
        model = input('model ')
#add model to car list
        lstCar.append(model)
        
        engine_size = int(input('engine_size '))
#add engine_size to car list
        lstCar.append(engine_size)
        
        price = float(input('price'))
#add price to  car list
        lstCar.append(price)
        
#ADD THE CAR TO THE LIST OF ALL CARS
        lstCarFile.append(lstCar)
        
    

    # for each of the 'no_of_students' entries print from the 5 cars lists
for i in range(0,2):
        lstPrintCar = lstCarFile[i]
        print('Make: ',lstPrintCar[0],'Model: ',lstPrintCar[1],'Engine Size: ',lstPrintCar[2],'Price: £',round(lstPrintCar[3],2))
        print('')
              
              
       
