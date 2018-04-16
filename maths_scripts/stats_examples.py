import statistics

example_list = [5,2,5,6,7,1,23,1,2,6,3,5,5]

print("list",example_list)

x = statistics.mean(example_list)
print("mean value:",x)

y = statistics.median(example_list)
print("median value:",y)

z = statistics.mode(example_list)
print("mode value:",z)

a = statistics.stdev(example_list)
print("standard deviation:",a)

b = statistics.variance(example_list)
print("variance:",b)
