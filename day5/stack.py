from collections import deque
import re

def get_stack_input():
    stacks = {}
    with open('stack.txt') as f:
        for line in f.readlines():
            for i, char in enumerate(line):
                if char.isalpha():
                    if (i-1) // 4 + 1 in stacks.keys():
                        stacks[(i-1) // 4 + 1].append(char)
                    else:
                        stacks[(i-1) // 4 + 1] = deque([char])
    f.close()
    for k, v in stacks.items():
        v.reverse()
    return stacks
       


'''
This function filters out all numbers from the instructions document in
sequence of their appearance
e.g. move 4 from 9 to 6 -> [4, 9, 6]
@return list of line of instruction [[4, 9, 6], [...], ...]
'''
def get_instructions_input():
    with open('instructions.txt') as instr:
        instructions = [re.findall(r'\d+', line) for line in instr.readlines()]
    instr.close()

    return instructions

def do_instruction(intr :list, stacks: dict):
    num_crates = int(intr[0])
    from_stack = int(intr[1])
    to_stack = int(intr[2])

    for i in range(num_crates):
        stacks[to_stack].append(stacks[from_stack].pop())

def do_instructions_CrateMover9001(intr :list, stacks: dict):
    num_crates = int(intr[0])
    from_stack = int(intr[1])
    to_stack = int(intr[2])

    chunk = [stacks[from_stack].pop() for _ in range(num_crates)][::-1]
    for c in chunk:
        stacks[to_stack].append(c)


def main():

    stacks = get_stack_input()

    for i in get_instructions_input():
        # do_instruction(i, stacks)
        do_instructions_CrateMover9001(i, stacks)
    
    for i in range(len(stacks)):
        print(stacks[i+1].pop(), end='')
    print()

if __name__ == '__main__':
    main()