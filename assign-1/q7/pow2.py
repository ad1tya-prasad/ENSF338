
import timeit

def pow2(n):
    return 2**n

def pow2_for_loop(n):
    result = []
    for i in range(n + 1):
        result.append(2**i)
    return result

def pow2_list_comprehension(n):
    return [2**i for i in range(n + 1)]


# for loop function
start = timeit.default_timer()
for i in range(1000):
    pow2_for_loop(1000)
end = timeit.default_timer()
print("Time taken for for loop function: ",end - start)

# list comprehension function
start = timeit.default_timer()
for i in range(1000):
    pow2_list_comprehension(1000)
end = timeit.default_timer()
print("Time taken for list comprehension function: ",end - start)
