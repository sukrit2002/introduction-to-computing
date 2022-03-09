count=0
def bubbleSort(array):
 for i in range(len(array)):
  swapped = False
  for j in range(0, len(array) - i - 1):
   if array[j] > array[j + 1]:
    temp = array[j]
    array[j] = array[j+1]
    array[j+1] = temp

    swapped = True
    if not swapped:
     break


val=[4,5,2,4,5,6,2,3,4,5,7]
print("Input array : ")
print(val)

bubbleSort(val)

print("Sorted array : ")
print(val)


def binary_search(arr, x):
 low = 0
 high = len(arr) - 1
 mid = 0
 while low <= high:
  mid = (high + low) // 2
  if arr[mid] < x:
   low = mid + 1
  elif arr[mid] > x:
   high = mid - 1
  else:
   return mid
 return -1
  
arr=val
x = 3
result = binary_search(arr, x)
if result != -1:
 print("Element is present at index",
 str(result))
 count+=1
else:
 print("Element is not present in array!")

print("Number of occurrences of element 4 is : ",count)

