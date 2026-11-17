import cv2
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

url = 'https://picsum.photos/id/237/200/300'
response = urllib.request.urlopen(url)
img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)


img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Oryginalny obraz')
plt.axis('off')
plt.show()

height, width = img.shape[:2]
img = cv2.resize(img, (width // 2, height // 2))


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


plt.imshow(img, cmap='gray')
plt.title('Obraz po przetworzeniu')
plt.axis('off')
plt.show()


print('Wymiary obrazu:', img.shape)
print('Macierz obrazu (fragment 5x5):')
print(img[:5, :5])


