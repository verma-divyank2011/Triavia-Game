print('Hello, Welcome to trivia')

ans = input('Are you ready to play (yes/no)')
score = 0
total_q = 3
if ans.lower() == 'yes':
    ans = input('1. 29 + 34 x 2 - 11= ')
    if ans.lower() == '86':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
    


    ans = input('2. 2 + 8 + 9 - 1= ')
    if ans == '18':
        score += 1
        print('Correct')
    else:
        print('Incorect')



    ans = input('3. 39 + 28 / 56 x 4= ')
    if ans.lower() == '41':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    print('Thank You for playing, you got ', score, " questions correct.")
    mark = (score/total_q) * 5

    print("Mark: ", Mark)
    
print('Goodbye')
