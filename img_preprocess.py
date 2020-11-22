from PIL import Image, ImageFont, ImageDraw

def img_preprocess(img_path, text):
    img = Image.open(img_path)
    #resize image
    basewidth = 800
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    #Draw text on image
    width, height = img.size
    x, y = width/2 - len(text), height-30
    fillcolor = "white"
    shadowcolor = "black"
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font  =  ImageFont.truetype ( "arial.ttf", 25 )
    # font = ImageFont.load_default()
    # draw.text((x, y),"Sample Text",(r,g,b))
    # draw.text((width/2 - len(text)/2, height-15),text,(255,255,255),font=font)
    # thin border
    # draw.text((x-1, y), text, font=font, fill=shadowcolor)
    # draw.text((x+1, y), text, font=font, fill=shadowcolor)
    # draw.text((x, y-1), text, font=font, fill=shadowcolor)
    # draw.text((x, y+1), text, font=font, fill=shadowcolor)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill='black')

    draw.text((x, y), text, font=font, fill=fillcolor)

    img.save(img_path)
