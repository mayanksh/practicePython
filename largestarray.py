#def largest(array, n):

#    max = array[0]  #initialize array

#    for i in range (1, n):
#        if array[i] > max:
#            max = array[i]
#    return max

#array = [1,2,3,4,5]
#n = len(array)

#answer = largest(array, n)
#print("largest element is: " , answer)

arr=int(input('Enter the element of an array:')
n = len(arr)
def largest(arr,n):
    max = arr[0]
    for i in range(1, n):

        if arr[i] > max:
        max = arr[i]
    return max

Ans = largest(arr,n)
print ("Largest in given array is",Ans)
