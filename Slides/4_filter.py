fib = [0,1,1,2,3,5,8,13,21,34,55]

result = filter(lambda x : x%2, fib)
print(f"Odd numbers in {fib}: {list(result)}")
result = filter(lambda x : x%2 == 0, fib)
print(f"Evem numbers in {fib}: {list(result)}")