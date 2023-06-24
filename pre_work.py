#Question 1
#Write a function to print "hello_USERNAME" USERNAME is the input of the function.
def hello_name(USERNAME):
    print ("hello_" + str(USERNAME) + "!")
    return

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100
#and returns nothing.
def first_odds():
    for value in range(1,101):
        if value % 2 == 1:
            print (value)
    return

#first_odds()

#Question 3
#Write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    #print (max(a_list))
    return max(a_list)


#max_num_in_list([4,384,348,993,84])
#max_num_in_list([94,49,348,4949])
#max_num_in_list([2,484,538,82])
#max_num_in_list([43,85,93,188,652])

#Question 4
#Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 > 0:
            #print (True)
            return True
    elif a_year % 400 == 0:
                #print(True)
                return True
    else:

        #print(False)
        return False

#is_leap_year(2004)
#is_leap_year(2008)
#is_leap_year(3128)
#is_leap_year(2199)
#is_leap_year(7257)

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    consec = True #set bool to auto True
    check_num = a_list[0] #est a comp num
    for num in a_list:
        #print(num)
        #print(check_num)
        if (num + 1) != (check_num + 1): #check if nums increment the same
            consec = False #set to false
            #print(consec)
        check_num += 1
    return consec

#is_consecutive([1,2,3,4,5])
#is_consecutive([1,2,4,6])
