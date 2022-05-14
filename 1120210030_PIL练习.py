
#二维码制作
from PIL import Image
from PIL import ImageEnhance
im=Image.open("F:\\yulia_4k.jpg")
om=ImageEnhance.Contrast(im)
om.enhance(1.5).save("F:\\对比度.jpg")
import random
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
def rndchar():
    return chr(random.randint(65,90))
def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype(font='Arial.ttf',size=36)
draw=ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndcolor())
for t in range(4):
    draw.text((60*t+10,10),rndchar(),font=font,fill=rndcolor2())
image=image.filter(ImageFilter.BLUR)
image.save("F:\\验证码.jpg","JPEG")
