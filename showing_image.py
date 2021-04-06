import cv2

def showing_image(imread, name='Showing Image'):
    cv2.imshow(name, imread)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return "Showing image. Press any button to close it."
