import csv
import pandas as pd

print('Welcome to Student Data Manager!')
print('1. Enter Student Data \n2. Read Student Record\n\n')
operations = int(input('Enter the serial number of the function you wish to perform '))

if operations == 1:
    f = open('percentage.csv', 'a', newline='')
    a = csv.writer(f)

    # a.writerow(['StudentID', 'rollno', 'name', 'mobileNo', 'emailID', 'address', 'p1','p2','p3','p4','p5','total', 'percentage', 'status'])

    iterations = int(input('enter the no of records: '))

    for i in range(0,iterations):
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

        total = p1 + p2 + p3 + p4 + p5
        percentage = total/5

        if percentage >= 35:
            status = 'pass'
        else:
            status = 'fail'


        a.writerow([StudentID, rollno, name, mobileNO, emailID, address, p1,p2,p3,p4,p5,total, percentage, status])
    print('record saved!')

elif operations == 2:
    # with open('percentage.csv', mode='r') as csv_file:
    # contents = csv_file.read()
    f = pd.read_csv('/home/hp/Documents/College/Coding/ACT - Technical/percentage.csv')
    StudentID_input = int(input('\nenter your student id: '))
    for index, value in enumerate(f['StudentID']):
        if value == StudentID_input:
            print(f.iloc[index, :])
            

else :
    print('enter valid input')