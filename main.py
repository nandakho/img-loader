import sys
import argparse
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

parser  = argparse.ArgumentParser(description="Open image file as transparent overlay")
parser.add_argument('image_name', type=str, help="Accept String as target's file name (Required!)")
parser.add_argument('-o','--opacity', type=int, help="Accept Integer as percentage of desired opacity value (Optional, Default: 50)", default=50)
parser.add_argument('-w','--windowed', type=bool, action=argparse.BooleanOptionalAction, help="Show image with window/draggable (False) (Optional, Default: False)")
parser.add_argument('-t','--top', type=bool, action=argparse.BooleanOptionalAction, help="Stay on top (True) or not (False) (Optional, Default: False)")
args = parser.parse_args()
opacity = float(args.opacity/100)
if opacity>1:
    opacity=1
if opacity<0:
    opacity=0
app = QApplication(sys.argv)
window = QMainWindow()
window.setAttribute(Qt.WA_TranslucentBackground, True)
window.setAttribute(Qt.WA_NoSystemBackground, True)
if args.windowed==True:
    if args.top==True:
        window.setWindowFlags(Qt.WindowStaysOnTopHint)
else:
    window.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    if args.top==True:
        window.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
    else:
        window.setWindowFlags(Qt.FramelessWindowHint)
window.setWindowOpacity(opacity)
label = QLabel(window)
pixmap = QPixmap(args.image_name)
label.setPixmap(pixmap)
label.setGeometry(0, 0, pixmap.width(), pixmap.height())
window.label = label
window.resize(pixmap.width(),pixmap.height())
window.show()
sys.exit(app.exec_())