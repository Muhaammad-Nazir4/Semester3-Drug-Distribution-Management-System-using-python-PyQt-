# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewrouterider.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import osmnx as ox
import networkx as nx
import folium
import webbrowser
import taxicab as tc
shortest_route = []

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(998, 607)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_41 = QtWidgets.QFrame(self.frame_2)
        self.frame_41.setMinimumSize(QtCore.QSize(348, 0))
        self.frame_41.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_41.setStyleSheet("\n"
"QPushButton#takeorderbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#takeorderbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#takeorderbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#viewassignedorderbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#viewassignedorderbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#viewassignedorderbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#viewroutebutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#viewroutebutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#viewroutebutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#orderdeliveredbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#orderdeliveredbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#orderdeliveredbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#seebonusbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#seebonusbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#seebonusbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#viewallproductbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#viewallproductbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#viewallproductbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#sendemailbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#sendemailbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#sendemailbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"QPushButton#viewmonthlyreportbutton{\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#viewmonthlyreportbutton:pressed{\n"
"color:gray;\n"
"}\n"
"QPushButton#viewmonthlyreportbutton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}\n"
"color:white;\n"
"background-color:#2783A3;\n"
"")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_41)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_42 = QtWidgets.QFrame(self.frame_41)
        self.frame_42.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_43 = QtWidgets.QFrame(self.frame_42)
        self.frame_43.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_43)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_38 = QtWidgets.QFrame(self.frame_43)
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_38)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.backlb = QtWidgets.QLabel(self.frame_38)
        self.backlb.setStyleSheet("image:url(:/newPrefix/back.png);")
        self.backlb.setText("")
        self.backlb.setObjectName("backlb")
        self.gridLayout_23.addWidget(self.backlb, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_38, 0, 0, 1, 1)
        self.frame_37 = QtWidgets.QFrame(self.frame_43)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.gridLayout_9.addWidget(self.frame_37, 1, 0, 1, 1)
        self.frame_39 = QtWidgets.QFrame(self.frame_43)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.gridLayout_9.addWidget(self.frame_39, 2, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.frame_43)
        self.frame_44 = QtWidgets.QFrame(self.frame_42)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_44)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_10 = QtWidgets.QLabel(self.frame_44)
        self.label_10.setStyleSheet("color:white;\n"
"font: 26pt \"Britannic Bold\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout_11.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.frame_44)
        self.frame_45 = QtWidgets.QFrame(self.frame_42)
        self.frame_45.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_8.addWidget(self.frame_45)
        self.verticalLayout_7.addWidget(self.frame_42)
        self.frame_46 = QtWidgets.QFrame(self.frame_41)
        self.frame_46.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_47 = QtWidgets.QFrame(self.frame_46)
        self.frame_47.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_9.addWidget(self.frame_47)
        self.frame_48 = QtWidgets.QFrame(self.frame_46)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_48)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_49 = QtWidgets.QFrame(self.frame_48)
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_49)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.takeorderbutton = QtWidgets.QPushButton(self.frame_49)
        self.takeorderbutton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.takeorderbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.takeorderbutton.setStyleSheet("text-align:left;\n"
"font: 13pt \"Britannic\";\n"
"padding-left:4px;\n"
"")
        self.takeorderbutton.setObjectName("takeorderbutton")
        self.gridLayout_12.addWidget(self.takeorderbutton, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_49)
        self.label_11.setMaximumSize(QtCore.QSize(40, 30))
        self.label_11.setStyleSheet("image:url(:/newPrefix/uiForm/3022237-200-removebg-preview.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_49)
        self.frame_50 = QtWidgets.QFrame(self.frame_48)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_50)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.viewassignedorderbutton = QtWidgets.QPushButton(self.frame_50)
        self.viewassignedorderbutton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.viewassignedorderbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewassignedorderbutton.setStyleSheet("font: 13pt \"Britannic\";\n"
"text-align:left;\n"
"padding-left:4px;")
        self.viewassignedorderbutton.setObjectName("viewassignedorderbutton")
        self.gridLayout_13.addWidget(self.viewassignedorderbutton, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_50)
        self.label_12.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_12.setStyleSheet("image:url(:/newPrefix/uiForm/assign.png)")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_13.addWidget(self.label_12, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_50)
        self.horizontalLayout_9.addWidget(self.frame_48)
        self.frame_51 = QtWidgets.QFrame(self.frame_46)
        self.frame_51.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.horizontalLayout_9.addWidget(self.frame_51)
        self.verticalLayout_7.addWidget(self.frame_46)
        self.frame_52 = QtWidgets.QFrame(self.frame_41)
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_53 = QtWidgets.QFrame(self.frame_52)
        self.frame_53.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_10.addWidget(self.frame_53)
        self.frame_54 = QtWidgets.QFrame(self.frame_52)
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_55 = QtWidgets.QFrame(self.frame_54)
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_55)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.viewroutebutton = QtWidgets.QPushButton(self.frame_55)
        self.viewroutebutton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.viewroutebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewroutebutton.setStyleSheet("font: 13pt \"Britannic\";\n"
"text-align:left;\n"
"padding-left:4px;")
        self.viewroutebutton.setObjectName("viewroutebutton")
        self.gridLayout_14.addWidget(self.viewroutebutton, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_55)
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_13.setStyleSheet("image:url(:/newPrefix/uiForm/download__2_-removebg-preview.png)\n"
"\n"
"\n"
"")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_14.addWidget(self.label_13, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_55)
        self.frame_56 = QtWidgets.QFrame(self.frame_54)
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_56)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.orderdeliveredbutton = QtWidgets.QPushButton(self.frame_56)
        self.orderdeliveredbutton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.orderdeliveredbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.orderdeliveredbutton.setStyleSheet("font: 13pt \"Britannic\";\n"
"text-align:left;\n"
"padding-left:4px;")
        self.orderdeliveredbutton.setObjectName("orderdeliveredbutton")
        self.gridLayout_15.addWidget(self.orderdeliveredbutton, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_56)
        self.label_14.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_14.setStyleSheet("image:url(:/newPrefix/uiForm/87932.png)")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_15.addWidget(self.label_14, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.frame_56)
        self.horizontalLayout_10.addWidget(self.frame_54)
        self.frame_57 = QtWidgets.QFrame(self.frame_52)
        self.frame_57.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_10.addWidget(self.frame_57)
        self.verticalLayout_7.addWidget(self.frame_52)
        self.frame_58 = QtWidgets.QFrame(self.frame_41)
        self.frame_58.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_58)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_59 = QtWidgets.QFrame(self.frame_58)
        self.frame_59.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.horizontalLayout_11.addWidget(self.frame_59)
        self.frame_60 = QtWidgets.QFrame(self.frame_58)
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_60)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_61 = QtWidgets.QFrame(self.frame_60)
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_61)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_15 = QtWidgets.QLabel(self.frame_61)
        self.label_15.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_15.setStyleSheet("image:url(:/newPrefix/uiForm/scalable-vector-graphics-computer-icons-gone-boy-portable-network-graphics-png-favpng-kSX9VUatX2qFUdngE08mdPmd4_t-removebg-preview.png)")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_16.addWidget(self.label_15, 0, 0, 1, 1)
        self.seebonusbutton = QtWidgets.QPushButton(self.frame_61)
        self.seebonusbutton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.seebonusbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seebonusbutton.setStyleSheet("font: 13pt \"Britannic\";\n"
"text-align:left;\n"
"padding-left:4px;\n"
"")
        self.seebonusbutton.setObjectName("seebonusbutton")
        self.gridLayout_16.addWidget(self.seebonusbutton, 0, 1, 1, 1)
        self.verticalLayout_10.addWidget(self.frame_61)
        self.frame_62 = QtWidgets.QFrame(self.frame_60)
        self.frame_62.setStyleSheet("")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_62)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_16 = QtWidgets.QLabel(self.frame_62)
        self.label_16.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_16.setStyleSheet("")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_17.addWidget(self.label_16, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.frame_62)
        self.horizontalLayout_11.addWidget(self.frame_60)
        self.frame_63 = QtWidgets.QFrame(self.frame_58)
        self.frame_63.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.horizontalLayout_11.addWidget(self.frame_63)
        self.verticalLayout_7.addWidget(self.frame_58)
        self.frame_64 = QtWidgets.QFrame(self.frame_41)
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_64)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_65 = QtWidgets.QFrame(self.frame_64)
        self.frame_65.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.horizontalLayout_12.addWidget(self.frame_65)
        self.frame_66 = QtWidgets.QFrame(self.frame_64)
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_66)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_67 = QtWidgets.QFrame(self.frame_66)
        self.frame_67.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_67)
        self.gridLayout_18.setContentsMargins(0, 0, 9, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_17 = QtWidgets.QLabel(self.frame_67)
        self.label_17.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_17.setStyleSheet("")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout_18.addWidget(self.label_17, 0, 0, 1, 1)
        self.verticalLayout_11.addWidget(self.frame_67)
        self.frame_68 = QtWidgets.QFrame(self.frame_66)
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_68)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_68)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMaximumSize(QtCore.QSize(40, 33))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_68)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayout_11.addWidget(self.frame_68)
        self.horizontalLayout_12.addWidget(self.frame_66)
        self.frame_69 = QtWidgets.QFrame(self.frame_64)
        self.frame_69.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.horizontalLayout_12.addWidget(self.frame_69)
        self.verticalLayout_7.addWidget(self.frame_64)
        self.gridLayout_2.addWidget(self.frame_41, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_10)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setMaximumSize(QtCore.QSize(167, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.usercomboBox = QtWidgets.QComboBox(self.frame_12)
        self.usercomboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.usercomboBox.setStyleSheet("font: 13pt \"Britannic\";\n"
"background-color:rgb(39, 131, 163);\n"
"color:white;\n"
"")
        self.usercomboBox.setObjectName("usercomboBox")
        self.usercomboBox.addItem("")
        self.usercomboBox.addItem("")
        self.gridLayout_4.addWidget(self.usercomboBox, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_13)
        self.label_2.setStyleSheet("image:url(:/newPrefix/png-transparent-computer-icons-person-name-miscellaneous-computer-wallpaper-monochrome-thumbnail-removebg-preview.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_13)
        self.gridLayout_6.addWidget(self.frame_8, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_4.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setStyleSheet("QPushButton#pushButton{\n"
"border:2px solid black;\n"
"border-radius:20px;\n"
"color:white;\n"
"background-color:rgb(39, 131, 163);\n"
"font: 16pt \"Britannic Bold\";\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color:white;\n"
"color:rgb(39, 131, 163);\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_17)
        self.label_3.setStyleSheet("font: 70pt \"Britannic Bold\";\n"
"color:rgb(39, 131, 163);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_10.setContentsMargins(-1, 100, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton = QtWidgets.QPushButton(self.frame_18)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_16)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_2.addWidget(self.frame_19)
        self.horizontalLayout_4.addWidget(self.frame_16)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4.addWidget(self.frame_15)
        self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Order Delivered"))
        self.label_10.setText(_translate("Form", "Rider"))
        self.takeorderbutton.setText(_translate("Form", "Take Order"))
        self.viewassignedorderbutton.setText(_translate("Form", "View Assigned Orders"))
        self.viewroutebutton.setText(_translate("Form", "View Route"))
        self.orderdeliveredbutton.setText(_translate("Form", "Order Delivered"))
        self.seebonusbutton.setText(_translate("Form", "See Bonus"))
        self.usercomboBox.setItemText(0, _translate("Form", "Manager"))
        self.usercomboBox.setItemText(1, _translate("Form", "Logout"))
        self.label_3.setText(_translate("Form", "Map"))
        self.pushButton.setText(_translate("Form", "View Route"))
        self.pushButton.clicked.connect(self.route)
        
    def route(self):
        ox.config(log_console=True, use_cache=True)
        # define the start and end locations in latlng
        start_latlng = (31.580143741276306, 74.35631829777687)
        end_latlng = (31.57159075213314, 74.3094038512588)
        end_latlng2 = (31.5881278522699, 74.31065454413614)
        end_latlng3 = (31.575282909832463, 74.38045653979057)
        # location where you want to find your route
        # find shortest route based on the mode of travel
        mode      = 'bike'        # 'drive', 'bike', 'walk'
        # find shortest path based on distance or time
        optimizer = 'length'        # 'length','time'
        # create graph from OSM within the boundaries of some 
        # geocodable place(s)
        graph = ox.graph_from_point((31.5204,74.3587) , dist = 15000, network_type = mode,simplify=False)
        # find the nearest node to the start location
        G = ox.add_edge_speeds(graph)
        G = ox.add_edge_travel_times(graph)           
        
        orig_node = ox.nearest_nodes(graph, 74.35631829777687 , 31.580143741276306)
        start_marker = folium.Marker(
                location = start_latlng,
                popup = "<i>Bashahi mosque</i>",
                icon = folium.Icon(color='green'))
        # find the nearest node to the end location

        dest_node = ox.nearest_nodes(graph, 74.3094038512588 , 31.57159075213314)
        end_marker = folium.Marker(
                location = end_latlng,
                popup = "<i>Mall</i>",
                icon = folium.Icon(color='red'))
        
        
        dest_node2 = ox.nearest_nodes(graph, 74.31065454413614 , 31.5881278522699)
        end_marker2 = folium.Marker(
                location = end_latlng2,
                popup = "<i>Puict</i>",
                icon = folium.Icon(color='red'))
        
        dest_node3 = ox.nearest_nodes(graph, 74.38045653979057 , 31.575282909832463)
        end_marker3 = folium.Marker(
                location = end_latlng3,
                popup = "<i>Shalimar</i>",
                icon = folium.Icon(color='red'))

        # shortest_route = tc.shortest_path(G, orig_node, dest_node)
        
        shortest_route1 = ox.shortest_path(graph,
                                        orig_node,
                                        dest_node,
                                        weight=None)
        
        shortest_route2 = ox.shortest_path(graph,
                                        orig_node,
                                        dest_node2,
                                        weight='travel_time')
        
        shortest_route3 = ox.shortest_path(graph,
                                        orig_node,
                                        dest_node3,
                                        weight='travel_time')
        
        shortest_route_map = ox.plot_route_folium(graph, shortest_route1 ,route_color='#ff0000', opacity=0.5 , zoom=50)
        shortest_route_map = ox.plot_route_folium(graph, shortest_route2 ,route_map = shortest_route_map ,route_color='#0000ff', opacity=0.5)
        shortest_route_map = ox.plot_route_folium(graph, shortest_route3 ,route_map = shortest_route_map ,route_color='#00bbff', opacity=0.5)
        start_marker.add_to(shortest_route_map)
        end_marker.add_to(shortest_route_map)
        end_marker2.add_to(shortest_route_map)
        end_marker3.add_to(shortest_route_map)
        
        folium.TileLayer('openstreetmap').add_to(shortest_route_map)
        folium.LayerControl().add_to(shortest_route_map)
        
        shortest_route_map.save("last.html")
        webbrowser.open_new_tab("last.html")
        
import images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
