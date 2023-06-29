	random_value = random.random() # random number in range [0.0,1.0)
	if random_value < 0.5:
		font = ImageFont.truetype("MyFont-Regular_ver3.otf", 128)
	else:
		font = ImageFont.truetype("UKNUMBER.ttf", 128)