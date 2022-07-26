import sys
import argparse
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6 import uic

def show_img():
    if form.show_img.text()=="Show Image":
        form.show_img.setText("Hide Image")
        imgwindow.show()
    else:
        form.show_img.setText("Show Image")
        imgwindow.hide()

def set_opacity(opacity):
    imgwindow.setWindowOpacity(float(opacity/100))

def get_img():
    fname = QFileDialog.getOpenFileName(None,'Open image','',"Any Image (*.jpg *.jpeg *.png *.gif *.bmp *.jfif *.pjpeg *.pjp *.apng *.avif *.svg *.webp *.ico *.tif *.tiff *.cur)")
    if fname[0]!='':
        set_img(fname[0])

def set_img(img_name):
    form.show_img.setEnabled(True)
    form.img_url.setText(img_name)
    pixmap = QPixmap(img_name)
    label.setPixmap(pixmap)
    label.setGeometry(0, 0, pixmap.width(), pixmap.height())
    imgwindow.label = label
    imgwindow.resize(pixmap.width(),pixmap.height())

def set_top_window(isTop,isWindow):
    if isWindow==True:
        if isTop==True:
            imgwindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
    else:
        imgwindow.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        if isTop==True:
            imgwindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint|Qt.WindowType.FramelessWindowHint)
        else:
            imgwindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

parser = argparse.ArgumentParser(description="Open image file as transparent overlay")
parser.add_argument('-i','--image_name', type=str, help="Accept String as target's file name (Optional)")
parser.add_argument('-o','--opacity', type=int, help="Accept Integer as percentage of desired opacity value (Optional, Default: 50)", default=50)
parser.add_argument('-w','--windowed', type=bool, action=argparse.BooleanOptionalAction, help="Show image with window/draggable (False) (Optional, Default: False)")
parser.add_argument('-t','--top', type=bool, action=argparse.BooleanOptionalAction, help="Stay on top (True) or not (False) (Optional, Default: False)")
args = parser.parse_args()
app = QApplication(sys.argv)
app.setStyle('Fusion')
Form, Window = uic.loadUiType("main-menu.ui")
mainmenu = Window()
imgwindow = QWidget()
imgwindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
imgwindow.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
set_top_window(args.windowed,args.top)
label = QLabel(imgwindow)
if args.image_name:
    set_img(args.image_name)
form = Form()
form.setupUi(mainmenu)
form.show_img.clicked.connect(show_img)
form.opacity_slider.valueChanged.connect(set_opacity)
if args.opacity:
    form.opacity_slider.setValue(args.opacity)
    set_opacity(args.opacity)
form.pick_img.clicked.connect(get_img)
print(form.opacity_slider.value())
mainmenu.show()
sys.exit(app.exec())