# functon to calculate the average of a list of numbers.
# this is  user defined function. - 'calAverage'
# 'len' function/method definition is built in python.

ages = [10, 20, 30, 40]               # array of numbers
incomes = [100, 200, 300, 400]

def calAverage(list):                    
    sum = 0;
    for i in list:                   # i = index variable...list is the inernal variable in the function.
        sum = sum + i;
    
    return sum/len(list)              # returns sum (100) / lenght of list (4)

print(calAverage(incomes))
