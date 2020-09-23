#Dyson Smith Sept. 23-2020
#Formating Strings

var = 'something else'# min max |this will cut it of at 10 charecter| will always start at 0
text = str.format('the {0:10.10} sting {1} are {2} formating','12345678910', var,'test2')
#> and < move it to the right/left ^makes in the middle
#if you add numbers then all have to be numberd and if all blanck then {} = amount of things
print(text)
print(str.format('Example "d": {0:15d}',15000)
#if its a d then it just prints as integer if , then puts ,'s in proper place if e scientific noteation
#f is flote and % is percent
