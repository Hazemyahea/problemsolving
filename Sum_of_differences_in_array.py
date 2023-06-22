## https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python

def sum_of_differences(arr):
    newarr =  sorted(arr,reverse=True)
    result = 0
    for x in range(len(newarr)-1):
        result+= newarr[x] - newarr[x+1]
    return result
