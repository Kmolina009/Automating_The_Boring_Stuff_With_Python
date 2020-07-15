# Magic8Ball
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Yes'
    elif answerNumber == 3:
        return 'mmmm, it\'s a bit hazy. Try again. . .'
    elif answerNumber == 4:
        return 'Ask again later'
    elif answerNumber == 5:
        return 'It is decidely so'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

# Quick notes form this chapter 
# none is a reserved word, basically the null datatype
# 
# sep=',' -> can be used with print statments to punctuate print
print('apple','orange','banana')
# apple orange banana
print('apple','orange','banana', sep=' / ')
# apple / orange / banana