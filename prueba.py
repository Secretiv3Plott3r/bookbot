def bubble_sort(nums,keys):
    swapping=True
    end=len(nums)
    while swapping:
        swapping=False
        for i in range(1,end):
            if nums[i-1] < nums[i]:  # Sorting DESCENDING
                nums[i], nums[i-1] = nums[i-1], nums[i]
                keys[i], keys[i-1] = keys[i-1], keys[i]
                swapping = True
        end-=1
    new_dict=convert_to_dict(nums,keys)
    return new_dict
def convert_to_dict(nums,keys):
    retu= dict(zip(keys,nums))
    return retu
        
my_dict={'a':1000,'b':20123,'c':1000,'d':20123,'e':1000,'f':20123,'g':1000,'h':20123,'i':1000,'j':20123,'k':106,'l':123}

print(my_dict)
listofkeys=list(my_dict.keys())
listofvalues=list(my_dict.values())
dict2=bubble_sort(listofvalues,listofkeys)
print(dict2)