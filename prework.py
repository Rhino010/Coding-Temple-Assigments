#Question 1
user_name = "Ryan"

def hello_name(user_name):
    print ('Hello ',user_name,'!')

hello_name(user_name)


#Question 2
def first_odds():
    for i in range(1,100,2):
        print(i)

#Question 3
a_list = [1,2,100,4,5]

def max_num_in_list(a_list):
    a_list.sort()
    return(a_list[-1])
    
max_num_in_list(a_list)

#Question 4
def is_leap_year(year):
    #your code here. Try to do it in one line.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Question 5
a_list = 1,2,4,5

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

is_consecutive(a_list)
