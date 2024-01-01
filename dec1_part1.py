
                                                
inputs = []

with open('dec1_part1_input.txt', 'r') as f:
    for line in f:

        inputs.append(line.strip())

print(inputs)
adder = []
nums_lst = []
count = 0
sum = 0
addables = []
for ele in inputs:
    print(ele)
    integers = ''
    for ind, dig in enumerate(ele):
        #print(ind, dig)
        if dig.isnumeric():
            integers += dig
        else:
            continue
        print("integers", integers)

    nums_lst.append(integers[0])
    print(integers[0])
    print(integers[-1])
    nums_lst.append(integers[-1])
    addable = integers[0] + integers[-1]
    print("addable", addable)
    addables.append(addable)

# print(addables)
for num in addables:
    sum += int(num)
print(sum)