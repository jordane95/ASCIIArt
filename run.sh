#!/bin/sh

# edge detection
echo "Performing edge detection..."
cd edge
python3 canny.py
python3 hed.py
echo "Edge detection finished"

# ocr
echo "Performing OCR..."
cd ../ocr
python3 ocr.py
echo "OCR finished"

# ascii matching
echo "Performing ASCII matching..."
cd ../ascii
python3 search.py
echo "ASCII matching finished"

