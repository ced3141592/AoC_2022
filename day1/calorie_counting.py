f = open("input.txt")

chunk :int = 0
comp :int = 0

for cal in f.readlines():
    try:
        chunk += int(cal)
    except ValueError as e:
        if chunk > comp:
            comp = chunk
            chunk = 0
        else:
            chunk = 0
    except Exception as e:
        print(e)

if chunk > comp:
    comp = chunk

print(comp)

f.close()