from PIL import Image,ImageFilter

#Изменение размера изображения
size = (100, 100)
original = Image.open('img.jpg')
original.thumbnail(size)
original.save('2.jpg')
original.show()

#Размытие картинки
img = original.filter(ImageFilter.BLUR)
img.show()

