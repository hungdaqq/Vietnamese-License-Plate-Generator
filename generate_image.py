from PIL import Image, ImageFont, ImageDraw
import numpy as np 
import random

def generate_1lines_image(template, bg = 'background/bg1.jpg'):
	
	random_value = random.random() # random number in range [0.0,1.0)
	if random_value < 0.5:
		font = ImageFont.truetype("MyFont-Regular_ver3.otf", 126)
	else:
		font = ImageFont.truetype("UKNUMBER2.ttf", 120)

	if type(bg).__name__ == 'str':
		im = Image.open(bg)
	else:
		im = bg
	# if len(template.replace('-', '').replace('.', '')) > 7:
	im = im.resize((640, 150))
	# else:
	# 	im = im.resize((640, 120))
	width, height = im.size
	draw = ImageDraw.Draw(im)
	textsize = font.getsize(template)
	textX = int((width - textsize[0]) / 2)
	textY = int((height - textsize[1]) / 2)
	fill = tuple(np.random.randint(20, size=3))
	draw.text((textX, textY), template, font=font, fill=fill)
	return im, textsize

def generate_2lines_images(template, bg = 'background/bg2.jpg', margin = 10, size = (640, 500)):
	random_value = random.random() # random number in range [0.0,1.0)
	if random_value < 0.5:
		font = ImageFont.truetype("MyFont-Regular_ver3.otf", 196)
		size = (640,500)
	else:
		font = ImageFont.truetype("UKNUMBER2.ttf", 180)
		size = (640,400)
	random_value = random.random()
	if type(bg).__name__ == 'str':
		im = Image.open(bg)
	else:
		im = bg
	im = Image.open(bg)
	im = im.resize(size)
	width, height = im.size
	draw = ImageDraw.Draw(im)
	line_1, line_2 = template.split('/')

	textsize1 = font.getsize(line_1)
	textX1 = int((width - textsize1[0]) / 2)
	textY1 = int((height/2 - textsize1[1]) / 2) + margin
	textsize2 = font.getsize(line_2)
	textX2 = int((width - textsize2[0]) / 2)
	textY2 = int(height/2 + (height/2 - textsize2[1]) / 2) - margin/2
	fill = tuple(np.random.randint(20, size=3))
	
	shadow = tuple(np.random.randint(200, 255, size=3))
	direction = tuple(np.random.randint(-3, 3, size=2))

	# Add drop shadow line 1
	draw.text((textX1 + direction[0], textY1 + direction[1]), line_1, font=font, fill=shadow)
	draw.text((textX1, textY1), line_1, font=font, fill=fill)
	
	# Add drop shadow line 2
	draw.text((textX2 + direction[0], textY2 + direction[1]), line_2, font=font, fill=shadow)
	draw.text((textX2, textY2), line_2, font=font, fill=fill)

	return im, (textsize1, textsize2)