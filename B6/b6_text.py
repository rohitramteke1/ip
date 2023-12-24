#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('Rock.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "The Rock"

font = ImageFont.truetype('arial.ttf', 32)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save('watermarked_rock.jpg')
