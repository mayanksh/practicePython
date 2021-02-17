import array

arr = array.array('i', [4, 6, 2, 6, 7, 8])

print("the new array is: ", end=" ")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")  # to move output in new line

arr.append(9)
print("the appended array is at the end: ", end=" ")
for i in range(0, 7):
    print(arr[i], end=" ")

print("\r")

arr.pop(6)
print("the array deleted is: ", end=" ")
for i in range(0, 6):
    print(arr[i], end=" ")