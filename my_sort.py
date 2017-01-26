list_one = [67, 45, 2, 13, 1, 998]
list_two = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def my_sort(list):
    new_list = []
    new_list.append(list[0])
    inserted = False

    for i in range(1, len(list)):
        for j in range(0, len(new_list)):
            if (list[i] < new_list[j]):
                if (j == 0):
                        new_list.insert(0, list[i])
                else:
                        new_list.insert(j, list[i])
                inserted = True
                break
        if(not inserted):
            new_list.append(list[i])
        inserted=False 

    print new_list
    
                    
        
my_sort(list_one)
my_sort(list_two)
