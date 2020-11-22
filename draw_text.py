from PIL import Image, ImageFont, ImageDraw

img = Image.open("img001.jpeg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Animesh Mohan",(255,255,255),font=font)
img.save('img001.jpeg')
