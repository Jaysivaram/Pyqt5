# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(866, 767)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(34)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("#Lemail{\n"
"background-color:#e6f1f1;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :10px\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/image/login.png);\n"
"border-top-left-radius:50px;\n"
"")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.widget)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setUnderline(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border-bottom-right-radius:50px;\n"
"background-color:white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("*{\n"
"}\n"
"\n"
"#Lemail{\n"
"background-color:#e6f1f1;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :10px\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("#Lemail{\n"
"background-color:#e6f1f1;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :10px\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Lemail = QtWidgets.QLineEdit(self.frame_5)
        self.Lemail.setStyleSheet("background-color:#e6f1f1;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :5px")
        self.Lemail.setAlignment(QtCore.Qt.AlignCenter)
        self.Lemail.setObjectName("Lemail")
        self.verticalLayout_5.addWidget(self.Lemail)
        self.Lpassword = QtWidgets.QLineEdit(self.frame_5)
        self.Lpassword.setStyleSheet("background-color:#e6f1f1;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :5px")
        self.Lpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Lpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.Lpassword.setObjectName("Lpassword")
        self.verticalLayout_5.addWidget(self.Lpassword)
        self.Login = QtWidgets.QPushButton(self.frame_5)
        self.Login.setStyleSheet("QPushButton#Login{\n"
"background-color:#0fb7b7;\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :5px\n"
"}\n"
"\n"
"QPushButton#Login:pressed{\n"
"background-color:#047b7b;\n"
"}")
        self.Login.setObjectName("Login")
        self.verticalLayout_5.addWidget(self.Login)
        self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RegisterHere = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.RegisterHere.setFont(font)
        self.RegisterHere.setStyleSheet("QPushButton#pushButton_2:pressed{\n"
"background-color:#047b7b;\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"\n"
"border:none;\n"
"border-bottom-color: 2px solid rgba(46,82,101,200);\n"
"color:solid rgba(240);\n"
"border-radius :10px\n"
"}")
        self.RegisterHere.setObjectName("RegisterHere")
        self.verticalLayout_3.addWidget(self.RegisterHere, 0, QtCore.Qt.AlignTop)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LoGin"))
        self.Lemail.setPlaceholderText(_translate("Form", "user email"))
        self.Lpassword.setPlaceholderText(_translate("Form", "password"))
        self.Login.setText(_translate("Form", "Login"))
        self.RegisterHere.setText(_translate("Form", "Resgister Here!"))
        self.label_2.setText(_translate("Form", "newUser"))
import resourc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LoginForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())