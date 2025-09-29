s = input().strip()

patterns = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for i in patterns:
    s = s.replace(i, '!') 

print(len(s))