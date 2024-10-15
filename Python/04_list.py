# it's a kind of array

items=["fruits","bread","vegetables","cold-drinks"]

# to access data at particular index we use indexing

items[0]="apples"

print(items)

# now the updated array is['apples', 'bread', 'vegetables', 'cold-drinks']

# to do conactination we can directly do that


grcoery_items=["Attta","Sause","Eggs","Toast"]
bathroom_items=["cleaner","soap","shamppo"]

merge_list=grcoery_items+bathroom_items

print(merge_list)


# to check the length we use len(function)

length_of_list=len(merge_list)

print(length_of_list)

# we can also generate sub list just similar to subStrings

subList=merge_list[0:5]

print(subList)


# We can use in method to check if something is present in the list or not. If value is present it will return true otherwise it will return false

check="Sause" in merge_list
print(check)