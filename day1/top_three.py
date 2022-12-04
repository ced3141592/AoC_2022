
class Elve:

    def __init__(self, fruits :list):
        self.fruits = fruits


    def get_total_calories(self) -> int:
        total = 0
        for cal in self.fruits:
            total += cal
        return total


f = open("../day1/input.txt")

elve_list :list = []
top3 :list = []
chunk :list = []

for cal in f.readlines():
    try:
        chunk.append(int(cal))
    except ValueError as e:

        elve_list.append(Elve(chunk.copy()))
        chunk.clear()

    except Exception as e:
        print(e)
    

elve_list.append(Elve(chunk.copy()))
chunk.clear()

f.close()

count = 0
for elve in elve_list:
    if count < 3:
        top3.append(elve.get_total_calories())
        top3.sort()
        count += 1
    else:
        cal = elve.get_total_calories()
        if cal > top3[0]:
            top3[0] = cal
            top3.sort()

total_top3 = 0
for i in top3:
    total_top3 += i

print(total_top3)
