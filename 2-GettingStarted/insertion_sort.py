import datetime
class InsertionSort():

 def __init__(self, array):
  self.array = array

#This method sorts the array by the insertion sort technique and prints the sorted array as well as returns it
#This method also returns the time it takes to sort the array
 def sort(self):
  current_time = datetime.datetime.now()
  sorted_array = [2,3,4]
  finished_time = datetime.datetime.now()
  
  print("The sorted numbers are : " + str(self.printArray(sorted_array)))


 def printArray(self,array):
  for element in array:
   print(element)

y = InsertionSort([4,5,6,2,7])
y.sort()