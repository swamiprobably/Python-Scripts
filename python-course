method = 'is a positive number' #Assign a string to a variable
valid = True

while valid:        #Use of while loop
    num = int(raw_input("Please enter a number in the range 1 to 100: ")) #Assign an integer to a variable
    if num>= 1 and num <= 100: #Use of logical operator
        valid = False
    else:
        print("Sorry number must be between 1 and 100")
        print("Please try again")
print("You entered {0}".format(num)) #Print out the assigned variable
print("This is a valid number and is a positive integer.")

num2 = float(raw_input('Enter a decimal number in the range 1 to 10 (i.e. 2.71): ')) #Assign a float to a variable
if num2 > 0 or num2 <=10:  #Use of logical operator
    print ('{} is a positive float.').format(num2) #Print out the assigned variable
elif num2 < 0:  #conditional statement
    print ('{} is a negative float.').format(num2) #Print out the assigned variable
else:       #conditional statement
    print ("This number doesn't exist!")

print ("\n")

def add_num(num, num2):
    a = num + num2          #Use of operator
    print ('Your whole number and decimal number added together is equal to: {}').format(a)  

def sub_num(num, num2):
    a = num - num2          #Use of operator
    print ('Your whole number subtracted from your decimal number is equal to: {}').format(a)

def mul_num(num, num2):
    a = num * num2          #Use of operator
    print ('Your whole number multiplied by your decimal number is equal to: {}').format(a)

def div_num(num, num2):
    a = num / num2          #Use of operator
    print ('Your whole number divided by your decimal number is equal to: {}').format(a)

def mod_num(num,num2):
    a = num % num2          #Use of operator
    print ('Your whole number divided by your decimal number has a remainder of: {}').format(a)

add_num(num,num2)
sub_num(num,num2)
mul_num(num,num2)
div_num(num,num2)
mod_num(num,num2)
add_num(num,num2)

print ("\n")

famous_numbers = ['2.71','3.14', '1', '0']                          #Create a list
famous_people = ['Euler', 'Archimedes', 'Brahmagupta', 'Hippasus']  #Create a list

name = (raw_input('What is your name?  ')).capitalize()
name not in famous_people   #Use of logical operator
print ("Sorry {}, you aren't famous yet!").format(name)

print ('These are famous mathematicians: {}').format(famous_people) #Iterate through list
print ('These are famous numbers: {}').format(famous_numbers)       #Iterate through list

dictA = dict(zip(famous_people,famous_numbers))
print ('This person discovered this number:')
print dictA

print ("\n")

science = ('Tesla', 'Einstein', 'Feynman', 'Newton')   #Use of a tuple

def extra(): #Iterate through a tuple  #define function that calls a string variable
    for person in science: #Use of a for loop
        print ('{} was an exemplary human being.').format(person) #Print out tuple
        
extra() #call function


