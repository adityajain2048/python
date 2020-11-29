numbers=[12,234,324,521,5332,1212,4222,2,4,40]
prev=0
largest=numbers[0]

for i in range(1,len(numbers)):
    if numbers[i]>largest:
        prev=largest
        largest=numbers[i]
print(prev)

