# ASCIIArt
Converting an RGB signboard image to its ASCII encoding within 140 characters.

# Example

Here is one example of our system.

This is the input image, downloaded arbitrarily from [internet](https://www.psyangji.com/15209.html)

![input](edge_detection/images/input.jpg)

The module of edge detection gives us

![hed](edge_detection/images/hed.jpg)

The module de OCR gives us

![ocr](ocr/images/result.jpg)

and the text content in the command line

```bash
[[[288.0, 268.0], [491.0, 268.0], [491.0, 305.0], [288.0, 305.0]], ('PSYANGJI.COM', 0.97459394)]
```

Based on these informations, we can do an image segmentation to get the image patches

![patch](ocr/images/canny_patch.jpg)

The ASCII matching module can find the best matching character for each patch. Combined with the result of OCR, we can get the final ASCII encoding result:

```
  | F       _ ,,, ,,, _   %      P      
  ! L       B| .   .l+@    2'  TC       
  !         F[(     []@    |,   L       
  ]         F|]     |]H    q"  'L       
  ]         L|]     []@    |_  j]       
  | L      ^F``"""""``"M   M==~%8      ,
n [W"""""""""^^     ^^"""""""""^"""""M"C
@ [@         ,`%  PSYANGJI.COM       | m
  ]Q        <~--*                    j p
  'q   E    -,-' TE`==JEP  @'' '` '    P
--;    @ lg>~Wy _,k_ _H@   E    -={    `
. ]    ] HM   ] '' -~,I@   "p ,.1TI  j  
```

## Structure
```
ASCIIArt
├── edge_detection                          // Edge detection module
│   ├── images                              // Images
│   │   ├── input.jpg                       // Input image
│   │   ...
│   ├── models/hed                          // Pretrained models
│   │   ├── hed_pretrained_bsds.caffemodel  // model parameters
│   │   ├── deploy.prototxt                 // model architecture
│   ├── hed.py                              // Holistically-Nested Edge Detection
│   └── canny.py                            // Canny
├── ocr                                     // OCR module
│   ├── images                              // Images
│   │   ├── hed.jpg
│   │   ...
│   ├── ocr.py                              // PaddleOCR
│   ├── utils.py                            // Some useful fonctions
│   └── README.md                           // Documentation of the OCR module
├── theme_color                             // Theme color extraction module
│   ├── images                              // Images
│   │   ├── roi.jpg                         // input
│   │   └── theme_color.png                 // output
│   ├── color.py                            // KMeans color clustering code
│   └── README.md                           // Documentation of the color extraction module
├── ascii                                   // ASCII matching module
│   ├── images                              // Images
│   │   ├── hed.jpg
│   │   ...
│   ├── fonts                               // Fonts
│   │   └── Menlo.ttc                       // Menlo monospace font       
│   ├── results                             // Converting results
│   │   ├── whole.txt                       // ASCII encoding of the whole image
│   │   ├── limit.txt                       // ASCII encoding of the ROI
│   │   ...                  
│   ├── ascii.py                            // Core code
│   ├── metrics.py                          // Different metrics for patch similarity
│   ├── search.py                           // Search of different segmentation configuration
│   └── README.md                           // Documentation of the ASCII matching module
├── README.md                               // Documentation of the whole project
...
```

## TODO

* Modularization

