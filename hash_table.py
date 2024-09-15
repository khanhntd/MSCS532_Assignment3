class Node:
  def __init__(self, key: int, value: any) -> None:
    self.key = key
    self.value = value
    self.next = None

class UnorderedMap:
  def __init__(self) -> None:
        self.capacity = 30
        self.array = [None] * self.capacity

  def hashingKey(self, key: int) -> int:
    # https://www.geeksforgeeks.org/mid-square-hashing/
    # using mid square hashing for uniformly distributed to minimize collision as much as possible
    extractDigits = 4
    squareKey = str(key ** 2)
    squareKeyStr = str(squareKey)
    startStrIndex = (len(squareKeyStr) - extractDigits) // 2
    midDigitsStr = squareKeyStr[startStrIndex: startStrIndex + extractDigits]
    midDigits = int(midDigitsStr)
    return midDigits % len(self.array)

  # Insert will insert the key to the hash map
  # after determine the hashing index
  # However, if there is a collision, the key will be added
  # at the beginning of the linked list
  # Time Complexity: O(1)
  def insert(self, key: int, value: any) -> None:
    bucketIndex = self.hashingKey(key)
    newNode = Node(key = key, value = value)
    if self.array[bucketIndex] is None:
      self.array[bucketIndex] = newNode
    else:
      newNode.next = self.array[bucketIndex]
      self.array[bucketIndex] = newNode

  # search will search the key from the hash map
  # after determine the hashing index
  # The more distributed for the data we have the better. We can use bisect
  # to improve to logn
  # https://docs.python.org/3/library/bisect.html
  # Time Complexity: O(n) (best is O(1))
  def search(self, key: int) -> int:
    bucketIndex = self.hashingKey(key)
    bucketHead = self.array[bucketIndex]

    while bucketHead is not None:
      if bucketHead.key == key:
        return bucketHead.value
      bucketHead = bucketHead.next

    return -1

  # search will remove the key from the hash map
  # after determine the hashing index
  # Time Complexity: O(n) (best is O(1))
  def remove(self, key:int) -> None:
    bucketIndex = self.hashingKey(key)
    bucketHead = self.array[bucketIndex]

    if bucketHead is None:
      print("The key does not exist in table", key)
      return

    if bucketHead.key == key:
      self.array[bucketIndex] = bucketHead.next
      return

    previousNode = None
    currentNode = self.array[bucketIndex]
    while currentNode is not None:
      if currentNode.key == key:
        break
      previousNode = currentNode
      currentNode = currentNode.next

    if currentNode is None:
      print("The key does not exist in table", key)
    else:
      previousNode.next = currentNode.next
    return

  def printDistribution(self) -> None:
    for bucketIndex in range(len(self.array)):
      numberOfElements = 0
      bucketHead = self.array[bucketIndex]
      if bucketHead is not None:
        while bucketHead is not None:
          numberOfElements += 1
          bucketHead = bucketHead.next
        print("Number of elements at bucket index", bucketIndex, " is ", numberOfElements)


def runningHashCollison() -> None:
  hashMap = UnorderedMap()
  hashMap.insert(16, "March")
  hashMap.insert(35, "FeiXiao")
  hashMap.insert(55, "Yunli")
  hashMap.insert(70, "Moze")
  hashMap.insert(75, "Hanabi")
  hashMap.insert(89, "Firefly")
  hashMap.insert(93, "Clara")
  hashMap.insert(20, "Huohuo")
  hashMap.insert(61, "Robin")
  hashMap.insert(12, "Topaz")
  hashMap.insert(6, "Tingyun")

  hashMap.printDistribution()

  print("Removing Tingyun from HashMap")
  hashMap.remove(6)
  print("Value of 35:", hashMap.search(17))
  print("Value of 35:", hashMap.search(35))
  print("Value of 6:", hashMap.search(6))
  print("Value of 89:", hashMap.search(89))
