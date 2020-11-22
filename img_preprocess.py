from PIL import Image, ImageFont, ImageDraw

def img_preprocess(img_path, text):
    img = Image.open(img_path)
    #resize image
    basewidth = 300
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    #Draw text on image
    width, height = img.size
    x, y = width/2 - len(text), height-15
    fillcolor = "white"
    shadowcolor = "black"
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font  =  ImageFont.truetype ( "arial.ttf", 16 )
    # font = ImageFont.load_default()
    # draw.text((x, y),"Sample Text",(r,g,b))
    # draw.text((width/2 - len(text)/2, height-15),text,(255,255,255),font=font)
    # thin border
    draw.text((x-1, y), text, font=font, fill=shadowcolor)
    draw.text((x+1, y), text, font=font, fill=shadowcolor)
    draw.text((x, y-1), text, font=font, fill=shadowcolor)
    draw.text((x, y+1), text, font=font, fill=shadowcolor)

    draw.text((x, y), text, font=font, fill=fillcolor)

    img.save(img_path)
