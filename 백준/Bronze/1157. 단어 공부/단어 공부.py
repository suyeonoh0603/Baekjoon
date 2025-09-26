word = input().strip()
word = word.upper()

result = ""
max_count = 0
rep = False

for letter in set(word) :
    count = word.count(letter)
    
    if count > max_count :
        max_count = count
        result = letter
        rep = False
        
    elif count == max_count :
        rep = True
        
print("?" if rep else result)