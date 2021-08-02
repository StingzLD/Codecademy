def count(N):
    count = 0
    while N > 1:
        N = N // 2
        count += 1
    return count


print(count(1))
num_iterations_1 = 0  # REPLACE
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

print(count(2))
num_iterations_2 = 1  # REPLACE
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

print(count(4))
num_iterations_4 = 2  # REPLACE
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

print(count(32))
num_iterations_32 = 5  # REPLACE
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

print(count(64))
num_iterations_64 = 6  # REPLACE
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))
