import requests
# GET  Получаем картинку с сайта и записываем в файл
img_url = 'https://i.ytimg.com/vi/lDvB4uPFEbU/maxresdefault.jpg'
response = requests.get(img_url)
with open('img.jpg', 'wb') as file:
    file.write(response.content)
# POST
data_response = requests.post('https://httpbin.org/post', data={'foo': 'bar'})
print(data_response.text)  # переданные данные находятся по ключу form

