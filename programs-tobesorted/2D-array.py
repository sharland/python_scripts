#declare how many students to enter
no_of_students = int(input('how many students?'))
# create 2 empty lists
lstStudents = []
lstMarks = []

for i in range(no_of_students):
        name = input('name ')
        #add name to end of students list
        lstStudents.append(name)
        mark = int(input('mark '))
        #add mark to end of mark list
        lstMarks.append(mark)              

#create a 2D list [students, marks]
lstStudent_Marks =[lstStudents, lstMarks]
#initialise total for average calculation
total = 0
for i in range(no_of_students):
    # for each of the 'no_of_students' entries print from the 2 listd
    print('name:',lstStudents[i],lstMarks[i])
    # accumulate the total
    total = total + lstMarks[i]
    
print('total ', total)
average = total/no_of_students
print('average ', average)

print('end')

