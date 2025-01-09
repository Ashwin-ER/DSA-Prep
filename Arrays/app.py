a = [0, 1, 2, 0, 5, 0, 8, 9, 0]
num = int(input('Enter num='))
index = []
for i in range(len(a)):
    if a[i]==num:
        index.append(i)
if index:
    print(f"found {num} at {index}th index")
else:
    print(f'the number {num} not found in index')