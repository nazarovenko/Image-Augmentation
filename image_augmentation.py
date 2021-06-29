import cv2
import random
import numpy as np
import os


def flipVertical(image):
    # randomly vertically flip per iteration
    flip = random.randint(0, 1)

    if flip == 0:  # 1/2 chancee of flipping
        # 0 is the parameter for vertical flip
        out = cv2.flip(image, flip)
    else:
        out = image

    return out


def grayScale(image):
    
    # converts BGR to grayscale image
    out = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # grayscale to BGR to retain 3 channels
    out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)
    print('image shape is:', out.shape)

    return out


def hueShift(image):
    # convert BGR to HSV and extract HSV values
    out = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(out)

    # generate random value to shift H
    # i found that a reasonable range is from -12 to 12
    shift_h = random.randint(-12, 12)
    h = ((h.astype('int16') + shift_h) % 180).astype('uint8')

    # generate output
    out = cv2.merge([h, s, v])
    out = cv2.cvtColor(out, cv2.COLOR_HSV2BGR)

    return out


def brightness_contrast_shift(image):
    # alpha adjusts 'brightness'
    # i found that a reasonable range is 0.00 to 1.40
    alpha = round(random.uniform(0.90, 1.40), 2)

    # beta adjusts 'contrast'
    # i found that a reasonable range is -30 to 30
    beta = round(random.uniform(-30, 30), 2)

    # apply shifts to output
    out = cv2.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), 0, beta)

    return out


def loopColoured(im, im_dir, im_name, num_augs):
    for i in range(num_augs):
        # apply transformations
        print('Augmentation', i + 1, '/', num_augs)
        out = hueShift(im)
        print('hue shift')
        out = flipVertical(out)
        print('flipped')
        out = brightness_contrast_shift(out)
        print('brightness and contrast shifted')

        # apply desired compression settings
        # lowering the value lowers the image size and quality
        # should not matter too much since Teachable Machine will resize the image
        compression = (int(cv2.IMWRITE_JPEG_QUALITY), 95)

        # creating path and saving augmented image
        filename = im_name + '_coloured_' + str(i + 1) + '.jpg'
        path = os.path.join(im_dir, 'Augmented Images', filename)
        print('saved in', path, '\n')
        cv2.imwrite(path, out, compression)


def loopGray(im, im_dir,  im_name, num_augs):
    for i in range(num_augs):
        # apply transformations
        print('Augmentation', i + 1, '/', num_augs)
        out = grayScale(im)
        print('gray scaled')
        out = flipVertical(out)
        print('flipped')
        out = brightness_contrast_shift(out)
        print('brightness and contrast shifted')

        # apply desired compression settings
        # lowering the value lowers the image size and quality
        # should not matter too much since Teachable Machine will resize the image
        compression = (int(cv2.IMWRITE_JPEG_QUALITY), 95)

        # creating path and saving augmented image
        filename = im_name + '_gray_' + str(i + 1) + '.jpg'
        path = os.path.join(im_dir, 'Augmented Images', filename)
        cv2.imwrite(path, out, compression)
        print('saved in', path, '\n')


def loopProduct(productName, im_dir):
    for filename in os.listdir(im_dir):

        # if filename.startswith(productName):
        if filename != "Augmented Images":
            print('Augmenting', filename)

            # open original image and define compression settings
            im_name = filename[:-4]  # remove .jpg
            im_path = os.path.join(im_dir, filename)
            print('Found', filename, 'in', im_path)
            im = cv2.imread(im_path)
            print(filename, 'opened', '\n')

            # perform loop desired number of times
            loopGray(im, im_dir, im_name, 5)
            loopColoured(im, im_dir, im_name, 5)
            print('----------------------------------------')

        else:
            continue


def loopAll(root_dir):
    for folder in os.listdir(root_dir):
        im_dirs = os.path.join(root_dir, folder)
        productName = folder
        loopProduct(productName, im_dirs)
        print('---------------------------------------------------------------------')

    print('Done All')


