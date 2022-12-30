import csv
import pandas as pd


operations = 0
iterations = 0
StudentID = 0
rollno = 0
name = '' 
mobileNO = ''
emailID = '' 
address = '' 
p1=0
p2=0
p3 =0
p4=0
p5 = 0
total = 0 
percentage = 0
status = ''
StudentID_input = 0

print('Welcome to Student Data Manager!')
print('1. Enter Student Data \n2. Read Student Record\n\n')
try:
    operations = int(input('Enter the serial number of the function you wish to perform '))
except ValueError as message:
    print('enter input as integer only : ', message)



if operations == 1:
    try:
        f = open('percentage-error-handling.csv', 'a', newline='')
        a = csv.writer(f)
    except FileNotFoundError as message:
        print('File not found : ', message)

    # a.writerow(['StudentID', 'rollno', 'name', 'mobileNo', 'emailID', 'address', 'p1','p2','p3','p4','p5','total', 'percentage', 'status'])
    try:
        iterations = int(input('enter the no of records: '))    #taking input the no. of records one wants to enter
    except ValueError as message:
        print('Enter the value as integer only : ', message)

    for i in range(0,iterations):
        try:
            StudentID = int(input('enter student ID'))
            rollno = int(input('enter student roll no'))
            name = input('enter student name')
            mobileNO = int(input('enter student mobile no'))
            emailID = input('enter student email id')
            address = input('enter student address')
            p1 = int(input('enter percentage of subject 1'))
            p2 = int(input('enter percentage of subject 2'))
            p3 = int(input('enter percentage of subject 3'))
            p4 = int(input('enter percentage of subject 4'))
            p5 = int(input('enter percentage of subject 5'))
        
        except ValueError as message:
            print('Enter valid input ', message)

        total = p1 + p2 + p3 + p4 + p5
        percentage = total/5

        if percentage >= 35:
            status = 'pass'
        else:
            status = 'fail'

        
        a.writerow([StudentID, rollno, name, mobileNO, emailID, address, p1,p2,p3,p4,p5,total, percentage, status])
        print('record saved!')

elif operations == 2:
    try:
        f = pd.read_csv('/home/hp/Documents/College/Coding/ACT - Technical/exception handling/percentage-error-handling.csv')
    except FileNotFoundError as message:
        print('file not found : ', message)
        
    try:
        StudentID_input = int(input('\nenter your student id: '))
    except ValueError as message:
        print('enter input as integer only : ', message)
    for index, value in enumerate(f['StudentID']):
        if value == StudentID_input:
            print(f.iloc[index, :])
        # if value != StudentID_input:
        #     print('StudentID not found!')

else :
    print('enter valid input')