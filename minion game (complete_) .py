player = {}
s = 'BANANA' #enter the game word here 
length = len(s) #6

start,end = 0, 1
def counter(start,end):
    counter_1 = start
    counter_2 = end
    i = length + 1 - len(s[start:end]) #i = number of iterations 
    for y in range(i):
        if s[start:end] == s[counter_1:counter_2]:
            if s[start:end] not in player:
                player[s[start:end]] = 1 
            else: 
                player[s[start:end]] += 1 
        counter_1 += 1 
        counter_2 += 1
        
def looper(start,end):
    #while end <= length:
    for x in s:
        counter(start,end)
        start += 1 
        end += 1 
        if s[start:end] in player:
            break

for z in range(length):
    looper(start,end)
    end += 1
#print("player: ", player)
#print("sum: ", sum(player.values()))

consonant = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowel = ['A', 'E','I','O','U']
stuart, kevin = 0,0 
for x in player:
    for y in x: 
        if y in consonant:
            stuart += player[x]
            break
        elif y in vowel:
            kevin += player[x]
            break

if stuart > kevin:
    print(f'Stuart {stuart}')
else:
    print(f'Kevin {kevin}')

