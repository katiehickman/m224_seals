from os.path import join, dirname, realpath, exists
from PIL import Image, ImageDraw, ImageFont
import numpy
import base64
from io import BytesIO


# hack: image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# hack: formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)

def drawFile(file, img_dict):
    if exists(join(dirname(realpath(__file__)), f"static/design/drawn_images/{img_dict['file']}")):
        print('file exists using drawn')
        return join(dirname(realpath(__file__)), f"static/design/drawn_images/{img_dict['file']}")
    else:
        print('making file')
        new_img = Image.open(join(dirname(realpath(__file__)), file))
        d1 = ImageDraw.Draw(new_img)
        font = ImageFont.truetype(join(dirname(realpath(__file__)), 'static/Roboto-MediumItalic.ttf'), 20)
        d1.text((0, 0), f"{img_dict['label']}", font=font, fill=(255, 0, 0))
        new_img.save(join(dirname(realpath(__file__)), f"static/design/drawn_images/{img_dict['file']}"))
        drawn_file = join(dirname(realpath(__file__)), f"static/design/drawn_images/{img_dict['file']}")
        return drawn_file

# hack: color_data prepares a series of images for data analysis
def image_data(path="static/design/", img_list=None):  # hack: path of static images is defaulted
    if img_list is None:  # hack: color_dict is defined with defaults
        img_list = [
            {'source': "Katie's Phone", 'label': "Katie Hickman", 'file': "katiergb.jpg"},
            {'source': "Shreya's Phone", 'label': "Shreya Ahuja", 'file': "banff.jpg"},
            {'source': "Derek's Phone", 'label': "Derek Bokelman", 'file': "derekrgb.jpeg"},

        ]

    # hack: gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        # to fix static images
        img_dict['path'] = '/' + path
        file = path + img_dict['file']
        print(file)

        img_reference = Image.open(drawFile(file, img_dict))

        # img_reference
        img_data = img_reference.getdata()  # used https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size


        # hack: Conversion of original Image to Base64, a string format that serves HTML nicely
        # img_dict
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])

        # hack: Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []

        # hack: 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # big O notation
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)

        # hack: create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
        img_dict['gray_data'] = []
        for pixel in img_dict['data']:

            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
#  end for loop for pixel
        img_reference.putdata(img_dict['gray_data'])

        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])
        img_dict['base64_GRAY'] = image_formatter(img_reference, img_dict['format'])

        # for grayscale hex/binary numbers
        img_dict['hex_array_GRAY'] = []
        img_dict['binary_array_GRAY'] = []

        # hack: 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        #for gray binary/hex changes
        for pixel in img_dict['gray_data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array_GRAY'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array_GRAY'].append(bin_value)

    return img_list  # list is returned with all the attributes for each image dictionary