try:
	from PySide6 import QtCore, QtWidgets, QtGui
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtWidgets, QtGui
	from shiboken2 import wrapInstance

from . import primUtil as pmutil
import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.resize(300,350)
		self.setWindowTitle("Primitive Creator")

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.primitive_listWidget = QtWidgets.QListWidget()
		self.primitive_listWidget.setIconSize(QtCore.QSize(60,60))
		self.primitive_listWidget.setSpacing(5)
		self.primitive_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
		self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.primitive_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)

		self.name_label = QtWidgets.QLabel("Name : ")
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet('background-color:#591C21; color:#FACFCE')
		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		
		self.create_button = QtWidgets.QPushButton("Create")
		self.create_button.setStyleSheet(
			'''
			QPushButton {
				background-color: #8C1F28
			}
			'''
			)
		self.create_button.clicked.connect(self.onClickCreate)

		self.cancel_button = QtWidgets.QPushButton("Cancel")
		self.cancel_button.setStyleSheet(
			'''
			QPushButton {
				background-color: #8C1F28
			}
			'''
			)
		self.cancel_button.clicked.connect(self.close)

		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)

		self.initIconWidget()

	def initIconWidget(self):
		prims = ['cone', 'torus', 'cube', 'sphere']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}')))
			item.setData(QtCore.Qt.UserRole, prim)
			self.primitive_listWidget.addItem(item)

	def onClickCreate(self):
		item = self.primitive_listWidget.currentItem()
		if not item:
			return
		prim = item.data(QtCore.Qt.UserRole)
		name = self.name_lineEdit.text().strip()
		pmutil.createPrim(prim, name)

def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()