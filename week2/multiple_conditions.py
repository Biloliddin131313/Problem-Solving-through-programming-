# Logical OR operator 

print('What type of adventure you want to ?')
type = input()
if (type == 'scary') or (type == 'short'):
    print('Entering the dark forest!')
elif (type == 'safe') or (type == 'long'):
    print('Taking the safe route')
else:
    print('Not sure which route to take !')

#Logical AND operator
print ('What did i hear ?')
voice = input()
print('What did i see ? ')
scene = input()
if (voice == 'grr') and (scene == 'two red eyes'):
    print('There is a scary creature. I should get out of here!')
else:
    print('I am little scared but i will continue !')
    
