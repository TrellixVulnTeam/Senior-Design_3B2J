# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogDismissal_v4.ui'
#
# Created: Fri Mar  9 08:35:39 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dismissal(object):
    def setupUi(self, Dismissal):
        Dismissal.setObjectName(_fromUtf8("Dismissal"))
        Dismissal.resize(951, 652)
        self.LogButton_Generate = QtGui.QPushButton(Dismissal)
        self.LogButton_Generate.setGeometry(QtCore.QRect(360, 560, 75, 23))
        self.LogButton_Generate.setMaximumSize(QtCore.QSize(1200, 900))
        self.LogButton_Generate.setObjectName(_fromUtf8("LogButton_Generate"))
        self.EndDateEdit = QtGui.QDateEdit(Dismissal)
        self.EndDateEdit.setGeometry(QtCore.QRect(180, 560, 110, 22))
        self.EndDateEdit.setMaximumSize(QtCore.QSize(1200, 900))
        self.EndDateEdit.setObjectName(_fromUtf8("EndDateEdit"))
        self.LogButton_Exit = QtGui.QPushButton(Dismissal)
        self.LogButton_Exit.setGeometry(QtCore.QRect(710, 560, 75, 23))
        self.LogButton_Exit.setMaximumSize(QtCore.QSize(1200, 900))
        self.LogButton_Exit.setObjectName(_fromUtf8("LogButton_Exit"))
        self.StartDateEdit = QtGui.QDateEdit(Dismissal)
        self.StartDateEdit.setGeometry(QtCore.QRect(10, 560, 110, 22))
        self.StartDateEdit.setMaximumSize(QtCore.QSize(1200, 900))
        self.StartDateEdit.setObjectName(_fromUtf8("StartDateEdit"))
        self.LogLabel_Title = QtGui.QLabel(Dismissal)
        self.LogLabel_Title.setGeometry(QtCore.QRect(310, 20, 251, 51))
        self.LogLabel_Title.setMaximumSize(QtCore.QSize(1200, 900))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.LogLabel_Title.setFont(font)
        self.LogLabel_Title.setObjectName(_fromUtf8("LogLabel_Title"))
        self.LogLabel_Start = QtGui.QLabel(Dismissal)
        self.LogLabel_Start.setGeometry(QtCore.QRect(20, 540, 61, 21))
        self.LogLabel_Start.setMaximumSize(QtCore.QSize(1200, 900))
        self.LogLabel_Start.setObjectName(_fromUtf8("LogLabel_Start"))
        self.LogLabel_End = QtGui.QLabel(Dismissal)
        self.LogLabel_End.setGeometry(QtCore.QRect(190, 540, 61, 21))
        self.LogLabel_End.setMaximumSize(QtCore.QSize(1200, 900))
        self.LogLabel_End.setObjectName(_fromUtf8("LogLabel_End"))
        self.LogOffAdmin = QtGui.QCommandLinkButton(Dismissal)
        self.LogOffAdmin.setGeometry(QtCore.QRect(700, 10, 187, 41))
        self.LogOffAdmin.setMaximumSize(QtCore.QSize(1200, 900))
        self.LogOffAdmin.setObjectName(_fromUtf8("LogOffAdmin"))
        self.DismissWidget = QtGui.QTabWidget(Dismissal)
        self.DismissWidget.setGeometry(QtCore.QRect(10, 90, 781, 441))
        self.DismissWidget.setMaximumSize(QtCore.QSize(1200, 900))
        self.DismissWidget.setObjectName(_fromUtf8("DismissWidget"))
        self.GenericTab = QtGui.QWidget()
        self.GenericTab.setObjectName(_fromUtf8("GenericTab"))
        self.LogTreeView_Generic = QtGui.QTableView(self.GenericTab)
        self.LogTreeView_Generic.setGeometry(QtCore.QRect(0, 1, 781, 421))
        self.LogTreeView_Generic.setObjectName(_fromUtf8("LogTreeView_Generic"))
        self.DismissWidget.addTab(self.GenericTab, _fromUtf8(""))
        self.StudentTab = QtGui.QWidget()
        self.StudentTab.setObjectName(_fromUtf8("StudentTab"))
        self.LogStudentText_SearchName = QtGui.QTextEdit(self.StudentTab)
        self.LogStudentText_SearchName.setGeometry(QtCore.QRect(0, 390, 211, 31))
        self.LogStudentText_SearchName.setObjectName(_fromUtf8("LogStudentText_SearchName"))
        self.LogStudentText_SearchID = QtGui.QTextEdit(self.StudentTab)
        self.LogStudentText_SearchID.setGeometry(QtCore.QRect(220, 390, 181, 31))
        self.LogStudentText_SearchID.setObjectName(_fromUtf8("LogStudentText_SearchID"))
        self.LogTreeView_Student = QtGui.QTreeView(self.StudentTab)
        self.LogTreeView_Student.setGeometry(QtCore.QRect(398, 0, 381, 421))
        self.LogTreeView_Student.setObjectName(_fromUtf8("LogTreeView_Student"))
        self.LogListWidget_Student = QtGui.QListWidget(self.StudentTab)
        self.LogListWidget_Student.setGeometry(QtCore.QRect(-40, 0, 441, 361))
        self.LogListWidget_Student.setObjectName(_fromUtf8("LogListWidget_Student"))
        self.LogStudentLabel_SearchName = QtGui.QLabel(self.StudentTab)
        self.LogStudentLabel_SearchName.setGeometry(QtCore.QRect(0, 360, 101, 16))
        self.LogStudentLabel_SearchName.setObjectName(_fromUtf8("LogStudentLabel_SearchName"))
        self.LogStudentLogLabel_SearchID = QtGui.QLabel(self.StudentTab)
        self.LogStudentLogLabel_SearchID.setGeometry(QtCore.QRect(220, 360, 61, 16))
        self.LogStudentLogLabel_SearchID.setObjectName(_fromUtf8("LogStudentLogLabel_SearchID"))
        self.LogStudentButton_SearchName = QtGui.QPushButton(self.StudentTab)
        self.LogStudentButton_SearchName.setGeometry(QtCore.QRect(130, 360, 75, 23))
        self.LogStudentButton_SearchName.setObjectName(_fromUtf8("LogStudentButton_SearchName"))
        self.LogStudentButton_SearchID = QtGui.QPushButton(self.StudentTab)
        self.LogStudentButton_SearchID.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.LogStudentButton_SearchID.setObjectName(_fromUtf8("LogStudentButton_SearchID"))
        self.DismissWidget.addTab(self.StudentTab, _fromUtf8(""))
        self.StaffTab = QtGui.QWidget()
        self.StaffTab.setObjectName(_fromUtf8("StaffTab"))
        self.LogTableView_Staff = QtGui.QTableView(self.StaffTab)
        self.LogTableView_Staff.setGeometry(QtCore.QRect(398, 0, 381, 421))
        self.LogTableView_Staff.setObjectName(_fromUtf8("LogTableView_Staff"))
        self.LogListWidget_Staff = QtGui.QListWidget(self.StaffTab)
        self.LogListWidget_Staff.setGeometry(QtCore.QRect(-40, 0, 441, 361))
        self.LogListWidget_Staff.setObjectName(_fromUtf8("LogListWidget_Staff"))
        self.LogStaffText_SearchID = QtGui.QTextEdit(self.StaffTab)
        self.LogStaffText_SearchID.setGeometry(QtCore.QRect(220, 390, 181, 31))
        self.LogStaffText_SearchID.setObjectName(_fromUtf8("LogStaffText_SearchID"))
        self.LogStaffText_SearchName = QtGui.QTextEdit(self.StaffTab)
        self.LogStaffText_SearchName.setGeometry(QtCore.QRect(0, 390, 211, 31))
        self.LogStaffText_SearchName.setObjectName(_fromUtf8("LogStaffText_SearchName"))
        self.LogStaffLabel_SearchName = QtGui.QLabel(self.StaffTab)
        self.LogStaffLabel_SearchName.setGeometry(QtCore.QRect(0, 360, 101, 16))
        self.LogStaffLabel_SearchName.setObjectName(_fromUtf8("LogStaffLabel_SearchName"))
        self.LogStaffLabel_SearchID = QtGui.QLabel(self.StaffTab)
        self.LogStaffLabel_SearchID.setGeometry(QtCore.QRect(220, 360, 61, 16))
        self.LogStaffLabel_SearchID.setObjectName(_fromUtf8("LogStaffLabel_SearchID"))
        self.LogStaffButton_SearchName = QtGui.QPushButton(self.StaffTab)
        self.LogStaffButton_SearchName.setGeometry(QtCore.QRect(130, 360, 75, 23))
        self.LogStaffButton_SearchName.setObjectName(_fromUtf8("LogStaffButton_SearchName"))
        self.LogStaffButton_SearchId = QtGui.QPushButton(self.StaffTab)
        self.LogStaffButton_SearchId.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.LogStaffButton_SearchId.setObjectName(_fromUtf8("LogStaffButton_SearchId"))
        self.DismissWidget.addTab(self.StaffTab, _fromUtf8(""))

        self.retranslateUi(Dismissal)
        self.DismissWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dismissal)

    def retranslateUi(self, Dismissal):
        Dismissal.setWindowTitle(_translate("Dismissal", "Dialog", None))
        self.LogButton_Generate.setText(_translate("Dismissal", "Generate", None))
        self.LogButton_Exit.setText(_translate("Dismissal", "Exit", None))
        self.LogLabel_Title.setText(_translate("Dismissal", "Dismissal Log", None))
        self.LogLabel_Start.setText(_translate("Dismissal", "Start Date", None))
        self.LogLabel_End.setText(_translate("Dismissal", "End Date", None))
        self.LogOffAdmin.setText(_translate("Dismissal", "Log Off", None))
        self.DismissWidget.setTabText(self.DismissWidget.indexOf(self.GenericTab), _translate("Dismissal", "Generic Report", None))
        self.LogStudentLabel_SearchName.setText(_translate("Dismissal", "Search Name:", None))
        self.LogStudentLogLabel_SearchID.setText(_translate("Dismissal", "Search ID:", None))
        self.LogStudentButton_SearchName.setText(_translate("Dismissal", "Search", None))
        self.LogStudentButton_SearchID.setText(_translate("Dismissal", "Search", None))
        self.DismissWidget.setTabText(self.DismissWidget.indexOf(self.StudentTab), _translate("Dismissal", "Student Report", None))
        self.LogStaffLabel_SearchName.setText(_translate("Dismissal", "Search Name:", None))
        self.LogStaffLabel_SearchID.setText(_translate("Dismissal", "Search ID:", None))
        self.LogStaffButton_SearchName.setText(_translate("Dismissal", "Search", None))
        self.LogStaffButton_SearchId.setText(_translate("Dismissal", "Search", None))
        self.DismissWidget.setTabText(self.DismissWidget.indexOf(self.StaffTab), _translate("Dismissal", "Staff Report", None))
