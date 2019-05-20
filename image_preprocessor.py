from PIL import Image

'''
This image will return a new image that is the gray-scale version of the original image that is passed to this function.
Parameters:
    original: Pillow Image, converted to RGB (  img.convert('RGB')  )
Return:
    gray-scale image
'''
def image_rgb_2_gray(original: Image):
    img_width, img_height = original.size
    gray_image = Image.new('L', (img_width, img_height), 0)

    for x in range(img_width):
        for y in range(img_height):
            color_r, color_g, color_b = original.getpixel((x, y))
            gray_scale = (int)((0.3 * color_r) + (0.59 * color_g) + (0.11 * color_b))

            gray_image.putpixel((x, y), gray_scale)

    return gray_image
