```python
from PyQt6 import QtWidgets, QtCore

#------------------------------------------------------------------------------
# Basic Usage
#------------------------------------------------------------------------------

# Creating an application
app = QtWidgets.QApplication([])

# Creating a widget
widget = QtWidgets.QWidget()

# Setting the widget's layout
layout = QtWidgets.QVBoxLayout()
widget.setLayout(layout)

# Creating a label widget and adding it to the layout
label = QtWidgets.QLabel("Hello, World!")
layout.addWidget(label)

# Showing the widget
widget.show()

# Running the application
app.exec()

#------------------------------------------------------------------------------
# Widgets
#------------------------------------------------------------------------------

# Label widget
label = QtWidgets.QLabel("Label")

# LineEdit widget
line_edit = QtWidgets.QLineEdit()

# PushButton widget
push_button = QtWidgets.QPushButton("Click Me!")

# RadioButton widget
radio_button = QtWidgets.QRadioButton("Radio Button")

# CheckBox widget
check_box = QtWidgets.QCheckBox("Check Box")

# ComboBox widget
combo_box = QtWidgets.QComboBox()

# DateEdit widget
date_edit = QtWidgets.QDateEdit()

# DateTimeEdit widget
datetime_edit = QtWidgets.QDateTimeEdit()

# Dial widget
dial = QtWidgets.QDial()

# DoubleSpinBox widget
double_spin_box = QtWidgets.QDoubleSpinBox()

# Frame widget
frame = QtWidgets.QFrame()

# GraphicsView widget
graphics_view = QtWidgets.QGraphicsView()

# GroupBox widget
group_box = QtWidgets.QGroupBox()

# Label widget
label = QtWidgets.QLabel("Label")

# ListView widget
list_view = QtWidgets.QListView()

# Menu widget
menu = QtWidgets.QMenu()

# MenuBar widget
menu_bar = QtWidgets.QMenuBar()

# ProgressBar widget
progress_bar = QtWidgets.QProgressBar()

# ScrollArea widget
scroll_area = QtWidgets.QScrollArea()

# ScrollBar widget
scroll_bar = QtWidgets.QScrollBar()

# Slider widget
slider = QtWidgets.QSlider()

# SpinBox widget
spin_box = QtWidgets.QSpinBox()

# StatusBar widget
status_bar = QtWidgets.QStatusBar()

# TabWidget widget
tab_widget = QtWidgets.QTabWidget()

# TextEdit widget
text_edit = QtWidgets.QTextEdit()

# TimeEdit widget
time_edit = QtWidgets.QTimeEdit()

# ToolBar widget
tool_bar = QtWidgets.QToolBar()

# TreeView widget
tree_view = QtWidgets.QTreeView()

# WebView widget
web_view = QtWidgets.QWebView()

#------------------------------------------------------------------------------
# Signals and Slots
#------------------------------------------------------------------------------

class MyWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button = QtWidgets.QPushButton("Click Me!")
        self.label = QtWidgets.QLabel("No button click yet!")
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        self.button.clicked.connect(self.handle_button_click)
    
    def handle_button_click(self):
        self.label.setText("Button clicked!")

#------------------------------------------------------------------------------
# Layouts
#------------------------------------------------------------------------------

# Horizontal layout
layout = QtWidgets.QHBoxLayout()
layout.addWidget(QtWidgets.QLabel("Username:"))
layout.addWidget(QtWidgets.QLineEdit())
layout.addWidget(QtWidgets.QLabel("Password:"))
layout.addWidget(QtWidgets.QLineEdit())
layout.addWidget(QtWidgets.QPushButton("Login"))
widget.setLayout(layout)

# Vertical layout
layout = QtWidgets.QVBoxLayout()
layout.addWidget(QtWidgets.QLabel("Username:"))
layout.addWidget(QtWidgets.QLineEdit())
layout.addWidget(QtWidgets.QLabel("Password:"))
layout.addWidget(QtWidgets.QLineEdit())
layout.addWidget(QtWidgets.QPushButton("Login"))
widget.setLayout(layout)

# Grid layout
layout = QtWidgets.QGridLayout()
layout.addWidget(QtWidgets.QLabel("Username:"), 0, 0)
layout.addWidget(QtWidgets.QLineEdit(), 0, 1)
layout.addWidget(QtWidgets.QLabel("Password:"), 1, 0)
layout.addWidget(QtWidgets.QLineEdit(), 1, 1)
layout.addWidget(QtWidgets.QPushButton("Login"), 2, 0, 1, 2)
widget.setLayout(layout)

#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------

# Message box
QtWidgets.QMessageBox.information(
    None,
    "Information",
    "This is an information message."
)

# Input dialog
result, ok = QtWidgets.QInputDialog.getText(
    None,
    "Input",
    "Enter your name:"
)

if ok:
    print("Your name is:", result)

# Color dialog
color = QtWidgets.QColorDialog.getColor()
if color.isValid():
    print("Selected color:", color.name())

# File dialog
filename, _ = QtWidgets.QFileDialog.getOpenFileName(
    None,
    "Open file",
    "",
    "Text files (*.txt);;All files (*.*)"
)

if filename:
    print("Selected file:", filename)

#------------------------------------------------------------------------------
# Threading
#------------------------------------------------------------------------------

class MyThread(QtCore.QThread):
    
    def run(self):
        for i in range(10):
            time.sleep(1)
            self.emit(QtCore.SIGNAL("message"), f"Count: {i+1}")
            
class MyWidget(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.label = QtWidgets.QLabel("Waiting for thread...")
        self.button = QtWidgets.QPushButton("Start thread")
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.thread = MyThread()
        self.thread.message.connect(self.handle_thread_message)
        self.button.clicked.connect(self.thread.start)
    
    def handle_thread_message(self, message):
        self.label.setText(message)

#------------------------------------------------------------------------------
# Resources
#------------------------------------------------------------------------------

# Embed an image in the executable
pyrcc5 -o resources_rc.py resources.qrc

# resources.qrc:
<RCC>
  <qresource prefix="/images">
    <file>image.png</file>
  </qresource>
</RCC>

# Use the embedded image in the code
pixmap = QtGui.QPixmap(":/images/image.png")
label = QtWidgets.QLabel()
label.setPixmap(pixmap)

#------------------------------------------------------------------------------
# Internationalization
#------------------------------------------------------------------------------

# Generate a translation template
pylupdate5 myapp.py -ts myapp_en.ts

# Translate the template to a specific language
lrelease myapp_en.ts
lrelease myapp_es.ts

# Use the translations in the code
translator = QtCore.QTranslator()
translator.load("myapp_es.qm")
app.installTranslator(translator)
```