import array

arr = array.array('i',[1,2,3]) #signed integers for array values

print ("New array is: ", end="")
for i in range (0, 3):
    print (arr[i], end=" ")

print("\r")

arr.append(4) #append value to the end of the array

print("Appened array is: ", end="") #new array with 4 added
for i in range (0, 4):
    print (arr[i], end=" ")

arr.insert(2, 5) #insert 5 at the second position in the array

print("\r")

print("New array is: ", end="")
for i in range (0, 5):
    print (arr[i], end=" ")