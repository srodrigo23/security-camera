import cv2

def resize(image, 
           width=None, 
           height=None, 
           inter=cv2.INTER_AREA):
    
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized