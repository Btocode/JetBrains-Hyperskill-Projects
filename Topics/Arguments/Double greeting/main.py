num = input()
num_int = [int(each) for each in num]
new = []
for i in range(1, len(num_int), 1):
    temp = num_int[i] + num_int[i-1]
    new.append(temp)
print(new)