name = input ('What type of book is this ? ')
print(name)
if name == 'adventure':
    print( "I like adventure books!")
print('Finished reading book!')

action = input('What activity you want to perform ?')
print(action)
if action == ('calculate'):
    print('Performing calculations ...')

else:
    print('Performing activity...')
print('Activity completed !')

direction  = input('Towards which direction should I go (up, down, left or right)?')
print(direction)
if direction == 'up':
    print('I am moving in up direction')
elif direction == 'down':
    print('I am moving in a down direction')
elif direction == 'left':
    print('I am moving in a left direction')
else:print('Iam moving in a right direction')

# type = (input('What type of book is this ? '))
if type == 'adventure':
    print('I like adventure books')
print('Finished reading book !')
user = input('Enter activity:')
if user == 'calculate':
    print('Performing calculations...')
else:
    print('Performing activity!')
print('Activity completed !')
robot = input('Towards which direction should i go:')
if robot == 'up':
    print('I am moving in upward direction !')
elif  robot == 'down':
    
        print('I am moving in downward direction !')
elif robot == 'left':
    
        print('I am moving in left direction !')
elif robot == 'right':
    print('I am moving in right direction !')
print('All done !')
user = int(input('Please enter the whole number :'))
if user % 2 == 0 :
    print('the following number is even !')
elif user % 2 == 1:
    print('The following number is odd ')
first_num = int(input('Please enter the first number:'))
second_num = int(input('Please enter the second number:'))
if first_num < second_num:
    print('The first number is smaller than second number ')
elif first_num > second_number:
    print('The first number is bigger than the second!')
