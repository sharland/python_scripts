
# create 4 empty lists
lstLondon = []
lstManchester = []
lstOxford = []
lstSheffield = []
for i in range(0,4):
        lstCity = []
        city = input('city ')
        #add city to start of  list
        lstCity.append(city)
        for j in range(0,4):
                miles = input('miles ')
#add miles to London list
                lstCity.append(miles)
        if i == 0:
                lstLondon = lstCity
        if i == 1:
                lstManchester = lstCity
        if i == 2:
                lstOxford = lstCity
        if i == 3:
                lstSheffield = lstCity
print (lstLondon)
                
for i in range(0,5):
    # for each of the 'no_of_students' entries print from the 5 cars lists
    print(lstLondon[i],lstManchester[i],lstOxford[i],lstSheffield[i])
   


print('end')

