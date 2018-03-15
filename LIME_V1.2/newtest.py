from PIL import Image, ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance
im = Image.open("img/inp_4.jpg")

im1 = im.filter(ImageFilter.BLUR)

im2 = im.filter(ImageFilter.MinFilter(3))
im3 = im.filter(ImageFilter.MinFilter)
im4 = im.filter(ImageFilter.SMOOTH_MORE)

enhancer = ImageEnhance.Contrast(im)
for i in range(8):
    factor = i / 4.0
    enhancer.enhance(factor).show("Contrast %f" % factor)

#im5.show()
