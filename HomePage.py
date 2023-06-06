# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"#LeftMenuBar,.ViewMore{\n"
" background-color:#2596be;\n"
" border-radius:10px\n"
"}\n"
"#searchBox{\n"
"border-radius:10px;\n"
"border:black;\n"
"}\n"
"#c1,#c2,#c3,#c4{\n"
"background-color:;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color:#2596be;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel#label_7:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setStyleSheet("background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_10.setStyleSheet("QPushButton#pushButton_10:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/feather/message-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_5.addWidget(self.pushButton_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/feather/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/feather/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_5.addWidget(self.pushButton_11)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_18 = QtWidgets.QFrame(self.frame_2)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_4.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_2)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_4.addWidget(self.frame_19)
        self.horizontalLayout.addWidget(self.frame_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MainBody = QtWidgets.QWidget(self.widget)
        self.MainBody.setObjectName("MainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_21 = QtWidgets.QFrame(self.MainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_20 = QtWidgets.QFrame(self.frame_21)
        self.frame_20.setStyleSheet("background-color:")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setStyleSheet("background-color:#2596be;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_7 = QtWidgets.QWidget(self.frame_22)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_12.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/feather/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_11.addWidget(self.pushButton_12, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel#label:hover{\n"
"background-color:white;\n"
"border-top-left-radius:10px;\n"
"border:2px solid white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_10.addWidget(self.widget_7)
        self.widget_9 = QtWidgets.QWidget(self.frame_22)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_9 = QtWidgets.QLabel(self.widget_9)
        self.label_9.setSizeIncrement(QtCore.QSize(30, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icons/feather/search.svg"))
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_21.addWidget(self.label_9)
        self.searchBox_2 = QtWidgets.QLineEdit(self.widget_9)
        self.searchBox_2.setStyleSheet("*{\n"
"background-color:transparent;\n"
"border-radius:10px;\n"
"border:2px solid black;\n"
"}")
        self.searchBox_2.setObjectName("searchBox_2")
        self.horizontalLayout_21.addWidget(self.searchBox_2)
        self.horizontalLayout_10.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.frame_22)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_13.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/feather/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_22.addWidget(self.pushButton_13)
        self.label_10 = QtWidgets.QLabel(self.widget_10)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_22.addWidget(self.label_10)
        self.horizontalLayout_10.addWidget(self.widget_10)
        self.horizontalLayout_2.addWidget(self.frame_22, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_9.addWidget(self.frame_20, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_21)
        self.cards_2 = QtWidgets.QWidget(self.MainBody)
        self.cards_2.setObjectName("cards_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cards_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.c1 = QtWidgets.QWidget(self.cards_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.c1.setFont(font)
        self.c1.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"border:10px;\n"
"}\n"
"QLabel#c1,#c2,#c3,c4:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.c1.setObjectName("c1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.c1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.c1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(24, 24))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/feather/shopping-cart.svg"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_4 = QtWidgets.QLabel(self.c1)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_6.addWidget(self.c1)
        self.c2 = QtWidgets.QWidget(self.cards_2)
        self.c2.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"}")
        self.c2.setObjectName("c2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.c2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.c2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setMinimumSize(QtCore.QSize(24, 24))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/icons/feather/shopping-cart.svg"))
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_12.addWidget(self.label_20)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.label_16 = QtWidgets.QLabel(self.c2)
        self.label_16.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.horizontalLayout_6.addWidget(self.c2)
        self.c3 = QtWidgets.QWidget(self.cards_2)
        self.c3.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"}")
        self.c3.setObjectName("c3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.c3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.c3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setMinimumSize(QtCore.QSize(24, 24))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/icons/feather/shopping-cart.svg"))
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_13.addWidget(self.label_23)
        self.verticalLayout_7.addWidget(self.frame_6)
        self.label_21 = QtWidgets.QLabel(self.c3)
        self.label_21.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_7.addWidget(self.label_21)
        self.horizontalLayout_6.addWidget(self.c3)
        self.c4 = QtWidgets.QWidget(self.cards_2)
        self.c4.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"}")
        self.c4.setObjectName("c4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.c4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.c4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_25 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_14.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.frame_7)
        self.label_26.setMinimumSize(QtCore.QSize(24, 24))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/icons/feather/shopping-cart.svg"))
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_14.addWidget(self.label_26)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.label_24 = QtWidgets.QLabel(self.c4)
        self.label_24.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_8.addWidget(self.label_24)
        self.horizontalLayout_6.addWidget(self.c4)
        self.verticalLayout.addWidget(self.cards_2)
        self.table_2 = QtWidgets.QWidget(self.MainBody)
        self.table_2.setObjectName("table_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.table_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_6 = QtWidgets.QWidget(self.table_2)
        self.widget_6.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_8 = QtWidgets.QFrame(self.widget_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_27 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("QLabel#label_27:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_16.addWidget(self.label_27)
        self.ViewMore_2 = QtWidgets.QPushButton(self.frame_8)
        self.ViewMore_2.setStyleSheet("#ViewMore_2{\n"
" background-color:#2596be;\n"
" border-radius:10px;\n"
"border: 2px solid #2596be;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/feather/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ViewMore_2.setIcon(icon6)
        self.ViewMore_2.setObjectName("ViewMore_2")
        self.horizontalLayout_16.addWidget(self.ViewMore_2)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.widget_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_28 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel#label_28:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_17.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("QLabel#label_29:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_17.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("QLabel#label_30:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_17.addWidget(self.label_30)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.widget_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_32 = QtWidgets.QLabel(self.frame_11)
        self.label_32.setStyleSheet("QLabel#label_32:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_10.addWidget(self.label_32)
        self.label_31 = QtWidgets.QLabel(self.frame_11)
        self.label_31.setStyleSheet("QLabel#label_31:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_10.addWidget(self.label_31)
        self.label_33 = QtWidgets.QLabel(self.frame_11)
        self.label_33.setStyleSheet("QLabel#label_33:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_10.addWidget(self.label_33)
        self.horizontalLayout_18.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_34 = QtWidgets.QLabel(self.frame_12)
        self.label_34.setStyleSheet("QLabel#label_34:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_11.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.frame_12)
        self.label_35.setStyleSheet("QLabel#label_35:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_11.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.frame_12)
        self.label_36.setStyleSheet("QLabel#label_36:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_11.addWidget(self.label_36)
        self.horizontalLayout_18.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_37 = QtWidgets.QLabel(self.frame_13)
        self.label_37.setStyleSheet("QLabel#label_37:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_12.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.frame_13)
        self.label_38.setStyleSheet("QLabel#label_38:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_12.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.frame_13)
        self.label_39.setStyleSheet("QLabel#label_37:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_12.addWidget(self.label_39)
        self.horizontalLayout_18.addWidget(self.frame_13)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.horizontalLayout_15.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.table_2)
        self.widget_8.setStyleSheet("*{\n"
"background-color:#bdcbce;\n"
"}")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_14 = QtWidgets.QFrame(self.widget_8)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_40 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("QLabel#label_40:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border:2px solid white;\n"
"}")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_19.addWidget(self.label_40)
        self.ViewMore = QtWidgets.QPushButton(self.frame_14)
        self.ViewMore.setStyleSheet("#ViewMore{\n"
" background-color:#2596be;\n"
"border-radius:10px;\n"
"border:2px solid #2596be;\n"
"}")
        self.ViewMore.setIcon(icon6)
        self.ViewMore.setObjectName("ViewMore")
        self.horizontalLayout_19.addWidget(self.ViewMore)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.widget_8)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_14.addWidget(self.pushButton_9)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_14.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_14.addWidget(self.pushButton_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_14.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_14.addWidget(self.pushButton_7)
        self.horizontalLayout_20.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_41 = QtWidgets.QLabel(self.frame_17)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.verticalLayout_15.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.frame_17)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.verticalLayout_15.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.frame_17)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_15.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.frame_17)
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.verticalLayout_15.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.frame_17)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_15.addWidget(self.label_45)
        self.horizontalLayout_20.addWidget(self.frame_17)
        self.verticalLayout_13.addWidget(self.frame_15)
        self.horizontalLayout_15.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.table_2)
        self.verticalLayout_3.addWidget(self.MainBody)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Count Ai"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.pushButton_10.setText(_translate("MainWindow", "Message"))
        self.pushButton_4.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_11.setText(_translate("MainWindow", "Logout"))
        self.label_8.setText(_translate("MainWindow", "DashBoard"))
        self.searchBox_2.setPlaceholderText(_translate("MainWindow", "search here !"))
        self.label_10.setText(_translate("MainWindow", "Jeyaram"))
        self.label_5.setText(_translate("MainWindow", "20,00,000"))
        self.label_4.setText(_translate("MainWindow", "INR"))
        self.label_19.setText(_translate("MainWindow", "20,00,000"))
        self.label_16.setText(_translate("MainWindow", "INR"))
        self.label_22.setText(_translate("MainWindow", "20,00,000"))
        self.label_21.setText(_translate("MainWindow", "INR"))
        self.label_25.setText(_translate("MainWindow", "20,00,000"))
        self.label_24.setText(_translate("MainWindow", "INR"))
        self.label_27.setText(_translate("MainWindow", "Latest Products"))
        self.ViewMore_2.setText(_translate("MainWindow", "ViewMore"))
        self.label_28.setText(_translate("MainWindow", "product"))
        self.label_29.setText(_translate("MainWindow", "price"))
        self.label_30.setText(_translate("MainWindow", "store"))
        self.label_32.setText(_translate("MainWindow", "milk"))
        self.label_31.setText(_translate("MainWindow", "biscut"))
        self.label_33.setText(_translate("MainWindow", "drinks"))
        self.label_34.setText(_translate("MainWindow", "10$"))
        self.label_35.setText(_translate("MainWindow", "5$"))
        self.label_36.setText(_translate("MainWindow", "15$"))
        self.label_37.setText(_translate("MainWindow", "arokia"))
        self.label_38.setText(_translate("MainWindow", "delight"))
        self.label_39.setText(_translate("MainWindow", "sevenup"))
        self.label_40.setText(_translate("MainWindow", "Clients"))
        self.ViewMore.setText(_translate("MainWindow", "ViewMore"))
        self.pushButton_9.setText(_translate("MainWindow", "Lincoln"))
        self.pushButton_6.setText(_translate("MainWindow", "william"))
        self.pushButton_5.setText(_translate("MainWindow", "jeyaram"))
        self.pushButton_8.setText(_translate("MainWindow", "matthe"))
        self.pushButton_7.setText(_translate("MainWindow", "Jackson"))
import resourc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
