i = 2
while i <= 9:
    j = 2
    while j <= 9:
        print(f"{i:d} * {j:d} = {i*j:d}", end="\t" if j < 9 else "\n")
        j += 1
    i += 1
