my_original_list=[12,24,35,24,88,120,155,88,120,155]
my_set=set(my_original_list)
remove_duplicate_with_index_maintain=[]
for i in my_original_list :
    if i in my_set:
                remove_duplicate_with_index_maintain.append(i)
                my_set.remove(i)
print(remove_duplicate_with_index_maintain)
                    
