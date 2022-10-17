numbers = []
for i in range(5):
    numbers.append(int(input()))
sum(numbers)
avg = sum(numbers)/len(numbers)
for i in range(5): 
    if numbers[i] > avg:
        print(numbers[i], end=' ')
