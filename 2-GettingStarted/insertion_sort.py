import datetime
class InsertionSort():

 def __init__(self, array):
  self.array = array

#This method sorts the array by the insertion sort technique and prints the sorted array as well as returns it
#This method also returns the time it takes to sort the array
 def sort(self):
  print("Original array : "+str(self.array))
  sorted_array = self.array
  current_time = datetime.datetime.now()
  for i in range(1,len(sorted_array)-1):
   # print("array is ")
   # print(sorted_array)
   # print("i is ")
   # print(i)
   # print("ith element is ")
   # print(sorted_array[i])
   key = sorted_array[i]
   for j in range(0,i):
    # print("j is ")
    # print(j)
    # print('jth element is ')
    # print(sorted_array[j])
    

    if sorted_array[j] > key:
     #Store the jth element in a temporary space
     temp = sorted_array[j]
     # print('key is')
     # print(key)
     del sorted_array[i]
     sorted_array.insert(0,key)
     #Change the key after the swap
     key = temp

     # print("changed array ")
     # print(sorted_array)
     # print('')

    else:
     # print("breaking")
     # print('')
     break


  finished_time = datetime.datetime.now()
  
  print("Sorted array : "+ str(sorted_array))
  print("The time taken : "+str(finished_time-current_time))
  return sorted_array


 def printArray(self,array):
  for element in array:
   print(element)

y = InsertionSort([4,5,6,2,7])
final_array = y.sort()
print(final_array)