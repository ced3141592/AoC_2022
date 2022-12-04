
def range_to_set(rnge :str):
    
    rnge = rnge.split('-')
    lower = int(rnge[0])
    upper = int(rnge[1])
    range_set = set()
    for i in range(upper-lower+1):
        range_set.add(lower+i)
    return range_set

def fully_contains(r1, r2):
    r1 :set = range_to_set(r1) 
    r2 :set = range_to_set(r2) 

    # return r1.issubset(r2) or r2.issubset(r1)   # Task 1
    return len(r1.intersection(r2)) > 0           # Task 2

with open('input.txt') as cleaning_list:

    count = 0
    for pair in cleaning_list.readlines():
        rnge = pair.split(',')
        if fully_contains(rnge[0], rnge[1]):
            count += 1
    
    print(count)
cleaning_list.close()