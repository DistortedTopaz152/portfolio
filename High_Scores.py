#Dyson Smith Sept 17-2020
#High Scorse
name1 = 'Topaz'
name2 = 'Opal'
name3 = 'Quartz'#jem stone nameing skeam
name4 = 'Ruby'
name5 = 'Amber'
name6 = 'Onix'
name7 = 'Emerald'
name8 = 'Saphire'
name9 = 'Aquamarien'
name10 = 'Diamond'

#some scorse may repet becuse of ties
score1 = 17050
score2 = 16500
score3 = 15050
score4 = 14950
score5 = 13750
score6 = 12500#reapeats
score7 = 11750
score8 = 10000#reapeats

line = '-------------------------'

print(' ________________')
print('|      High Scores       |')
print(str.format('|{0}{2:5.10}{1:d}|',name1,score1,line))
print(str.format('|{0}{2:5.12}{1:d}|',name2,score2,line))
print(str.format('|{0}{2:5.9}{1:d}|',name3,score3,line))
print(str.format('|{0}{2:5.12}{1:d}|',name4,score4,line))
print(str.format('|{0}{2:5.10}{1:d}|',name5,score5,line))
print(str.format('|{0}{2:5.12}{1:d}|',name6,score6,line))
