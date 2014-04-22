#! /usr/local/bin/python3

# variables: 1 .. n

# example: x is rep by 1; y is rep by 2; z is rep by 3
# formula (x or ¬y) and z  represented by phi = {{1,-2}, {3}}
# v = {1,3} represents x=True  y=False  z=True
def eval_clause(v, c):
  for lit in c:
    if lit < 0:
      if -lit not in v:
        return True
    else:
      if lit in v:
        return True
  return False

def eval(v, phi):
  for clause in phi:
    if not eval_clause(v, clause):
      return False
  return True

print(eval([1,3], [[1,-2], [3]]))
print(eval([1], [[1,-2], [3]]))
