from paddleocr import PaddleOCR, draw_ocr
from utils import * 
import numpy as np

# Also switch the language by modifying the lang parameter
ocr = PaddleOCR(lang="en") # The model file will be downloaded automatically when executed for the first time
img_path ='images/input.jpg'
result = ocr.ocr(img_path)
# Recognition and detection can be performed separately through parameter control
# result = ocr.ocr(img_path, det=False)  Only perform recognition
# result = ocr.ocr(img_path, rec=False)  Only perform detection
# Print detection frame and recognition result
for line in result:
    print(line)

# Visualization
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes)
im_show = Image.fromarray(im_show)
im_show.save('images/result.jpg')


# ROI extraction
image_array = np.array(image)
H, W, channel = image_array.shape
x_min, x_max, y_min, y_max = get_bounds(boxes, W, H)
sliced_array = image_array[y_min:y_max, x_min:x_max, :]
roi = Image.fromarray(sliced_array.astype('uint8')).convert('RGB')
roi.save('images/roi.jpg')


### Patching part
box = boxes[0]
text = txts[0]
text_len = len(text)
print("text len: ", text_len)

image = cv.imread("images/canny.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# print(image)
# print(image.shape)

Tw, Th, Rw, Rh = segment(image, box, text_len) 

print("Tw: %d, Th: %d" % (Tw, Th))

draw_patch(image, int(box[0][0]-(Rw-text_len)//2*Tw), int(box[0][1]-(Rh-1)//2*Th), Tw, Th, Rw, Rh)
