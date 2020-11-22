from PIL import Image, ImageFont, ImageDraw

def img_preprocess(img_path, text, count):
    try:
        img = Image.open(img_path)
        #resize image
        basewidth = 800
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)

        #Draw text on image
        width, height = img.size
        x, y = width/2, height/2
        fillcolor = "white"
        shadowcolor = "black"
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font  =  ImageFont.truetype ( "arial.ttf", 30 )
        w, h = font.getsize(text)
        draw.rectangle((x, y, x + w, y + h), fill='black')

        w, h = draw.textsize(text)
        draw.text(((width-w)/2,(height-h)/2), text, font=font, fill=fillcolor)

        extention = img_path.split('.')[-1]

        img.save('./Dataset/img/'+str(count)+'.'+extention)
    except Exception as e:
        print('Error in img_preprocessing: ', e)
        pass
