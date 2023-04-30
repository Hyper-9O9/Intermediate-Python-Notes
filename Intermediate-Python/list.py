# Lists: ordered, mutable, allows duplicate elements
mylist = ["apple", "banana", "cherry"]
print(mylist)

# you can create a list using list function
mylist2 = list()
print(mylist2)

# can contain different data types
mylist3 = [5, "apple", True, "apple"]
print(mylist3)

# you can print a specific item by specifying the item index
item = mylist3[2]
print(item)

# you can print an item from the end using -
item = mylist3[-1]
print(item)

# printing the items using iteration
for item in mylist3:
    print(item)

# checking for an item in the list
if "banana" in mylist3:
    print("you can go bananas")
else:
    print("no banana na :(")

# to show length of a list
print(len(mylist3))

# you can add items using append
mylist3.append("banana")
print(mylist3)

# to add item at a specific place use insert
mylist3.insert(0, "lemon")
print(mylist3)

# to take out the last item use pop
mylist3.pop()
print(mylist3)

# to remove a specifc item use remove
mylist3.remove(5)
print(mylist3)

# to clear the whole list use clear
mylist.clear()
print(mylist)

# to reverse a list items use reverse
mylist3.reverse()
print(mylist3)

# you can sort numbers for lists with sort
mylist4 = [3,5,8,9,0,-3,-2,2,434,6,1,-19]
mylist4.sort()
print(mylist4)

# you can sort a list and store it inside another one using sorted
new_list = sorted(mylist4)
print(new_list)

# if you want to make a list of repeated elements use * element#
zero_list = [0] * 4
print(zero_list)

# you can merge two lists together using list1 + list2
combine_list1 = [0,1,2,3,4]
combine_list2 = [5,6,7,8,9]
combined = combine_list1 + combine_list2
print(combined)

# if you want to get the items in a range of index use slice [start_index:end_index], or [:end_index] or [start_index:]
a = combined[2:6]
print(a)
b = combined[:6]
print(b)
c = combined[6:]
print(c)

# you can define the stepping [:: steps]
d = combined[::3] # from beginning till the end go by 3
print(d)
e = combined[2::]
print(e)

# you can refer two variables to the same list inside the memory as following
list_org = ['apple','banana','orange']
list_cpy = list_org
# if we add item to the copy list, the same item would be added to the original list
list_cpy.append('cherry')
print(f"this is the original list {list_org}")
print(f"this is the copy list {list_cpy}")
print()
# instead you can use copy method to make an actual copy
list_org = ['apple','banana','orange']
list_cpy = list_org.copy()
# now only the copy list will be different from the original memory space
list_cpy.append('cherry')
print(f"this is the original list {list_org}")
print(f"this is the copy list {list_cpy}")
print()

# you can make copy of list in two other ways
list_org = ['apple','banana','orange']
# by using list
list_cpy1 = list(list_org)
# by using slice
list_cpy2 = list_org[:]

list_cpy1.append('cherry')
list_cpy2.append('berry')
print(f"this is the original list {list_org}")
print(f"this is the copy 1  list {list_cpy1}")
print(f"this is the copy 2  list {list_cpy2}")
print()

# you can square your list numbers as following
mylist = [1,2,3,4,5,6,7]
squared_list = [i*i for i in mylist]

print(f"this is the original list {mylist}")
print(f"this is the Squared list {squared_list}")
print()