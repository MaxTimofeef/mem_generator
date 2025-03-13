print("Генератор мемов запущен!")
print("Список картинок: ")
print("1.кот в ресторане")
print("2.Кот в очках")

user_answer = int(input("Выберите картинку цифрой"))

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")


if user_answer == 1:
    image = "Кот в очках.png"
elif user_answer == 2:
    image = "Кот в ресторане.png"