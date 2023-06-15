## Find array Qu from codeWars in py .. 
## https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/python
def find_array(arr1, arr2):
    arr3 = []
    if len(arr1) == 0 or len(arr2) == 0 :
        return arr3
    else:
        for x in arr2:
             if x < len(arr1):
                arr3.append(arr1[x])
        return arr3
