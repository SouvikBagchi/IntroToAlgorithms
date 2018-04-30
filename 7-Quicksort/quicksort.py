class Quicksort():


 def sort(self,arr):
  #INITIALIZE LESS, MORE AND EQUAL ARRAY
  less_arr = []
  more_arr = []
  equal_arr = [] 

  if(len(arr)>1):
   pivot = arr[0]
   for element in arr:
    if element < pivot :
     less_arr.append(element)
    if element > pivot :
     more_arr.append(element)
    if element == pivot:
     equal_arr.append(element)

   return self.sort(less_arr)+equal_arr+self.sort(more_arr)

  else :
   self.sorted = arr
   return arr


test_arr = [55,67,21,38,97,45,27,59,82]
test = Quicksort()
sorted = test.sort(test_arr)