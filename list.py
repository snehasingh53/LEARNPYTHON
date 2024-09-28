# CREATING LIST #
lst =[6,8,3,5,9,"sneha"]
print(lst)

##### INSERTING INTO LIST #####

# append list 
lst.append(53)
print("list after appending" ,lst)

# extend list
lst.extend([63,43,23,"singh"])
print("list after exteding",lst)

# insert function 
lst.insert(5,78)
print("list after inserting 78 at 5th index",lst)



###### REMOVING ITEM FROM THE LIST ######

#pop function
lst.pop()
print("List after popping last item",lst)
lst.pop(3)
print("list after popping element of index 3",lst)

#remove function 
lst.remove(78)
print("list after removing element 78",lst)


###### SORTING #####
lst2=[6,78,3,9,7]
lst2.sort()
print("List after sorting element in increasing order",lst2)

# sort in decreasing order
lst2.sort(reverse=True)
print("List after sorting element in decreasing order",lst2)




###### SLICING #######
lst[4:10:2]
print("list after performing slicing operation",lst)