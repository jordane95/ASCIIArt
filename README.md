# ASCIIArt
Converting an RGB signboard image to its ASCII encoding within 140 characters.

The whole pipeline is mainly composed of 3 modules, edge detection, ocr and ascii matching. For more detail, please read the documentation in each folder.

## Example

Here is an example of our system.

This is the input image, downloaded from [Internet](https://www.psyangji.com/15209.html)

![input](images/input.jpg)

After processed by the 3 modules, we can get the final ASCII encoding result:

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

# Usage

1. run pip install -r requirements.txt
2. put your image in /images/folder
3. sh run.sh
4. your results will be saved in the /results/ folder

## Structure

```
ASCIIArt
├── edge                                    // Edge detection 
│   ├── hed.py                              // Holistically-Nested Edge Detection
│   ├── canny.py                            // Canny
│   ├── README.md                           // Documentation of the edge detection module
│   ...
├── ocr                                     // OCR module
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

* Optimization

