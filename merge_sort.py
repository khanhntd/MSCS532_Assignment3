import random

# quickSort will following the three steps:
# Step 1: Choose the pivot (first element of the array)
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3: Repeat the same for the left side and right side
# Time complexity: O(n log n) (O(n^2) when the array is sorted either in descending or ascending)
# Space complexity: O(log n) (O(n) when the array is sorted either in descending or ascending)
# https://en.wikipedia.org/wiki/Quicksort
def quickSort(array: list[int]) -> list[int]:
  if len(array) <= 1:
    return array

  # Step 1: Choose pivot as the first element of the array
  pivot = array[0]

  # Step 2: Parition the array into two sides
  leftArray = [element for element in array[1:] if element < pivot] # Smaller than the pivot
  rightArray = [element for element in array[1:] if element >= pivot] # Larger than the pivot

  # Step 3: Repeat the same operation for left side and right side
  return quickSort(leftArray) + [pivot] + quickSort(rightArray)

# randomizedQuickSort will mostly do the same with quick sort; however,
# it also increases the randomness in choosing the pivot to
# reduce the likelihood of consistently picking a poor pivot.
# Time complexity: O(n log n) (O(n^2) when the array is sorted either in descending or ascending)
# Space complexity: O(log n) (O(n) when the array is sorted either in descending or ascending)
def randomizedQuickSort(array: list[int]) -> list[int]:
  if len(array) <= 1:
    return array

  # Step 1: Choose the pivot randomly by using random pivot selection
  # https://www.baeldung.com/cs/randomized-quicksort
  # since some algorithms for choosing pivot can be costly if not choosing
  # correcly (e.g medium of 3 for fixed position can be leveraged
  # https://programmingpraxis.com/2016/11/08/a-median-of-three-killer-sequence/)
  pivot = array[random.randint(0, len(array) - 1) % (len(array))]
  # Step 2: Parition the array into two sides
  leftArray = [element for element in array[1:] if element < pivot] # Smaller than the pivot
  rightArray = [element for element in array[1:] if element >= pivot] # Larger than the pivot
  # Step 3: Repeat the same operation for left side and right side
  return quickSort(leftArray) + [pivot] + quickSort(rightArray)

# generateArray will generate the corresponding array (e.g reverse sorted array)
def generateArray(numberOfElements: int, isSort: bool, sortIncreasing: bool, isRepeatingElement: bool) -> list[int]:
  array = []

  if isRepeatingElement:
    array = [random.randint(1, 1) for _ in range(0, numberOfElements)]
  else:
    array = [random.randint(0, 200) for _ in range(0, numberOfElements)]
  if (isSort):
    if sortIncreasing:
      array.sort()
    else:
      array.sort(reverse=True)

  return array

# printArray will print all the elements in the array
def printArray(array: list[int]):
    for i in range(len(array)):
        print(array[i], end=" ")
    print("\n")

def runningSort():
  arr = generateArray(numberOfElements=10, isSort=False,sortIncreasing=False, isRepeatingElement= True)
  print("Before sorting")
  printArray(arr)
  sortedArray = randomizedQuickSort(arr)
  print("After sorting ")
  printArray(sortedArray)