from PIL import Image, ImageFilter

img = Image.open('./Astro.jpg')

# filter_image = img.convert('L')
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img2 = img.filter(ImageFilter.SMOOTH)
# filter_img.save("blur.png", 'png')
# filter_img2.save("smooth.png", 'png')
# filter_image.save("grey.png", 'png')

img.thumbnail((400, 400))
img.save('thumbnail.jpg')
