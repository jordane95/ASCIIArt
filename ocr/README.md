# OCR Module

The optical character recognition (OCR) aims at detecting and recognizing text in image of real scenarios. This part is heavily dependent on the [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) model open sourced by Baidu. For more detail, please refer to the original [paper](https://github.com/PaddlePaddle/PaddleOCR).

## Environment Requirement

* Python3
* PandlePandle

You can click [here](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/multi_languages_en.md) for more detail.

We recommend to use *conda* for environment management. You can install it on its official [site](https://www.anaconda.com/products/individual#Downloads).

1. Creat environment

   You can choose to create your own environment for this specific application. If you want to run it directly in the *base* environment, please skip to step 2.

   ```bash
   # create a new environment
   conda create -n your_env
   # activate your new environment
   conda activate your_env
   ```

2. Install packages

   In the environment just created, you can install the required packages using the following instructions in the shell/cmd.

   ```bash
   # paddle installation
   pip3 install paddlepaddle
   
   # paddleocr package installation
   pip3 install paddleocr==2.0.6
   ```

3. Check installation

   You can check the installing results via the following commands.

   ```bash
   # enter into the python command line mode
   % python3
   ```

   Normally, you should be in the python environment, inpliciting the Python version number in the terminal. In the interactive Python environment, input the following code.

   ```python
   >>> import paddleocr
   ```

   If there is no error raised, then you have configured the environment correctly.

## Usage

The code for OCR is written in Python script ocr.py.

```python
from paddleocr import PaddleOCR, draw_ocr

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
im_show.save('result.jpg')
```

You can run this code via

```bash
% python3 ocr.py
```

 The detected text will be shown in the command line

```bash
[2021/07/01 11:29:13] root INFO: dt_boxes num : 1, elapse : 0.4738023281097412
[2021/07/01 11:29:13] root INFO: rec_res num  : 1, elapse : 0.016218900680541992
[[[288.0, 268.0], [491.0, 268.0], [491.0, 305.0], [288.0, 305.0]], ('PSYANGJI.COM', 0.97459394)]
```

The last line includes the text recognized.

You can also check the visualization result by entering

```bash
open images/result.jpg
```

You will see the resulting image like this, with a red box entouring the text detected.

![result](images/result.jpg)

For comparasion convenience, the input image is like this

![input](images/input.jpg)

Based on the result of text detection, we extend the text enclosing text box according to the image size and text lenght. We can extract the region of interest (ROI), and get the following result. The function is implemented in utils.py

![roi](images/roi.jpg)

Note: The PaddleOCR utilize the CRNN for text recognition, thus it can only recognize *single* line text.

## References

1. https://github.com/PaddlePaddle/PaddleOCR
2. Du Y, Li C, Guo R, et al. PP-OCR: A practical ultra lightweight OCR system[J]. arXiv preprint arXiv:2009.09941, 2020.

