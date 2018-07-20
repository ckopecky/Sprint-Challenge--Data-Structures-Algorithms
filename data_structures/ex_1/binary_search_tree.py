class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #call cb on the current binary search tree node
    #recursion
    cb(self.value):
    #if self.left exists
    if self.left != None:
      self.left.depth_first_for_each(cb)
    #if self.right exists:
    if self.right != None:
      self.right.depth_first_for_each(cb)
    return

    #when hits a point when there are no more left-most branches, goes back up to most
    #recent cb. then will invoke the self.right. If no right...goes back up one more

    #iterative

    stack = [self]
    #iterate through elements in the stack

    while len(stack):
      #pop off the top-most stack element
      curr = stack.pop()
      #check to see if curr has right child
      if curr.right:
        stack.append(curr.right)
      if curr.left:
        stack.append(curr.left)
      #call the cb
      cb(curr.value)
    
  def breadth_first_for_each(self, cb):
    #iterative
    queue = [self]
    while len(queue) > 0 :
      curr = queue.pop(0)
      cb(curr.value)
      if curr.left != None:
        queue.append(curr.left)
      if curr.right != None:
        queue.append(curr.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
