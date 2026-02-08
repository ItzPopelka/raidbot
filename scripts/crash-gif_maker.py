from PIL import Image

size = (15000, 15000)
img = Image.new('RGB', size, color='black')

img.save('crash.gif', 'GIF')
print("File is ready. What is bigger? This file or your mom?")