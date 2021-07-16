# Theme Color Extraction

Regarding the RGB pixels in the image as 3-dimensional data points, we can do a color clustering to perform the theme color extraction.

## Environment Requirement

* sklearn
* numpy
* matplotlib
* OpenCV

## Usage

The code is implemented in color.py

You can use this program by issuing the following command

```shell
# usage
python color_kmeans.py --image images/roi.jpg --clusters 3
```

where you can replace the image path as you wish, and also the cluster number.

## Example

In our case, we extract the theme colors from an image extracted from the OCR module. 

![roi](images/roi.jpg)

<center>input image</center>

After processed with the program color.py, the result of theme color is

![color](images/theme_color.png)

<center>Theme color of the input image</center>

You can see that the first color, white gray, corresponds to the text, logo and the white window edge above. The black gray corresponds to the background of the signboard. The brown corrsesponds to the brick above and the scene inside the store.

## Reference

1. https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/