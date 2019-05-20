from PIL import Image
import math

'''
This function applies a mask upon data. The result of this operation is returned. The only condition is that the mask and the data list must be the same size. If this is not the situation, this function will raise an error.
Parameters:
    data: list with data points
    mask: list with mask values
Return
    result of the mask on the data as an integer
'''
def applyMask(data: list, mask: list) -> int:
    if (len(data) != len(mask)):
        raise Exception("Data list and mask are not the same size!")

    result = 0

    for index_x in range(len(data)):

        if (len(data[index_x]) != len(mask[index_x])):
            raise Exception("Data list and mask are not the same size!")

        for index_y in range(len(data[index_x])):
            result = result + (data[index_x][index_y] * mask[index_x][index_y])

    return result

'''
This image will return a new image that is the gray-scale version of the original image that is passed to this function.
Parameters:
    original: Pillow Image, converted to RGB (  img.convert('RGB')  )
Return:
    gray-scale image
'''
def image_rgb_2_gray(original: Image) -> Image:
    img_width, img_height = original.size
    gray_image = Image.new('L', (img_width, img_height), 0)

    for x in range(img_width):
        for y in range(img_height):
            color_r, color_g, color_b = original.getpixel((x, y))
            gray_scale = (int)((0.3 * color_r) + (0.59 * color_g) + (0.11 * color_b))

            gray_image.putpixel((x, y), gray_scale)

    return gray_image

def image_edge_detection(original: Image) -> Image:
    #get image size
    img_width, img_height = original.size

    #create empty image
    edge_detected_image = Image.new('L', (img_width, img_height), 0)

    #declare filters
    mask_horizontal_edges = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    mask_vertical_edges = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    edge_buffer_size = (int) (math.floor(len(mask_horizontal_edges) / 2))

    #loop through each pixel, pass edge
    for x in range(edge_buffer_size, img_width-edge_buffer_size):
        for y in range(edge_buffer_size, img_height-edge_buffer_size):
            #get old pixels
            old_values = []
            for get_old_x_index in range(len(mask_horizontal_edges)):
                old_values.append([])
                for get_old_y_index in range(len(mask_horizontal_edges)):
                    old_values[get_old_x_index].append(original.getpixel((x - edge_buffer_size + get_old_x_index, y - edge_buffer_size + get_old_y_index)))

            #apply x filter
            result_horizontal_mask = applyMask(old_values, mask_horizontal_edges)
            #apply y filter
            result_vertical_mask = applyMask(old_values, mask_vertical_edges)

            #average filter results
            average_result = (int) (math.sqrt(result_horizontal_mask*result_horizontal_mask + result_vertical_mask*result_vertical_mask)) #https://en.wikipedia.org/wiki/Sobel_operator  <-- this explains the square root on the sum of the squares. They do it here in the pseudocode, that might give better results

            #set pixel value
            edge_detected_image.putpixel((x, y), average_result)

    #return result
    return edge_detected_image
