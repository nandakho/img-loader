# Description
Simple Python app to load image as an overlay, opacity and some other options can be set.  
Now with GUI..  

## Options
`-h` Show helps  
`-i IMAGE_NAME` Automatically load [IMAGE_NAME] as file path string to GUI Menu, and is now an optional argument  
`-o OPACITY | --opacity OPACITY` Set image opacity, [OPACITY] is Integer within 0 to 100, default value is 50  
`-w | --windowed | --no-windowed` Display window or not, default is not displayed (--no-windowed)  
`-t | --top | --no-top` Stay on top, default does not stay on top (--no-top)  
`-m MAX_RATIO | --max-ratio MAX_RATIO` Set maximum ratio between screen's and image's resolution while maintaining aspect ratio, [MAX_RATIO] is Integer within 0 to 100, default value is 80  
```
MAX_RATIO Note:
MAX_RATIO is only used when loading an image larger than screen's resolution times the ratio.  
You can set it to 100, and the largest of either image's width or image's height will fit to your screen's and the other dimension will adjust according to it's original aspect ratio.  

Example 1:  
MAX_RATIO: 80  
Screen Resolution: 1920*1080
Image Loaded: 1280*720  
Displayed Image Resolution: 1280*720  
Nothing changed, image displayed on full resolution, because 1280 and 720 is still below (1920 * 0.8 = 1536) and (1080 * 0.8 = 864)
  
Example 2:  
MAX_RATIO: 50  
Screen Resolution: 1920*1080  
Image Loaded: 1440*1440  
Displayed Image Resolution: 540*540  
Image is displayed on 540*540, which is the smallest of (1920 * 0.5 = 960) or (1080 * 0.5 = 540)  

Example 3:  
MAX_RATIO: 30  
Screen Resolution: 1366*768  
Image Loaded: 2880*1440  
Displayed Image Resolution: 408*204  
Image is displayed on (408*204), this is based on screen's width ratio (1366 * 0.3 = 409.8) and screen's height ratio (768 * 0.3 = 230.4)  
Converting both values to integer with original image aspect ratio (2:1) in mind, we got (408*230)  
And if we take the width (408) it's height will become (204) based on original aspect ratio (2:1)  
Meanwhile if we take the height (230) then it's width will become (460)  
Since (408*204) is smaller than (230*460) then it's selected  

```

## Usage
With .py script:  
`path\to\python-executable main.py [-h] [-i IMAGE_NAME] [-o | --opacity OPACITY] [-w | --windowed | --no-windowed] [-t | --top | --no-top] [-m | --max-ratio MAX_RATIO]`  
or with binary:  
`main.exe [-h] [-i IMAGE_NAME] [-o | --opacity OPACITY] [-w | --windowed | --no-windowed] [-t | --top | --no-top] [-m | --max-ratio MAX_RATIO]`  
  
Example with binary:
```
main.exe -h                         #Show helps
main.exe -i image.jpg               #Open image.jpg with all default options (50% opacity, window-less, not draggable, and does not stay on top)  
main.exe -o 10 -w -t -i image.jpg   #Open image.jpg with 10% opacity, windowed, draggable, and stay on top  
```

## Lib Used
PyQt6 - `pip install PyQt6`  
argparse - `pip install argparse` (If not included with standard library)  
pyinstaller - `pip install pyinstaller`

## Build
- Build with pyinstaller: `pyinstaller img-loader.spec`  
Binary output in generated `dist` folder  
- Or download prebuilt one in [release](https://github.com/nandakho/img-loader/releases)