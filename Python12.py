'''
Name: Rohit Nachaloor
Date: 02/21/2019
Assignment No. 12
Period: 1
Cowart
'''
def mycode():

    #Correct Answer List
    correct = []

    #Question 1
    print('What is the capital of the Netherlands')
    print('a. Paris b. Rotterdam c. Dutch d. Amsterdam')
    ans1 = input()
    score = 0
    if (ans1 == 'd'):
        print('Correct!!!')
        correct.append('1. Amsterdam')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is Amsterdam.')

    #Question 2    
    print('What is the capital of India')
    print('a. Dhaka b. New Delhi c. Mumbai d. Islamabad')
    ans1 = input()
    if (ans1 == 'b'):
        print('Correct!!!')
        correct.append('2. New Delhi')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is New Delhi.')

    #Question 3
    print('What is the capital of Poland')
    print('a. Berlin b. Chechnya c. Warsaw d. Moscow')
    ans1 = input()
    if (ans1 == 'c'):
        print('Correct!!!')
        correct.append('3. Warsaw')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is Warsaw.')    

    #Question 4
    print('What is the capital of Bangladesh')
    print('a. Dhaka b. Riyadh c. New Delhi d. Malé')
    ans1 = input()
    if (ans1 == 'a'):
        print('Correct!!!')
        correct.append('4. Dhaka')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is Dhaka.')

    #Question 5
    print('What is the capital of Sudan')
    print('a. Algiers b. Khartoum c. Juba d. Pretoria')
    ans1 = input()
    if (ans1 == 'b'):
        print('Correct!!!')
        correct.append('5. Khartoum')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is Khartoum.')

    #Question 6
    print('What is the capital of Uzbekistan')
    print('a. Astana b. Bishkek c. Dushanbe d. Tashkent')
    ans1 = input()
    if (ans1 == 'd'):
        print('Correct!!!')
        correct.append('6. Tashkent')
        score = score + 1
    else:
        print('Sorry. You are wrong. The correct answer is Tashkent.')

    #Condition for final message based on amount correct
    if (score > 3):
        print('Congratualions!!! You got '+str(score)+' right.')
    elif (0 < score < 4):
        print('Unfortunatley, you only got '+str(score)+' right.')
    else:
        print('Unfortunatley, you got nothing correct.')
    print('Here is a list of your correct answers.')
    print(correct)

def main():
    mycode()
if(__name__)==("__main__"):
    main()

