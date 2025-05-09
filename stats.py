def word_count(file_contents):
    splitted=file_contents.split()
    num_words= len(splitted)
    return num_words

def word_by_word(file_contents):
    dix=dict()
    file_c=file_contents.lower()
    spl=file_c.split()
    for i in range(97,237):
        dix[chr(i)]=0
    for ch in file_c:
        if 'a' <= ch <= 'z':   # Only letters
            dix[ch] += 1
    
    return dix

def report(my_dict):
    listofkeys=list(my_dict.keys())
    listofvalues=list(my_dict.values())
    dict2=bubble_sort(listofvalues,listofkeys)
    return dict2

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
    return dict(zip(keys,nums))