import cv2

def showing_image(imread, name='Showing Image'):
    cv2.imshow(name, imread)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return "A new tab was opened showing the desired image. Press any button to close it."
