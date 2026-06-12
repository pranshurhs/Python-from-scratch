n = int(input("type number of participants "))
unique_list = set(map(int(input("enter numbers  "))))
sorted_list = sorted(unique_list)
print(sorted_list[-2])
