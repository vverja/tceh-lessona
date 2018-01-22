from random import randint

statistics = {'correct_answers': 0, 'incorrect_answers': 0, 'total_attempts':0}
while True:
    print('Генерируем новое число')
    some_number = randint(0,9)
    while True:
        statistics['total_attempts'] +=1
        i_number = input("Угадайте число")
        if i_number == 'q':
            break
        elif int(i_number) == some_number:
            print('Верный ответ!!!')
            statistics['correct_answers'] +=1
            break
        else:
            print('Неверный ответ')
            statistics['incorrect_answers'] +=1
    if i_number == 'q':
        break
print('Всего правильных ответов:',statistics['correct_answers'])
print('Неправильных ответов:',statistics['incorrect_answers'])
percent = statistics['correct_answers']/statistics['total_attempts']*100
print('Процент попадания: ', percent)