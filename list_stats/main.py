numbers = list(map(int, input().split(',')))

maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
average = total / len(numbers)

print(f"Max: {maximum}")
print(f"Min: {minimum}")
print(f"Sum: {total}")
print(f"Avg: {average}")
