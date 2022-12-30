def welcome(fname, lname):
    '''
    Prints out your first and last name
    '''
    print(f'First Name is {fname}')
    print(f'Last Name is {lname}')

def square(n):
    '''
    Prints the square of a number
    '''
    print(n**2)

def login(username , password):
    '''
    Maps the username and password for login purposes
    '''
    if username == password:
        print('You have logged in successfully')
    else:
        print('You have entered the wrong credentials')

pi = 3.145