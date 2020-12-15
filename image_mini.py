from PIL import Image
import numpy as np



path = 'C:/Users/SEDan/Documents/image_mini/image_mini/images/image.jpg'
img = Image.open(path)

def clone(image):
	#takes an image and returns a clone that is made of blocks of the original image
	width, height = img.size 
	#size of blocks is predetermined to be 10x10 pixels
	pixels = []
	for i in range(height):
		row = []
		j = 0
		while j < width:
			for k in range(10):
				row.append(img.getpixel((j,i)))
			j += 10
		pixels.append(row)
	print(pixels)





			

clone(img)


# # Convert the pixels into an array using numpy
# array = np.array(pixels, dtype=np.uint8)

# # Use PIL to create an image from the new array of pixels
# new_image = Image.fromarray(array)
# new_image.save('new.png')


