import itertools

stuff = ["x+xSin","y+ySin","x+xCos","y+yCos","x","y"]

permStuff = list(itertools.permutations(stuff, 6))
print(len(permStuff))