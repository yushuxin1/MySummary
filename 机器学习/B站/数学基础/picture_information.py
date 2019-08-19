import numpy as np
from PIL import Image
import cv2

# image = cv2.imread('1.jpg')
# print(image)
# print(type(image))
# print(image.shape)

# a = Image.open('1.jpg')
# print(a)
# b = np.array(a)
# print(b)
# print(type(b))

if __name__ == '__main__':
    image_file = '2.jpg'
    height = 100

    img = Image.open(image_file)
    img_width, img_height = img.size
    # 给定比例获得字符的宽高
    width = int(1.8 * height * img_width // img_height)
    # 根据字符的宽高对原始图像进行拉伸得到新的图像
    img = img.resize((width, height), Image.ANTIALIAS)
    # 把新的图像转成灰度图
    pixels = np.array(img.convert('L'))
    print('type(pixels) = ', type(pixels))
    print(pixels.shape)
    print(pixels)
    chars = "MNHQ$OC?7>!:-;. "
    N = len(chars)
    step = 256 // N
    print(N)
    result = ""
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j] // step]
        result += '\n'
    with open('text.txt', mode='w') as f:
        f.write(result)