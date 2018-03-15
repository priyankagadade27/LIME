import Image
import ImageEnhance

brightness = 2.0
peak = Image.open( "img/inp_5.jpg")
enhancer = ImageEnhance.Brightness(peak)
bright = enhancer.enhance(brightness)
bright.save( "new_output.jpg")
bright.show()

contrast = 1.3
enhancer = ImageEnhance.Contrast(bright)
con = enhancer.enhance(contrast)
con.save( "new_output1.jpg")
con.show()