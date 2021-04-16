from random import randint
answers = ('да', 'нет', 'это сложный вопрос, я не знаю ответа')
question = ""
while question != "стоп":
    print('Введите Ваш вопрос. Если Вы хотите завершить общение, то введите "стоп"')
    question = str(input())
    answer = answers[randint(0,len(answers)-1)]
    if question == "стоп":
        break
    print(answer)
