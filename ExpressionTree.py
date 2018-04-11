#  File: ExpressionTree.py

#  Description: Creates an expression tree

#  Student's Name: Matthew Frangos

#  Student's UT EID: msf955

#  Partner's Name: Braeden Conrad

#  Partner's UT EID: bsc875

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 4/11/2018

#  Date Last Modified: 4/11/2018

operators=['+', '-', '*', '/']

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  def createTree (self, expr):
  	array=expr.split()
  	for val in array:
  		if(val=='('):




  def evaluate (self, aNode):


  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print(aNode.data)

def main():

main()
  
'''
def operate (oper1, oper2, token):
  if (token == "+"):
    return oper1 + oper2
  elif (token == "-"):
    return oper1 - oper2
  elif (token == "*"):
    return oper1 * oper2
  elif (token == "/"):
    return oper1 / oper2
 
def rpn (s):
  theStack = Stack()

  operators = ["+", "-", "*", "/"]

  tokens = s.split()

  for item in tokens:
    if (item in operators):
      oper2 = theStack.pop()
      oper1 = theStack.pop()
      theStack.push (operate (oper1, oper2, item))
    else:
      theStack.push (float(item))

  return theStack.pop()'''