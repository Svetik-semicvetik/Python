def compare(S1,S2):
    ngrams = [
        S1[i:i+3] for i in range(len(S1))
    ]
    count = 0 
    for ngram in ngrams:
        count += S2.count(ngram)
    return count/max(len(S1), len(S2))
    
from random import randint
answers = ('да', 'нет', 'это сложный вопрос, я не знаю ответа')
question = ""
while question != "стоп":
    print('Введите Ваш вопрос. Если Вы хотите завершить общение, то введите "стоп"')
    question = str(input())
    answer = answers[randint(0,len(answers)-1)]
    if compare('стоп', question) > 0.7:
        break
    print(answer)