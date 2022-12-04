
def get_item_priority(item):
    value = ord(item)
    # a-z -> 1 - 26 and A - Z 27 - 52
    if value > 96 and value < 123:
        return value - 96
    else:
        return value - 38


with open('input.txt') as rucksacks:

    # task 1
    sum_priorities = 0

    #task 2
    sum_priorities_group = 0
    count = 0
    group = set()


    for rucksack in rucksacks:
        rucksack = rucksack[:-1] # chop off \n

        # Task 1
        if len(rucksack) % 2 == 0:
            comp1, comp2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
            same_item = set(comp1).intersection(set(comp2))
            if len(same_item) == 1:
                for item in same_item:
                    sum_priorities += get_item_priority(item)
            else:
                raise Exception("More than one same item per compartment")
        else:
            raise Exception("uneven rucksack length")

        # Task 2
        if len(group) == 0:
            group.update(set(rucksack))
        else:
            group = group.intersection(set(rucksack))
        count += 1
        if count % 3 == 0:
            if len(group) == 1:
                sum_priorities_group += get_item_priority(list(group)[0])
                group.clear()
            else:
                raise Exception("More than one same item per compartment")



    print(sum_priorities)
    print(sum_priorities_group)


rucksacks.close()