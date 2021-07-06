# ASCIIArt
Converting an RGB signboard image to its ASCII encoding within 140 characters

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