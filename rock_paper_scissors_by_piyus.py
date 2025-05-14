from random import choice

print("------->Welcome to Rock paper scissors<-------")
print("                -> By Piyus                   ")

while True:
    ch=(input('''
Do you want to play ?
1. Yes
2. No
---------------------> '''))
    
    if int(ch) == 1:
        print("There are total 5 rounds")
        y=0
        c=0

        for i in range(1,6):
            print(f'-> Round {i}')
            ur_choice = input('''
Choose option [1/2/3]
1. Rock
2. Paper
3. Scissors
---------------------> ''')
            
            if int(ur_choice ) == 1:
                ur_choice = 'Rock'
                print(f'You choose -> {ur_choice}')
            elif int(ur_choice ) == 2:
                ur_choice = 'Paper'
                print(f'You choose -> {ur_choice}')
            elif int(ur_choice ) == 3:
                ur_choice = 'Scissors'
                print(f'You choose -> {ur_choice}')
            else:
                print('Invalid option ! ! !')
            
            cmp = choice(['Rock','Paper','Scissors'])
            print(f'Computer choose -> {cmp}')
            if ur_choice == cmp:
                print('Its a draw')
            elif (ur_choice == 'Rock' and cmp == 'Scissors' ) or (ur_choice == 'Paper' and cmp == 'Rock' ) or (ur_choice == 'Scissors' and cmp == 'Rock' ):
                y+=1
            elif (ur_choice == 'Rock' and cmp == 'Paper' ) or (ur_choice == 'Paper' and cmp == 'Scissors' ) or (ur_choice == 'Scissors' and cmp == 'Rock' ):
                c+=1
            
        print(f'Your Score {y}')
        print(f'Computer Score {c}')

        if y == c:
            print('Its a draw ! ! !')
        elif y > c:
            print('Yay, you won :-)')
        else:
            print('You lose :-(')

    elif int(ch) == 2:
        break
    else:
        print('Invalid Choice ! ! !')
    