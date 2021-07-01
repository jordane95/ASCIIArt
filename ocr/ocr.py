from paddleocr import PaddleOCR, draw_ocr
from utils import get_bounds 
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

image_array = np.array(image)
H, W, channel = image_array.shape
x_min, x_max, y_min, y_max = get_bounds(boxes, W, H)
sliced_array = image_array[y_min:y_max, x_min:x_max, :]
roi = Image.fromarray(sliced_array.astype('uint8')).convert('RGB')
roi.save('images/roi.jpg')



