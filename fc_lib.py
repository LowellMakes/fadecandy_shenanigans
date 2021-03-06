import cv2

def chunks(l, n):
    #split array l into n equal size chunks.
    #assumes len(l) is a multiple of n
    for i in xrange(0, len(l), n):
      yield l[i:i+n]

def fix_array(a):
    #modify the array to fit our display, which has alternating
    #rows of 32 pixels
    c = chunks(a, 32)
    flip = False
    rebuilt = []
    for chunk in c:
        if flip:
            rebuilt.append(chunk[::-1])
        else:
            rebuilt.append(chunk)
        flip = not flip
    rebuilt = [item for sublist in rebuilt for item in sublist]
    return rebuilt


def read_image_to_array(path):
    #Read image
    im = cv2.imread(path)
    return opencv_image_to_array(im)

def opencv_image_to_array(im):
    #fix color, opencv uses bgr, we want rgb
    rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    #resize image to our display size
    out = cv2.resize(rgb, (32,25)).tolist()
    #flatten image to a 1d array
    flat =  [item for sublist in out for item in sublist]
    #map the image array to our display, which has alternating rows
    array = fix_array(flat)
    return array

