import sys,os
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
    iw = pixmap.width()
    ih = pixmap.height()
    percent = 1
    maxw = int(app.primaryScreen().size().width()*percent)
    maxh = int(app.primaryScreen().size().height()*percent)
    if iw>ih:
        if iw>maxw:
            label.setPixmap(pixmap.scaledToWidth(maxw))
            ih = (maxw/iw)*ih
            iw = maxw
        else:
            label.setPixmap(pixmap)
    if ih>iw:
        if ih>maxh:
            label.setPixmap(pixmap.scaledToHeight(maxh))
            iw = (maxh/ih)*iw
            ih = maxh
        else:
            label.setPixmap(pixmap)
    label.setGeometry(0, 0, int(iw), int(ih))
    imgwindow.label = label
    imgwindow.resize(int(iw), int(ih))

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

def toggle_top_window():
    top = form.top_true.isChecked()
    window = form.window_true.isChecked()
    set_top_window(top,window)

## Max Memorry Allocated to Load Image Here in Megabytes
os.environ['QT_IMAGEIO_MAXALLOC'] = "2048"
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
imgwindow.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose, False)
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
form.window_true.toggled.connect(toggle_top_window)
form.top_true.toggled.connect(toggle_top_window)
mainmenu.show()
sys.exit(app.exec())