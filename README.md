# Description
Simple Python app to load image as an overlay, opacity and some other options can be set.

## Options
`-h` Show helps
`-o OPACITY | --opacity OPACITY` Set image opacity, [OPACITY] is Integer within 0 to 100, default value is 50
`-w | --windowed | --no-windowed` Display window or not, default is not displayed (--no-windowed)
`-t | --top | --no-top` Stay on top, default does not stay on top (--no-top)
`image_name` Image to be loaded, use relative or full path without space

## Usage
With .py script:  
`path\to\python-executable main.py [-h] [-o OPACITY] [-w | --windowed | --no-windowed] [-t | --top | --no-top] image_name`  
or with binary:  
`main.exe [-h] [-o OPACITY] [-w | --windowed | --no-windowed] [-t | --top | --no-top] image_name`  
  
Example with binary:
```
main.exe -h #Show helps
main.exe image.jpg  #Open image.jpg with all default options (50% opacity, window-less, not draggable, and does not stay on top)  
main.exe -o 10 -w -t image.jpg  #Open image.jpg with 10% opacity, windowed, draggable, and stay on top  
```

## Lib Used
PyQt5 - `pip install PyQt5`
argparse - `pip install argparse` (If not included with standard library)

## Build
- Build with pyinstaller: 
- Or download in [release]()