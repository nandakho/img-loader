import sys,os
import argparse
from PyQt6.QtCore import *
from PyQt6.QtGui import *
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
    title = "Opacity: "+str(opacity)+"%"
    form.box_opacity.setTitle(title)

def set_ratio(ratio):
    title = "Maximum Image Ratio (On Pick Image): "+str(ratio)+"%"
    form.box_ratio.setTitle(title)

def get_img():
    fname = QFileDialog.getOpenFileName(None,'Open image','',"Any Image (*.jpg *.jpeg *.png *.gif *.bmp *.jfif *.pjpeg *.pjp *.apng *.avif *.svg *.webp *.ico *.tif *.tiff *.cur)")
    if fname[0]!='':
        set_img(fname[0],float(form.ratio_slider.value()/100))

def set_img(img_name,percent,size_new=None,size_old=None,resize=True):
    form.show_img.setEnabled(True)
    form.img_url.setText(img_name)
    pixmap = QPixmap(img_name)
    iw = pixmap.width()
    ih = pixmap.height()
    maxw = int(app.primaryScreen().size().width()*percent)
    maxh = int(app.primaryScreen().size().height()*percent)
    if size_new!=None and size_old!=None:
        pixmap = pixmap.scaled(size_new.width(),size_new.height(),Qt.AspectRatioMode.KeepAspectRatio)
    else:
        pixmap = pixmap.scaled(maxw,maxh,Qt.AspectRatioMode.KeepAspectRatio) if iw>maxw or ih>maxh else pixmap
    label.setPixmap(pixmap)
    label.setGeometry(0, 0, pixmap.width(), pixmap.height())
    imgwindow.label = label
    imgwindow.setWindowTitle(img_name)
    if resize==True:
        imgwindow.adjustSize()

def set_top_window(isTop,isWindow):
    imgwindow.destroy()
    reopen = False
    if imgwindow.isVisible():
        reopen = True
    imgwindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False if isWindow==True else True)
    imgwindow.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, False if isWindow==True else True)
    imgwindow.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True if isWindow!=True else False)
    imgwindow.setWindowFlag(Qt.WindowType.Window, True)
    imgwindow.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True if isTop==True else False)
    imgwindow.setWindowFlag(Qt.WindowType.FramelessWindowHint, False if isWindow==True else True)
    imgwindow.setWindowFlag(Qt.WindowType.WindowTransparentForInput, True if isWindow!=True else False)
    if reopen==True:
        imgwindow.show()
    imgwindow.adjustSize()

def img_resize(event):
    set_img(imgwindow.windowTitle(),float(form.ratio_slider.value()/100),size_new=event.size(),size_old=event.oldSize(),resize=False)

def toggle_top_window():
    top = form.top_true.isChecked()
    window = form.window_true.isChecked()
    set_top_window(top,window)

## Max Memorry Allocated to Load Image Here in Megabytes
os.environ['QT_IMAGEIO_MAXALLOC'] = "2048"
parser = argparse.ArgumentParser(description="Open image file as transparent overlay")
parser.add_argument('-i','--image-name', type=str, help="Accept String as target's file name (Optional)")
parser.add_argument('-o','--opacity', type=int, help="Accept Integer as percentage of desired opacity value (Optional, Default: 50)", default=50)
parser.add_argument('-w','--windowed', type=bool, action=argparse.BooleanOptionalAction, help="Show image with window/draggable (False) (Optional, Default: False)")
parser.add_argument('-t','--top', type=bool, action=argparse.BooleanOptionalAction, help="Stay on top (True) or not (False) (Optional, Default: False)")
parser.add_argument('-m','--max-ratio', type=int, help="If loaded image's dimension is larger than the screen's dimension, this value will determine maximum dimension size calculated by screen's resolution times the percentage of given value (Optional, Default: 80)", default=80)
args = parser.parse_args()
app = QApplication(sys.argv)
app.setStyle('Fusion')
Form, Window = uic.loadUiType("img-loader.ui")
mainmenu = Window()
imgwindow = QWidget()
imgwindow.resizeEvent = img_resize
imgwindow.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose, False)
imgwindow.setWindowFlag(Qt.WindowType.WindowFullscreenButtonHint,False)
imgwindow.setWindowFlag(Qt.WindowType.WindowCloseButtonHint,False)
imgwindow.setWindowFlag(Qt.WindowType.WindowMinMaxButtonsHint,False)
imgwindow.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint,False)
imgwindow.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint,False)
imgwindow.setWindowFlag(Qt.WindowType.WindowSystemMenuHint,False)
label = QLabel(imgwindow)
form = Form()
form.setupUi(mainmenu)
mainmenu.setFixedSize(mainmenu.size())
mainmenu.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
set_top_window(args.windowed,args.top)
form.show_img.clicked.connect(show_img)
form.opacity_slider.valueChanged.connect(set_opacity)
form.ratio_slider.valueChanged.connect(set_ratio)
if args.image_name:
    set_img(args.image_name,float(args.max_ratio/100))
if args.opacity:
    form.opacity_slider.setValue(args.opacity)
    set_opacity(args.opacity)
if args.max_ratio:
    form.ratio_slider.setValue(args.max_ratio)
form.pick_img.clicked.connect(get_img)
form.window_true.toggled.connect(toggle_top_window)
form.top_true.toggled.connect(toggle_top_window)
mainmenu.show()
sys.exit(app.exec())