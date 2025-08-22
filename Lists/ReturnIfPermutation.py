list1 = ["A","big","monkey","got","lost","in","the","jangle"]
list2 = ["A","bog","monkey","got","lost","in","the","jangle"]
flag=0
list1.sort()
list2.sort()

print(f"{list1}")
print(f"{list2}")

if list1 == list2 :
        print("Anagram")
else:
    print("Not an Anagram")



