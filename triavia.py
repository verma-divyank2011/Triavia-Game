print('Hello, Welcome to trivia')

ans = input('Are you ready to play (yes/no)')
score = 0
total_q = 3
if ans.lower() == 'yes':
    ans = input('1. Whats is the best programing language?= ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
    


    ans = input('2. What is 2 + 8 + 9 - 1= ')
    if ans == '18':
        score += 1
        print('Correct')
    else:
        print('Incorect')



    ans = input('3. Which company(s) laptop is best (hp/dell)?= ')
    if ans.lower() == 'hp':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    print('Thank You for playing, you got ', score, " questions correct.")
    mark = (score/total_q) * 100

    print("Mark: ", Mark)
    
print('Goodbye')
