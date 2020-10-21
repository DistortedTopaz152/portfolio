#Dyson Smith
#Oct. 5-2020
#lists
import random
top_games = [# if its () insted of [] it becomes unchangable A.K.A a Tupple
    'mysterye dungen rescue red',#0   |  least to favorite
    'pokemon sword',
    'mario maker2',
    'xenoblade chronicles x',
    'warframe',
    'halo master chief collection',
    'super hot',
    'minecraft',
    'breath of the wild',
    'pokemon sun',
    'subnotica',
    'mario&luigi dream team',
    'forager',
    'smash bros ultimate',
    'enter the gungeon',
    'notia',
    'terraria modes',
    'borderlands2',
    'pokemon randomizers',
    'borderlands3',
    'terraria',
    'pokemon X&Y',
    'pokemon emerald',
    'hollow knight',
    'pokemon platnum'#24
    ]

##high_scores = [443,950,1000,410,875,600,550,500,395,380]

##print(top_games)
##print(len(top_games))
##
##print(max(high_scores))
##print(max(top_games))
##
##print(max(high_scores))
##print(max(top_games))

top_games.append('world of warcraft')
top_games.sort()
top_games.reverse()
top_games.insert(0,'Zelda link to the past')
top_games.insert(6,'Zelda link to the past')
##print(top_games.count('Zelda link to the past'))
num = top_games.index('Zelda link to the past',True)
game = top_games.pop(int(num))
##print(game)
newlist = top_games.copy()
top_games.clear()
##print(top_games)
print(newlist)


points = 0
if len(newlist) >= 25:
    points+=25
else:
    points-=25

if not top_games:
    points+=10
else:
    points-=10

if 'world of warcraft' in newlist:
    points+=10
else:
    points-=10

if newlist.count('Zelda link to the past') > 1:
    points-=5
else:
    points+=5

if newlist.index('Zelda link to the past') == 0:
    points+=25
else:
    points-=25

if newlist.count('world of warcraft') > 1:
    points+=25
else:
    points-=25

for i in newlist:
    if 'pokemon' in i or 'Pokemon' in i:
        points-=100
    if 'halo'in i or 'Halo' in i:
        points-=100
    if 'fortnite' in i or 'Fortnite' in i:
        points-=100000000000
    if 'smash' in i:
        points-=50

if points >= 90:
    print('A')
elif points <=89 and points >= 71:
    print('B')
elif points <=70 and points >= 61:
    print('C')
elif points <= 60 and points > 50:
    print('D')
else:
    print('F')

print(points)

##print(top_games.count('Zelda link to the past'))
##top_games.remove('Zelda link to the past')
##print(top_games.count('Zelda link to the past'))

##print(top_games)

##numbers = []
##x=0
##while x != 100:
##    numbers.append(random.randint(1000,10000))
##    x+=1
##print(numbers)
##numbers.sort()
##print(numbers)

##x=0
##while x != len(high_scores):
##    print('looping',x)
##    high_scores [x]+=1000
##    x+=1
##print(high_scores)
##y=0
##while True:
##    print(y)
##    y+=1
##    if y >10000000:
##        break
