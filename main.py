from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
print("Список картинок: ")
print("1.кот в очках")
print("2.Кот в ресторане")

user_answer = int(input("Выберите картинку цифрой "))

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")


if user_answer == 1:
    image_file = "Кот в очках.png"
elif user_answer == 2:
    image_file = "Кот в ресторане.png"

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0,0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0,0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 20), bottom_text, font=font, fill="black")

# draw.text((0,100), bottom_text, font=font, fill="black")

image.save("new_meme.jpg")