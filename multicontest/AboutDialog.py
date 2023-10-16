# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)
from multicontest import resources_rc

class Ui_about_dialog(object):
    def setupUi(self, about_dialog):
        if not about_dialog.objectName():
            about_dialog.setObjectName(u"about_dialog")
        about_dialog.resize(653, 374)
        about_dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        about_dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(about_dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(10, -1, 10, 10)
        self.info_layout = QVBoxLayout()
#ifndef Q_OS_MAC
        self.info_layout.setSpacing(-1)
#endif
        self.info_layout.setObjectName(u"info_layout")
        self.logo_layout = QHBoxLayout()
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_btn = QToolButton(about_dialog)
        self.logo_btn.setObjectName(u"logo_btn")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.logo_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/multicontest_icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QSize(100, 100))
        self.logo_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.logo_layout.addWidget(self.logo_btn)


        self.info_layout.addLayout(self.logo_layout)

        self.version_label = QLabel(about_dialog)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.version_label)

        self.copyright_label = QLabel(about_dialog)
        self.copyright_label.setObjectName(u"copyright_label")
        font1 = QFont()
        font1.setBold(True)
        self.copyright_label.setFont(font1)

        self.info_layout.addWidget(self.copyright_label)


        self.main_layout.addLayout(self.info_layout)

        self.license_tab_layout = QTabWidget(about_dialog)
        self.license_tab_layout.setObjectName(u"license_tab_layout")
        self.license_tab = QWidget()
        self.license_tab.setObjectName(u"license_tab")
        self.verticalLayout_3 = QVBoxLayout(self.license_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 5, 1, 0)
        self.license_text = QTextBrowser(self.license_tab)
        self.license_text.setObjectName(u"license_text")
        self.license_text.setFrameShape(QFrame.Box)
        self.license_text.setFrameShadow(QFrame.Plain)
        self.license_text.setLineWidth(0)
        self.license_text.setOverwriteMode(True)
        self.license_text.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.license_text)

        self.license_tab_layout.addTab(self.license_tab, "")
        self.opensource_tab = QWidget()
        self.opensource_tab.setObjectName(u"opensource_tab")
        self.verticalLayout_4 = QVBoxLayout(self.opensource_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 5, 1, 0)
        self.opensource_text = QTextBrowser(self.opensource_tab)
        self.opensource_text.setObjectName(u"opensource_text")
        self.opensource_text.setFrameShape(QFrame.Box)
        self.opensource_text.setFrameShadow(QFrame.Raised)
        self.opensource_text.setLineWidth(0)
        self.opensource_text.setMarkdown(u"")
        self.opensource_text.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.opensource_text.setOverwriteMode(True)
        self.opensource_text.setOpenExternalLinks(True)

        self.verticalLayout_4.addWidget(self.opensource_text)

        self.license_tab_layout.addTab(self.opensource_tab, "")

        self.main_layout.addWidget(self.license_tab_layout)

        self.main_layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.main_layout)

        self.buttons_layout = QFrame(about_dialog)
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.buttons_layout.setFrameShape(QFrame.StyledPanel)
        self.buttons_layout.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_layout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, 10)
        self.website_btn = QPushButton(self.buttons_layout)
        self.website_btn.setObjectName(u"website_btn")
        self.website_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.website_btn)

        self.doc_btn = QPushButton(self.buttons_layout)
        self.doc_btn.setObjectName(u"doc_btn")
        self.doc_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.doc_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.buttons_layout)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.buttons_layout)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(about_dialog)

        self.license_tab_layout.setCurrentIndex(0)
        self.close_btn.setDefault(True)


        QMetaObject.connectSlotsByName(about_dialog)
    # setupUi

    def retranslateUi(self, about_dialog):
        about_dialog.setWindowTitle(QCoreApplication.translate("about_dialog", u"Dialog", None))
        self.logo_btn.setText(QCoreApplication.translate("about_dialog", u"MultiConTest", None))
        self.version_label.setText(QCoreApplication.translate("about_dialog", u"Version 1.0", None))
        self.copyright_label.setText(QCoreApplication.translate("about_dialog", u"<html><head/><body><p align=\"center\">Copyright \u00a9 2023</p><p align=\"center\">University of T\u00fcbingen</p><p align=\"center\">Nicolas Kersten</p></body></html>", None))
        self.license_tab_layout.setTabText(self.license_tab_layout.indexOf(self.license_tab), QCoreApplication.translate("about_dialog", u"License", None))
        self.license_tab_layout.setTabText(self.license_tab_layout.indexOf(self.opensource_tab), QCoreApplication.translate("about_dialog", u"Included open-source software", None))
        self.website_btn.setText(QCoreApplication.translate("about_dialog", u"Website", None))
        self.doc_btn.setText(QCoreApplication.translate("about_dialog", u"Documentation", None))
        self.close_btn.setText(QCoreApplication.translate("about_dialog", u"Close", None))
    # retranslateUi

