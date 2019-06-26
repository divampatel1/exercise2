#pre-work Question 1 --
#creat function to display Hello Username
#with the username as a variable

def hello_username(user_name) :
    """ DOCSTRING: Tell the end user of this function what it is used for. AND What it expects. """
    print("Hello " + user_name )

hello_username( "Divam" )   

#Prework Question 2 - Print 100 Odd Numbers

def odd_numbers():
    for value in range(1,100,2) :
        print (value) 

#prework Question 3 -Find max number in the list

def find_max_number(a_list):
    max(a_list)


number_list = [2,3,56,8,9,100]
find_max_number(number_list)


# Prework Question 4 -- write a function
# To find out if a given year is a leap year or not

def is_leap_year(year):
        # Leap year if divisible by 4, 100, 400
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
                print (True)
        else:
                print (False) 

is_leap_year(2062)



# Prework question 5 -- check to see if numbers in the list are consecutive

def consecusitive_number (a_list) :
        for i in range (1,len9(a_list)) :
        if a_list[i] - 1 != a_list[i-1]:
                return False
        return True




# hello_username(user_name)
# odd_number()
# number_list =[2,3,,56,8,9,100]
# find max number (number list)
# is_leap_year(year)