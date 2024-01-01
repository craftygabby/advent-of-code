
inputs = []

with open('dec1_part2_test_input.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip())
        
print(inputs)
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
integers = []
set = []
for ele in inputs:
    
    for num in nums:
        if num in ele:
            print(num)
            set.append(nums.index(num))
            continue
    print(set)
    # if len(set) == 1:
    #     set.append(set[0])
    integers.append(set)
    
    set = []
print(integers)
# for ele in nums:
#     for line in inputs:
#         if ele in line:
#             print(ele)
print("eles NOT IN CORRECT ORDER YET and haven't accounted for numbers as actual digits yet")