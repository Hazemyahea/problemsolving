## https://www.codewars.com/kata/5a2be17aee1aaefe2a000151

def array_plus_array(arr1,arr2):
    index= 0
    arr1sum = 0
    arr2sum = 0
    ## while loop to add and sum every elemnt  in each array in diffrent varaible
    ## Using while loop and the condition is sum two array elemnt - index (index is varble start from 0 and in every loop +1 ) > 0
    while len(arr1) + len( arr2) - index > 0 :
        if len(arr1) - index > 0:
            arr1sum+=arr1[index]
        if len(arr2) - index > 0:
            arr2sum+=arr2[index]
        index = index +1
    return arr1sum + arr2sum
    
    ## idon't know but i'm so happy in this solutions in used while loop form my mind :D .. to avoid usint two loops Although it will be the same rate of time, but I feel that this solution is better
