from PIL import Image
import numpy as np
import time

start = time.time()



path = 'C:/Users/SEDan/Documents/image_mini/image_mini/images/'
picture = str(input('Name of picture file? '))
path = path + picture
img = Image.open(path)

def clone(image,n):
	#takes an image and returns a clone that is made of blocks of the original image
	width, height = img.size 
	#size of blocks is predetermined to be nxn pixels
	pixels = []
	i = 0
	while i < height:
		for l in range(n):
			row = []
			j = 0
			while j < width:
				for k in range(n):
					row.append(img.getpixel((j,i)))
				j += n
			pixels.append(row)
		i += n
	return pixels
	





			

pixels = clone(img,150)


# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('C:/Users/SEDan/Documents/image_mini/image_mini/images/new'+picture)
end = time.time()

total = end-start
print(total)


