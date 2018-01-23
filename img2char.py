# -*- coding: utf-8 -*-
# https://www.shiyanlou.com/courses/370/labs/1191/document
# https://zhuanlan.zhihu.com/p/28642264
from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")  
img_path = 'F:\Python\cat.png'
savepath = 'F:\Python\cat.txt'

def rgb2char(r,g,b,alpha = 256):
	if alpha == 0:
		return ''
	length = len(ascii_char)
	# RGB  ---> gray
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	# unit = (256.0 + 1)/length
	unit = (256.0 + 1) / length
	return ascii_char[int(gray/unit)]

def preprocss(img_path, delta = 100):
	img = Image.open(img_path)
	width, height = img.size # height=153,  width = 153
	if width > height:
		max = width
	else:
		max = height
	scale = max / delta
	# ( 20 + ( 0 / 19 ) ) ) / ( 1 / 19 ) <----->( 20 + ( 0 / 19 ) ) ) / 0  integer division error and only in Python 2.x
	# width, height = int (width/scale), int(height/scale)
	img = img.resize((width, height))
	return img

def img2char(img_obj, savepath):
	txt = ''
	width, height = img_obj.size
	for i in range(height):
		line = ''
		for j in range(width):
			line  += rgb2char(*img_obj.getpixel((j, i)))
		txt  = txt + line +  '\n'
	print txt
	with open(savepath, 'w+') as f:
		f.write(txt)

if __name__ == '__main__':
	print 'start to converting the image to char...............'
	img_obj = preprocss(img_path)
	img2char(img_obj, savepath)
	print 'endind to converting the image to char...............'

