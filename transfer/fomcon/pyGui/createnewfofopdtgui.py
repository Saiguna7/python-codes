# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Set\Documents\CompSys\4th Semeter THESIS\Code\fomcon\guipyQtui\createnewfofopdtgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogCreateNewFOTF(object):
    def setupUi(self, dialogCreateNewFOTF):
        dialogCreateNewFOTF.setObjectName("dialogCreateNewFOTF")
        dialogCreateNewFOTF.setWindowModality(QtCore.Qt.WindowModal)
        dialogCreateNewFOTF.resize(339, 187)
        dialogCreateNewFOTF.setMinimumSize(QtCore.QSize(0, 0))
        dialogCreateNewFOTF.setMaximumSize(QtCore.QSize(480, 360))
        dialogCreateNewFOTF.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogCreateNewFOTF)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(dialogCreateNewFOTF)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditSysName = QtWidgets.QLineEdit(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSysName.sizePolicy().hasHeightForWidth())
        self.lineEditSysName.setSizePolicy(sizePolicy)
        self.lineEditSysName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditSysName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSysName.setObjectName("lineEditSysName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSysName)
        self.label_4 = QtWidgets.QLabel(dialogCreateNewFOTF)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_GainK = QtWidgets.QLineEdit(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_GainK.sizePolicy().hasHeightForWidth())
        self.lineEdit_GainK.setSizePolicy(sizePolicy)
        self.lineEdit_GainK.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_GainK.setText("")
        self.lineEdit_GainK.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_GainK.setObjectName("lineEdit_GainK")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_GainK)
        self.label_3 = QtWidgets.QLabel(dialogCreateNewFOTF)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_DelayText = QtWidgets.QLineEdit(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_DelayText.sizePolicy().hasHeightForWidth())
        self.lineEdit_DelayText.setSizePolicy(sizePolicy)
        self.lineEdit_DelayText.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_DelayText.setText("")
        self.lineEdit_DelayText.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_DelayText.setObjectName("lineEdit_DelayText")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_DelayText)
        self.label_5 = QtWidgets.QLabel(dialogCreateNewFOTF)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_TimeConstant = QtWidgets.QLineEdit(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_TimeConstant.sizePolicy().hasHeightForWidth())
        self.lineEdit_TimeConstant.setSizePolicy(sizePolicy)
        self.lineEdit_TimeConstant.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_TimeConstant.setText("")
        self.lineEdit_TimeConstant.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_TimeConstant.setObjectName("lineEdit_TimeConstant")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_TimeConstant)
        self.label_2 = QtWidgets.QLabel(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_OrderAlpha = QtWidgets.QLineEdit(dialogCreateNewFOTF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_OrderAlpha.sizePolicy().hasHeightForWidth())
        self.lineEdit_OrderAlpha.setSizePolicy(sizePolicy)
        self.lineEdit_OrderAlpha.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_OrderAlpha.setText("")
        self.lineEdit_OrderAlpha.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_OrderAlpha.setObjectName("lineEdit_OrderAlpha")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_OrderAlpha)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOK = QtWidgets.QPushButton(dialogCreateNewFOTF)
        self.pushButtonOK.setEnabled(False)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout.addWidget(self.pushButtonOK)
        self.pushButtonCancel = QtWidgets.QPushButton(dialogCreateNewFOTF)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(dialogCreateNewFOTF)
        QtCore.QMetaObject.connectSlotsByName(dialogCreateNewFOTF)

    def retranslateUi(self, dialogCreateNewFOTF):
        _translate = QtCore.QCoreApplication.translate
        dialogCreateNewFOTF.setWindowTitle(_translate("dialogCreateNewFOTF", "Create new FO-FOPDT"))
        self.label.setText(_translate("dialogCreateNewFOTF", "System Name:"))
        self.label_4.setText(_translate("dialogCreateNewFOTF", "Gain ( K ): "))
        self.label_3.setText(_translate("dialogCreateNewFOTF", "Delay{s} ( L >= 0 ): "))
        self.label_5.setText(_translate("dialogCreateNewFOTF", "Time Constant: "))
        self.label_2.setText(_translate("dialogCreateNewFOTF", "Alpha : {0.01 < alpha < 2} "))
        self.pushButtonOK.setText(_translate("dialogCreateNewFOTF", "OK"))
        self.pushButtonCancel.setText(_translate("dialogCreateNewFOTF", "Cancel"))

