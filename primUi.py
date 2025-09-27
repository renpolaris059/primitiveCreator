try:
	from PySide6 import QtCore, QtWidgets, QtGui
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtWidgets, QtGui
	from shiboken2 import wrapInstance

import maya.OpenMayaUi as omui

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)

		self.resize(300,330)
		self.setWindowTitle("Primitive Creator")

def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()