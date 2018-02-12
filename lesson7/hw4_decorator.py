def decor(func):
    print('Создаем декоратор...')
    def wrapper():
        print('Запускаем функцию')
        func()
        print('Окончили функцию')
    return wrapper

@decor
def func():
    print("Сама функция")

func()
func()
