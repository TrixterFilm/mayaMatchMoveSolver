# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\catte\dev\mayaMatchMoveSolver\python\mmSolver\tools\solver\ui\solver_layout.ui'
#
# Created: Tue Dec 25 23:12:26 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 898)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.collection_layout = QtWidgets.QHBoxLayout()
        self.collection_layout.setSpacing(1)
        self.collection_layout.setObjectName("collection_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.collection_layout.addItem(spacerItem)
        self.collection_label = QtWidgets.QLabel(Form)
        self.collection_label.setObjectName("collection_label")
        self.collection_layout.addWidget(self.collection_label)
        self.collectionName_comboBox = QtWidgets.QComboBox(Form)
        self.collectionName_comboBox.setObjectName("collectionName_comboBox")
        self.collection_layout.addWidget(self.collectionName_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.collection_layout.addItem(spacerItem1)
        self.collectionSelect_pushButton = QtWidgets.QPushButton(Form)
        self.collectionSelect_pushButton.setObjectName("collectionSelect_pushButton")
        self.collection_layout.addWidget(self.collectionSelect_pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.collection_layout.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.collection_layout)
        self.objectAttribute_layout = QtWidgets.QHBoxLayout()
        self.objectAttribute_layout.setObjectName("objectAttribute_layout")
        self.object_layout = QtWidgets.QVBoxLayout()
        self.object_layout.setSpacing(1)
        self.object_layout.setObjectName("object_layout")
        self.object_frame = QtWidgets.QFrame(Form)
        self.object_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.object_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.object_frame.setObjectName("object_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.object_frame)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.objectAddRemove_layout = QtWidgets.QHBoxLayout()
        self.objectAddRemove_layout.setSpacing(1)
        self.objectAddRemove_layout.setObjectName("objectAddRemove_layout")
        self.object_label = QtWidgets.QLabel(self.object_frame)
        self.object_label.setObjectName("object_label")
        self.objectAddRemove_layout.addWidget(self.object_label)
        self.objectAdd_toolButton = QtWidgets.QToolButton(self.object_frame)
        self.objectAdd_toolButton.setObjectName("objectAdd_toolButton")
        self.objectAddRemove_layout.addWidget(self.objectAdd_toolButton)
        self.objectRemove_toolButton = QtWidgets.QToolButton(self.object_frame)
        self.objectRemove_toolButton.setObjectName("objectRemove_toolButton")
        self.objectAddRemove_layout.addWidget(self.objectRemove_toolButton)
        self.verticalLayout_5.addLayout(self.objectAddRemove_layout)
        self.object_treeView = QtWidgets.QTreeView(self.object_frame)
        self.object_treeView.setObjectName("object_treeView")
        self.verticalLayout_5.addWidget(self.object_treeView)
        self.object_layout.addWidget(self.object_frame)
        self.objectAttribute_layout.addLayout(self.object_layout)
        self.attribute_layout = QtWidgets.QVBoxLayout()
        self.attribute_layout.setSpacing(1)
        self.attribute_layout.setObjectName("attribute_layout")
        self.attribute_frame = QtWidgets.QFrame(Form)
        self.attribute_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.attribute_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attribute_frame.setObjectName("attribute_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.attribute_frame)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.attributeAddRemove_layout = QtWidgets.QHBoxLayout()
        self.attributeAddRemove_layout.setSpacing(1)
        self.attributeAddRemove_layout.setObjectName("attributeAddRemove_layout")
        self.attribute_label = QtWidgets.QLabel(self.attribute_frame)
        self.attribute_label.setObjectName("attribute_label")
        self.attributeAddRemove_layout.addWidget(self.attribute_label)
        self.attributeAdd_toolButton = QtWidgets.QToolButton(self.attribute_frame)
        self.attributeAdd_toolButton.setObjectName("attributeAdd_toolButton")
        self.attributeAddRemove_layout.addWidget(self.attributeAdd_toolButton)
        self.attributeRemove_toolButton = QtWidgets.QToolButton(self.attribute_frame)
        self.attributeRemove_toolButton.setObjectName("attributeRemove_toolButton")
        self.attributeAddRemove_layout.addWidget(self.attributeRemove_toolButton)
        self.verticalLayout_6.addLayout(self.attributeAddRemove_layout)
        self.attribute_treeView = QtWidgets.QTreeView(self.attribute_frame)
        self.attribute_treeView.setObjectName("attribute_treeView")
        self.verticalLayout_6.addWidget(self.attribute_treeView)
        self.attribute_layout.addWidget(self.attribute_frame)
        self.objectAttribute_layout.addLayout(self.attribute_layout)
        self.verticalLayout_4.addLayout(self.objectAttribute_layout)
        self.solverOptions_layout = QtWidgets.QVBoxLayout()
        self.solverOptions_layout.setSpacing(1)
        self.solverOptions_layout.setObjectName("solverOptions_layout")
        self.solverOptions_frame = QtWidgets.QFrame(Form)
        self.solverOptions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.solverOptions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.solverOptions_frame.setObjectName("solverOptions_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.solverOptions_frame)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.solverTop_layout = QtWidgets.QHBoxLayout()
        self.solverTop_layout.setObjectName("solverTop_layout")
        self.solver_label = QtWidgets.QLabel(self.solverOptions_frame)
        self.solver_label.setObjectName("solver_label")
        self.solverTop_layout.addWidget(self.solver_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.solverTop_layout.addItem(spacerItem3)
        self.solverAdd_toolButton = QtWidgets.QToolButton(self.solverOptions_frame)
        self.solverAdd_toolButton.setObjectName("solverAdd_toolButton")
        self.solverTop_layout.addWidget(self.solverAdd_toolButton)
        self.solverRemove_toolButton = QtWidgets.QToolButton(self.solverOptions_frame)
        self.solverRemove_toolButton.setObjectName("solverRemove_toolButton")
        self.solverTop_layout.addWidget(self.solverRemove_toolButton)
        self.verticalLayout_7.addLayout(self.solverTop_layout)
        self.solver_layout = QtWidgets.QHBoxLayout()
        self.solver_layout.setSpacing(1)
        self.solver_layout.setObjectName("solver_layout")
        self.solver_tableView = QtWidgets.QTableView(self.solverOptions_frame)
        self.solver_tableView.setObjectName("solver_tableView")
        self.solver_layout.addWidget(self.solver_tableView)
        self.solverSide_layout = QtWidgets.QVBoxLayout()
        self.solverSide_layout.setObjectName("solverSide_layout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.solverSide_layout.addItem(spacerItem4)
        self.solverMoveUp_toolButton = QtWidgets.QToolButton(self.solverOptions_frame)
        self.solverMoveUp_toolButton.setObjectName("solverMoveUp_toolButton")
        self.solverSide_layout.addWidget(self.solverMoveUp_toolButton)
        self.solverMoveDown_toolButton = QtWidgets.QToolButton(self.solverOptions_frame)
        self.solverMoveDown_toolButton.setObjectName("solverMoveDown_toolButton")
        self.solverSide_layout.addWidget(self.solverMoveDown_toolButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.solverSide_layout.addItem(spacerItem5)
        self.solver_layout.addLayout(self.solverSide_layout)
        self.verticalLayout_7.addLayout(self.solver_layout)
        self.solverOverrides_layout = QtWidgets.QHBoxLayout()
        self.solverOverrides_layout.setObjectName("solverOverrides_layout")
        self.overrideCurrentFrame_label = QtWidgets.QLabel(self.solverOptions_frame)
        self.overrideCurrentFrame_label.setObjectName("overrideCurrentFrame_label")
        self.solverOverrides_layout.addWidget(self.overrideCurrentFrame_label)
        self.overrideCurrentFrame_checkBox = QtWidgets.QCheckBox(self.solverOptions_frame)
        self.overrideCurrentFrame_checkBox.setText("")
        self.overrideCurrentFrame_checkBox.setObjectName("overrideCurrentFrame_checkBox")
        self.solverOverrides_layout.addWidget(self.overrideCurrentFrame_checkBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.solverOverrides_layout.addItem(spacerItem6)
        self.verticalLayout_7.addLayout(self.solverOverrides_layout)
        self.line = QtWidgets.QFrame(self.solverOptions_frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.statusLine_layout = QtWidgets.QHBoxLayout()
        self.statusLine_layout.setObjectName("statusLine_layout")
        self.statusLine_label = QtWidgets.QLabel(self.solverOptions_frame)
        self.statusLine_label.setObjectName("statusLine_label")
        self.statusLine_layout.addWidget(self.statusLine_label)
        self.verticalLayout_7.addLayout(self.statusLine_layout)
        self.emptySpace01_layout = QtWidgets.QHBoxLayout()
        self.emptySpace01_layout.setObjectName("emptySpace01_layout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.emptySpace01_layout.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.emptySpace01_layout)
        self.solverOptions_layout.addWidget(self.solverOptions_frame)
        self.verticalLayout_4.addLayout(self.solverOptions_layout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.collection_label.setText(QtWidgets.QApplication.translate("Form", "Collection", None, -1))
        self.collectionSelect_pushButton.setText(QtWidgets.QApplication.translate("Form", "Select", None, -1))
        self.object_label.setText(QtWidgets.QApplication.translate("Form", "Objects", None, -1))
        self.objectAdd_toolButton.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.objectRemove_toolButton.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.attribute_label.setText(QtWidgets.QApplication.translate("Form", "Attributes", None, -1))
        self.attributeAdd_toolButton.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.attributeRemove_toolButton.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.solver_label.setText(QtWidgets.QApplication.translate("Form", "Solvers", None, -1))
        self.solverAdd_toolButton.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.solverRemove_toolButton.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))
        self.solverMoveUp_toolButton.setText(QtWidgets.QApplication.translate("Form", "△", None, -1))
        self.solverMoveDown_toolButton.setText(QtWidgets.QApplication.translate("Form", "▽", None, -1))
        self.overrideCurrentFrame_label.setText(QtWidgets.QApplication.translate("Form", "Override Current Frame", None, -1))
        self.statusLine_label.setText(QtWidgets.QApplication.translate("Form", "Status.", None, -1))

