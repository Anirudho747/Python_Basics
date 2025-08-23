list1 = [7,23,34,10,56,23,23,10,34,56,23,33,11,23,34]
print(list1)

# Step 1: Slice the list from index 3 to the end
part1 = list1[3:]

# Step 2: Slice the list from start to index 3
part2 = list1[:3]

# Step 3: Concatenate both parts
rotated = part1 + part2

print(rotated)

