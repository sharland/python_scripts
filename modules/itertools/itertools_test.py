import itertools

stuff = [1,2,3]

permStuff = list(itertools.permutations(stuff, 3))
print(permStuff)