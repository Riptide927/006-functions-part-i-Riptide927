#! python3
import problem1


def test1():
  # Problem 1 Assertions
  assert problem1.hypotenuse(3,4,False) == 5

def test2():
  assert problem1.hypotenuse(13,5,True) == 12
