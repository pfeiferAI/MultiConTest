# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
from multicontest import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 597)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.action_export_test_result = QAction(MainWindow)
        self.action_export_test_result.setObjectName(u"action_export_test_result")
        self.action_export_all_results = QAction(MainWindow)
        self.action_export_all_results.setObjectName(u"action_export_all_results")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_method_description = QAction(MainWindow)
        self.action_method_description.setObjectName(u"action_method_description")
        self.action_clear_all = QAction(MainWindow)
        self.action_clear_all.setObjectName(u"action_clear_all")
        self.action_software_description = QAction(MainWindow)
        self.action_software_description.setObjectName(u"action_software_description")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.cls_tab = QWidget()
        self.cls_tab.setObjectName(u"cls_tab")
        self.verticalLayout = QVBoxLayout(self.cls_tab)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 10, 5, 5)
        self.cls_header_layout = QHBoxLayout()
        self.cls_header_layout.setObjectName(u"cls_header_layout")
        self.cls_file_text = QLabel(self.cls_tab)
        self.cls_file_text.setObjectName(u"cls_file_text")
        self.cls_file_text.setWordWrap(True)

        self.cls_header_layout.addWidget(self.cls_file_text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.cls_header_layout.addItem(self.horizontalSpacer)

        self.generate_clustering_btn = QPushButton(self.cls_tab)
        self.generate_clustering_btn.setObjectName(u"generate_clustering_btn")
        self.generate_clustering_btn.setEnabled(True)

        self.cls_header_layout.addWidget(self.generate_clustering_btn)

        self.select_cls_file = QPushButton(self.cls_tab)
        self.select_cls_file.setObjectName(u"select_cls_file")

        self.cls_header_layout.addWidget(self.select_cls_file)


        self.verticalLayout.addLayout(self.cls_header_layout)

        self.cls_details_frame = QFrame(self.cls_tab)
        self.cls_details_frame.setObjectName(u"cls_details_frame")
        self.cls_details_frame.setFrameShape(QFrame.Box)
        self.cls_details_layout = QHBoxLayout(self.cls_details_frame)
        self.cls_details_layout.setObjectName(u"cls_details_layout")
        self.cls_preview_layout = QVBoxLayout()
        self.cls_preview_layout.setObjectName(u"cls_preview_layout")
        self.cls_preview_lbl = QLabel(self.cls_details_frame)
        self.cls_preview_lbl.setObjectName(u"cls_preview_lbl")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.cls_preview_lbl.setFont(font)

        self.cls_preview_layout.addWidget(self.cls_preview_lbl)

        self.cls_unique_table = QTableView(self.cls_details_frame)
        self.cls_unique_table.setObjectName(u"cls_unique_table")
        self.cls_unique_table.setFrameShape(QFrame.Box)
        self.cls_unique_table.setFrameShadow(QFrame.Plain)
        self.cls_unique_table.setLineWidth(0)
        self.cls_unique_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.cls_preview_layout.addWidget(self.cls_unique_table)


        self.cls_details_layout.addLayout(self.cls_preview_layout)

        self.cls_table_layout = QVBoxLayout()
        self.cls_table_layout.setObjectName(u"cls_table_layout")
        self.cls_table_lbl = QLabel(self.cls_details_frame)
        self.cls_table_lbl.setObjectName(u"cls_table_lbl")
        self.cls_table_lbl.setFont(font)

        self.cls_table_layout.addWidget(self.cls_table_lbl)

        self.cls_table = QTableView(self.cls_details_frame)
        self.cls_table.setObjectName(u"cls_table")
        self.cls_table.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.cls_table.setFrameShape(QFrame.Box)
        self.cls_table.setFrameShadow(QFrame.Plain)
        self.cls_table.setLineWidth(0)
        self.cls_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.cls_table_layout.addWidget(self.cls_table)


        self.cls_details_layout.addLayout(self.cls_table_layout)


        self.verticalLayout.addWidget(self.cls_details_frame)

        self.tabWidget.addTab(self.cls_tab, "")
        self.label_tab = QWidget()
        self.label_tab.setObjectName(u"label_tab")
        self.verticalLayout_10 = QVBoxLayout(self.label_tab)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 10, 5, 5)
        self.labels_header_layout = QHBoxLayout()
        self.labels_header_layout.setSpacing(5)
        self.labels_header_layout.setObjectName(u"labels_header_layout")
        self.label_file_txt = QLabel(self.label_tab)
        self.label_file_txt.setObjectName(u"label_file_txt")
        self.label_file_txt.setWordWrap(True)

        self.labels_header_layout.addWidget(self.label_file_txt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.labels_header_layout.addItem(self.horizontalSpacer_2)

        self.import_labels_btn = QPushButton(self.label_tab)
        self.import_labels_btn.setObjectName(u"import_labels_btn")

        self.labels_header_layout.addWidget(self.import_labels_btn)

        self.advanced_label_settings_btn = QPushButton(self.label_tab)
        self.advanced_label_settings_btn.setObjectName(u"advanced_label_settings_btn")

        self.labels_header_layout.addWidget(self.advanced_label_settings_btn)


        self.verticalLayout_10.addLayout(self.labels_header_layout)

        self.cat_advanced_frame = QFrame(self.label_tab)
        self.cat_advanced_frame.setObjectName(u"cat_advanced_frame")
        self.cat_advanced_frame.setFrameShape(QFrame.Box)
        self.cat_advanced_frame.setFrameShadow(QFrame.Plain)
        self.cat_advanced_frame.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.cat_advanced_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.drop_missing_check = QCheckBox(self.cat_advanced_frame)
        self.drop_missing_check.setObjectName(u"drop_missing_check")
        self.drop_missing_check.setChecked(True)

        self.horizontalLayout_6.addWidget(self.drop_missing_check)

        self.category_settings_layout = QVBoxLayout()
        self.category_settings_layout.setSpacing(5)
        self.category_settings_layout.setObjectName(u"category_settings_layout")
        self.category_count_label = QLabel(self.cat_advanced_frame)
        self.category_count_label.setObjectName(u"category_count_label")

        self.category_settings_layout.addWidget(self.category_count_label)

        self.category_count_layout = QHBoxLayout()
        self.category_count_layout.setSpacing(10)
        self.category_count_layout.setObjectName(u"category_count_layout")
        self.category_count_spin = QSpinBox(self.cat_advanced_frame)
        self.category_count_spin.setObjectName(u"category_count_spin")
        self.category_count_spin.setMinimum(2)
        self.category_count_spin.setMaximum(20)
        self.category_count_spin.setValue(10)

        self.category_count_layout.addWidget(self.category_count_spin)

        self.refine_cat_count_btn = QPushButton(self.cat_advanced_frame)
        self.refine_cat_count_btn.setObjectName(u"refine_cat_count_btn")

        self.category_count_layout.addWidget(self.refine_cat_count_btn)

        self.category_count_layout.setStretch(0, 2)
        self.category_count_layout.setStretch(1, 1)

        self.category_settings_layout.addLayout(self.category_count_layout)


        self.horizontalLayout_6.addLayout(self.category_settings_layout)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_10.addWidget(self.cat_advanced_frame)

        self.label_selection_frame = QFrame(self.label_tab)
        self.label_selection_frame.setObjectName(u"label_selection_frame")
        self.label_selection_frame.setFrameShape(QFrame.Box)
        self.verticalLayout_11 = QVBoxLayout(self.label_selection_frame)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.labels_table_layout = QVBoxLayout()
        self.labels_table_layout.setSpacing(3)
        self.labels_table_layout.setObjectName(u"labels_table_layout")
        self.labels_table_head_layout = QHBoxLayout()
        self.labels_table_head_layout.setObjectName(u"labels_table_head_layout")
        self.labels_preview_lbl = QLabel(self.label_selection_frame)
        self.labels_preview_lbl.setObjectName(u"labels_preview_lbl")
        self.labels_preview_lbl.setFont(font)

        self.labels_table_head_layout.addWidget(self.labels_preview_lbl)

        self.sort_frame = QFrame(self.label_selection_frame)
        self.sort_frame.setObjectName(u"sort_frame")
        self.sort_frame.setFrameShape(QFrame.NoFrame)
        self.sort_frame.setFrameShadow(QFrame.Plain)
        self.sort_frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.sort_frame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.sort_labels_lbl = QLabel(self.sort_frame)
        self.sort_labels_lbl.setObjectName(u"sort_labels_lbl")

        self.horizontalLayout_3.addWidget(self.sort_labels_lbl)

        self.sort_up_btn = QPushButton(self.sort_frame)
        self.sort_up_btn.setObjectName(u"sort_up_btn")

        self.horizontalLayout_3.addWidget(self.sort_up_btn)

        self.sort_down_btn = QPushButton(self.sort_frame)
        self.sort_down_btn.setObjectName(u"sort_down_btn")

        self.horizontalLayout_3.addWidget(self.sort_down_btn)


        self.labels_table_head_layout.addWidget(self.sort_frame)

        self.query_field = QLineEdit(self.label_selection_frame)
        self.query_field.setObjectName(u"query_field")
        self.query_field.setClearButtonEnabled(True)

        self.labels_table_head_layout.addWidget(self.query_field)

        self.find_cat_btn = QPushButton(self.label_selection_frame)
        self.find_cat_btn.setObjectName(u"find_cat_btn")

        self.labels_table_head_layout.addWidget(self.find_cat_btn)

        self.labels_table_head_layout.setStretch(0, 1)
        self.labels_table_head_layout.setStretch(2, 1)

        self.labels_table_layout.addLayout(self.labels_table_head_layout)

        self.label_table = QTableView(self.label_selection_frame)
        self.label_table.setObjectName(u"label_table")
        self.label_table.setFrameShape(QFrame.Box)
        self.label_table.setFrameShadow(QFrame.Plain)
        self.label_table.setLineWidth(0)
        self.label_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.label_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.label_table.horizontalHeader().setHighlightSections(False)

        self.labels_table_layout.addWidget(self.label_table)

        self.labels_table_layout.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.labels_table_layout)

        self.line = QFrame(self.label_selection_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line)

        self.label_overlap_layout = QGridLayout()
        self.label_overlap_layout.setObjectName(u"label_overlap_layout")
        self.label_overlap_layout.setHorizontalSpacing(10)
        self.label_overlap_layout.setVerticalSpacing(0)
        self.sel_overlap_txt = QLabel(self.label_selection_frame)
        self.sel_overlap_txt.setObjectName(u"sel_overlap_txt")

        self.label_overlap_layout.addWidget(self.sel_overlap_txt, 0, 4, 1, 1)

        self.sel_overlap_lbl = QLabel(self.label_selection_frame)
        self.sel_overlap_lbl.setObjectName(u"sel_overlap_lbl")

        self.label_overlap_layout.addWidget(self.sel_overlap_lbl, 0, 3, 1, 1)

        self.overlap_txt = QLabel(self.label_selection_frame)
        self.overlap_txt.setObjectName(u"overlap_txt")

        self.label_overlap_layout.addWidget(self.overlap_txt, 0, 2, 1, 1)

        self.sample_overlap_lbl = QLabel(self.label_selection_frame)
        self.sample_overlap_lbl.setObjectName(u"sample_overlap_lbl")

        self.label_overlap_layout.addWidget(self.sample_overlap_lbl, 0, 0, 1, 1)

        self.overlap_lbl = QLabel(self.label_selection_frame)
        self.overlap_lbl.setObjectName(u"overlap_lbl")

        self.label_overlap_layout.addWidget(self.overlap_lbl, 0, 1, 1, 1)

        self.label_overlap_layout.setColumnStretch(0, 2)
        self.label_overlap_layout.setColumnStretch(1, 1)
        self.label_overlap_layout.setColumnStretch(2, 1)
        self.label_overlap_layout.setColumnStretch(3, 1)
        self.label_overlap_layout.setColumnStretch(4, 1)

        self.verticalLayout_11.addLayout(self.label_overlap_layout)


        self.verticalLayout_10.addWidget(self.label_selection_frame)

        self.verticalLayout_10.setStretch(2, 1)
        self.tabWidget.addTab(self.label_tab, "")
        self.conf_tab = QWidget()
        self.conf_tab.setObjectName(u"conf_tab")
        self.verticalLayout_5 = QVBoxLayout(self.conf_tab)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 10, 5, 5)
        self.conf_warning_frame = QFrame(self.conf_tab)
        self.conf_warning_frame.setObjectName(u"conf_warning_frame")
        self.conf_warning_frame.setFrameShape(QFrame.WinPanel)
        self.conf_warning_layout = QHBoxLayout(self.conf_warning_frame)
        self.conf_warning_layout.setObjectName(u"conf_warning_layout")
        self.conf_warning_txt = QLabel(self.conf_warning_frame)
        self.conf_warning_txt.setObjectName(u"conf_warning_txt")

        self.conf_warning_layout.addWidget(self.conf_warning_txt)


        self.verticalLayout_5.addWidget(self.conf_warning_frame)

        self.conf_factor_layout = QHBoxLayout()
        self.conf_factor_layout.setSpacing(10)
        self.conf_factor_layout.setObjectName(u"conf_factor_layout")
        self.conf_factor_lbl = QLabel(self.conf_tab)
        self.conf_factor_lbl.setObjectName(u"conf_factor_lbl")
        self.conf_factor_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.conf_factor_layout.addWidget(self.conf_factor_lbl)

        self.conf_factor_txt = QLabel(self.conf_tab)
        self.conf_factor_txt.setObjectName(u"conf_factor_txt")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.conf_factor_txt.setFont(font1)
        self.conf_factor_txt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.conf_factor_txt.setWordWrap(True)

        self.conf_factor_layout.addWidget(self.conf_factor_txt)

        self.conf_factor_layout.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.conf_factor_layout)

        self.conf_p_lbl_layout = QHBoxLayout()
        self.conf_p_lbl_layout.setSpacing(10)
        self.conf_p_lbl_layout.setObjectName(u"conf_p_lbl_layout")
        self.conf_tab_widget = QTabWidget(self.conf_tab)
        self.conf_tab_widget.setObjectName(u"conf_tab_widget")
        self.conf_tab_widget.setTabPosition(QTabWidget.South)
        self.vis_tab = QWidget()
        self.vis_tab.setObjectName(u"vis_tab")
        self.verticalLayout_3 = QVBoxLayout(self.vis_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.conf_vis_widget = QWidget(self.vis_tab)
        self.conf_vis_widget.setObjectName(u"conf_vis_widget")

        self.verticalLayout_3.addWidget(self.conf_vis_widget)

        self.conf_tab_widget.addTab(self.vis_tab, "")
        self.cont_tab = QWidget()
        self.cont_tab.setObjectName(u"cont_tab")
        self.verticalLayout_4 = QVBoxLayout(self.cont_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.cont_table = QTableView(self.cont_tab)
        self.cont_table.setObjectName(u"cont_table")
        self.cont_table.setFrameShape(QFrame.Box)
        self.cont_table.setFrameShadow(QFrame.Plain)
        self.cont_table.setLineWidth(0)
        self.cont_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_4.addWidget(self.cont_table)

        self.conf_tab_widget.addTab(self.cont_tab, "")

        self.conf_p_lbl_layout.addWidget(self.conf_tab_widget)

        self.conf_result_layout = QVBoxLayout()
        self.conf_result_layout.setObjectName(u"conf_result_layout")
        self.conf_p_val_frame = QFrame(self.conf_tab)
        self.conf_p_val_frame.setObjectName(u"conf_p_val_frame")
        self.conf_p_val_frame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.conf_p_val_frame.setFrameShape(QFrame.Panel)
        self.conf_p_val_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.conf_p_val_frame)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.conf_p_val_txt = QLabel(self.conf_p_val_frame)
        self.conf_p_val_txt.setObjectName(u"conf_p_val_txt")
        self.conf_p_val_txt.setFont(font1)
        self.conf_p_val_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.conf_p_val_txt)

        self.conf_p_val_lbl = QLabel(self.conf_p_val_frame)
        self.conf_p_val_lbl.setObjectName(u"conf_p_val_lbl")
        self.conf_p_val_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.conf_p_val_lbl)

        self.conf_compute_btn = QPushButton(self.conf_p_val_frame)
        self.conf_compute_btn.setObjectName(u"conf_compute_btn")

        self.verticalLayout_17.addWidget(self.conf_compute_btn)

        self.p_val_details_btn = QPushButton(self.conf_p_val_frame)
        self.p_val_details_btn.setObjectName(u"p_val_details_btn")

        self.verticalLayout_17.addWidget(self.p_val_details_btn)

        self.export_single_result_btn = QPushButton(self.conf_p_val_frame)
        self.export_single_result_btn.setObjectName(u"export_single_result_btn")

        self.verticalLayout_17.addWidget(self.export_single_result_btn)


        self.conf_result_layout.addWidget(self.conf_p_val_frame)

        self.orig_p_val_frame = QFrame(self.conf_tab)
        self.orig_p_val_frame.setObjectName(u"orig_p_val_frame")
        self.orig_p_val_frame.setFrameShape(QFrame.Panel)
        self.orig_p_val_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_16 = QVBoxLayout(self.orig_p_val_frame)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.orig_p_txt = QLabel(self.orig_p_val_frame)
        self.orig_p_txt.setObjectName(u"orig_p_txt")
        self.orig_p_txt.setFont(font1)
        self.orig_p_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.orig_p_txt)

        self.orig_p_lbl = QLabel(self.orig_p_val_frame)
        self.orig_p_lbl.setObjectName(u"orig_p_lbl")
        self.orig_p_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.orig_p_lbl)


        self.conf_result_layout.addWidget(self.orig_p_val_frame)

        self.perm_frame = QFrame(self.conf_tab)
        self.perm_frame.setObjectName(u"perm_frame")
        self.perm_frame.setFrameShape(QFrame.Panel)
        self.perm_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_18 = QVBoxLayout(self.perm_frame)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(3, 3, 3, 3)
        self.failed_perm_txt = QLabel(self.perm_frame)
        self.failed_perm_txt.setObjectName(u"failed_perm_txt")
        self.failed_perm_txt.setFont(font1)
        self.failed_perm_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.failed_perm_txt)

        self.failed_perm_lbl = QLabel(self.perm_frame)
        self.failed_perm_lbl.setObjectName(u"failed_perm_lbl")
        self.failed_perm_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.failed_perm_lbl)


        self.conf_result_layout.addWidget(self.perm_frame)

        self.perm_frame_warning = QFrame(self.conf_tab)
        self.perm_frame_warning.setObjectName(u"perm_frame_warning")
        self.perm_frame_warning.setFrameShape(QFrame.WinPanel)
        self.perm_frame_warning.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.perm_frame_warning)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.failed_perm_txt_warning = QLabel(self.perm_frame_warning)
        self.failed_perm_txt_warning.setObjectName(u"failed_perm_txt_warning")
        self.failed_perm_txt_warning.setFont(font1)
        self.failed_perm_txt_warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.failed_perm_txt_warning)

        self.failed_perm_lbl_warning = QLabel(self.perm_frame_warning)
        self.failed_perm_lbl_warning.setObjectName(u"failed_perm_lbl_warning")
        self.failed_perm_lbl_warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.failed_perm_lbl_warning)


        self.conf_result_layout.addWidget(self.perm_frame_warning)

        self.conf_result_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.conf_result_layout.addItem(self.conf_result_spacer)

        self.progress_bar = QProgressBar(self.conf_tab)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)

        self.conf_result_layout.addWidget(self.progress_bar)


        self.conf_p_lbl_layout.addLayout(self.conf_result_layout)

        self.conf_p_lbl_layout.setStretch(0, 3)
        self.conf_p_lbl_layout.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.conf_p_lbl_layout)

        self.tabWidget.addTab(self.conf_tab, "")
        self.results_tab = QWidget()
        self.results_tab.setObjectName(u"results_tab")
        self.verticalLayout_7 = QVBoxLayout(self.results_tab)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 10, 5, 5)
        self.results_layout = QHBoxLayout()
        self.results_layout.setObjectName(u"results_layout")
        self.multiple_testing_warning = QLabel(self.results_tab)
        self.multiple_testing_warning.setObjectName(u"multiple_testing_warning")

        self.results_layout.addWidget(self.multiple_testing_warning)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.results_layout.addItem(self.horizontalSpacer_3)

        self.export_all_results_btn = QPushButton(self.results_tab)
        self.export_all_results_btn.setObjectName(u"export_all_results_btn")

        self.results_layout.addWidget(self.export_all_results_btn)


        self.verticalLayout_7.addLayout(self.results_layout)

        self.results_table = QTableView(self.results_tab)
        self.results_table.setObjectName(u"results_table")
        self.results_table.setFrameShape(QFrame.Box)
        self.results_table.setFrameShadow(QFrame.Plain)
        self.results_table.setLineWidth(0)
        self.results_table.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_7.addWidget(self.results_table)

        self.verticalLayout_7.setStretch(1, 1)
        self.tabWidget.addTab(self.results_tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.data_overview_frame = QFrame(self.centralwidget)
        self.data_overview_frame.setObjectName(u"data_overview_frame")
        self.data_overview_frame.setFrameShape(QFrame.StyledPanel)
        self.data_overview_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.data_overview_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 5, -1, 5)
        self.sample_count_frame = QFrame(self.data_overview_frame)
        self.sample_count_frame.setObjectName(u"sample_count_frame")
        self.sample_count_frame.setFrameShape(QFrame.Panel)
        self.sample_count_frame.setFrameShadow(QFrame.Plain)
        self.sample_count_frame.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.sample_count_frame)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.sample_count_txt = QLabel(self.sample_count_frame)
        self.sample_count_txt.setObjectName(u"sample_count_txt")
        self.sample_count_txt.setFont(font1)
        self.sample_count_txt.setLayoutDirection(Qt.LeftToRight)
        self.sample_count_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.sample_count_txt)

        self.sample_count_lbl = QLabel(self.sample_count_frame)
        self.sample_count_lbl.setObjectName(u"sample_count_lbl")
        self.sample_count_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.sample_count_lbl)


        self.horizontalLayout_9.addWidget(self.sample_count_frame)

        self.cluster_count_frame = QFrame(self.data_overview_frame)
        self.cluster_count_frame.setObjectName(u"cluster_count_frame")
        self.cluster_count_frame.setFrameShape(QFrame.Panel)
        self.cluster_count_frame.setFrameShadow(QFrame.Plain)
        self.cluster_count_frame.setLineWidth(1)
        self.verticalLayout_8 = QVBoxLayout(self.cluster_count_frame)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.cluster_count_txt = QLabel(self.cluster_count_frame)
        self.cluster_count_txt.setObjectName(u"cluster_count_txt")
        self.cluster_count_txt.setFont(font1)
        self.cluster_count_txt.setLayoutDirection(Qt.LeftToRight)
        self.cluster_count_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cluster_count_txt)

        self.cluster_count_lbl = QLabel(self.cluster_count_frame)
        self.cluster_count_lbl.setObjectName(u"cluster_count_lbl")
        self.cluster_count_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.cluster_count_lbl)


        self.horizontalLayout_9.addWidget(self.cluster_count_frame)

        self.label_count_frame = QFrame(self.data_overview_frame)
        self.label_count_frame.setObjectName(u"label_count_frame")
        self.label_count_frame.setFrameShape(QFrame.Panel)
        self.label_count_frame.setFrameShadow(QFrame.Plain)
        self.label_count_frame.setLineWidth(1)
        self.verticalLayout_9 = QVBoxLayout(self.label_count_frame)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.label_count_txt = QLabel(self.label_count_frame)
        self.label_count_txt.setObjectName(u"label_count_txt")
        self.label_count_txt.setFont(font1)
        self.label_count_txt.setLayoutDirection(Qt.LeftToRight)
        self.label_count_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_count_txt)

        self.label_count_lbl = QLabel(self.label_count_frame)
        self.label_count_lbl.setObjectName(u"label_count_lbl")
        self.label_count_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_count_lbl)


        self.horizontalLayout_9.addWidget(self.label_count_frame)

        self.cat_label_frame = QFrame(self.data_overview_frame)
        self.cat_label_frame.setObjectName(u"cat_label_frame")
        self.cat_label_frame.setFrameShape(QFrame.Panel)
        self.cat_label_frame.setFrameShadow(QFrame.Plain)
        self.cat_label_frame.setLineWidth(1)
        self.verticalLayout_13 = QVBoxLayout(self.cat_label_frame)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.cat_label_txt = QLabel(self.cat_label_frame)
        self.cat_label_txt.setObjectName(u"cat_label_txt")
        self.cat_label_txt.setFont(font1)
        self.cat_label_txt.setLayoutDirection(Qt.LeftToRight)
        self.cat_label_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cat_label_txt)

        self.cat_label_lbl = QLabel(self.cat_label_frame)
        self.cat_label_lbl.setObjectName(u"cat_label_lbl")
        self.cat_label_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cat_label_lbl)


        self.horizontalLayout_9.addWidget(self.cat_label_frame)


        self.verticalLayout_2.addWidget(self.data_overview_frame)

        self.verticalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_export_test_result)
        self.menuFile.addAction(self.action_export_all_results)
        self.menuFile.addAction(self.action_clear_all)
        self.menuHelp.addAction(self.action_method_description)
        self.menuHelp.addAction(self.action_software_description)
        self.menuHelp.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.conf_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_export_test_result.setText(QCoreApplication.translate("MainWindow", u"Export test result", None))
        self.action_export_all_results.setText(QCoreApplication.translate("MainWindow", u"Export all results", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About MultiConTest", None))
        self.action_method_description.setText(QCoreApplication.translate("MainWindow", u"Method description", None))
        self.action_clear_all.setText(QCoreApplication.translate("MainWindow", u"Clear all data and results", None))
#if QT_CONFIG(tooltip)
        self.action_clear_all.setToolTip(QCoreApplication.translate("MainWindow", u"Removes all imported data and computed results", None))
#endif // QT_CONFIG(tooltip)
        self.action_software_description.setText(QCoreApplication.translate("MainWindow", u"Software description", None))
        self.cls_file_text.setText(QCoreApplication.translate("MainWindow", u"No file selected", None))
        self.generate_clustering_btn.setText(QCoreApplication.translate("MainWindow", u"My data is not clustered yet", None))
        self.select_cls_file.setText(QCoreApplication.translate("MainWindow", u"Select sample-cluster assignment file", None))
        self.cls_preview_lbl.setText(QCoreApplication.translate("MainWindow", u"Cluster overview", None))
        self.cls_table_lbl.setText(QCoreApplication.translate("MainWindow", u"Sample-cluster assignments", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cls_tab), QCoreApplication.translate("MainWindow", u"Clustering", None))
        self.label_file_txt.setText(QCoreApplication.translate("MainWindow", u"No label file selected", None))
        self.import_labels_btn.setText(QCoreApplication.translate("MainWindow", u"Select sample label CSV file", None))
        self.advanced_label_settings_btn.setText(QCoreApplication.translate("MainWindow", u"Adjust categories", None))
        self.drop_missing_check.setText(QCoreApplication.translate("MainWindow", u"drop missing values", None))
        self.category_count_label.setText(QCoreApplication.translate("MainWindow", u"maximum number of categories per label:", None))
        self.refine_cat_count_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.labels_preview_lbl.setText(QCoreApplication.translate("MainWindow", u"Potential confounding factor selection", None))
        self.sort_labels_lbl.setText(QCoreApplication.translate("MainWindow", u"sort labels", None))
        self.sort_up_btn.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.sort_down_btn.setText(QCoreApplication.translate("MainWindow", u"Z-A", None))
        self.query_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"find sample label by name...", None))
        self.find_cat_btn.setText(QCoreApplication.translate("MainWindow", u"Find label", None))
        self.sel_overlap_txt.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.sel_overlap_lbl.setText(QCoreApplication.translate("MainWindow", u"selected label", None))
        self.overlap_txt.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.sample_overlap_lbl.setText(QCoreApplication.translate("MainWindow", u"Sample overlap", None))
        self.overlap_lbl.setText(QCoreApplication.translate("MainWindow", u"all labels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.label_tab), QCoreApplication.translate("MainWindow", u"Sample labels", None))
        self.conf_warning_txt.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.conf_factor_lbl.setText(QCoreApplication.translate("MainWindow", u"Selected potential confounding factor:", None))
        self.conf_factor_txt.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.conf_tab_widget.setTabText(self.conf_tab_widget.indexOf(self.vis_tab), QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.conf_tab_widget.setTabText(self.conf_tab_widget.indexOf(self.cont_tab), QCoreApplication.translate("MainWindow", u"Contingency table", None))
        self.conf_p_val_txt.setText(QCoreApplication.translate("MainWindow", u"not computed", None))
        self.conf_p_val_lbl.setText(QCoreApplication.translate("MainWindow", u"p-value", None))
        self.conf_compute_btn.setText(QCoreApplication.translate("MainWindow", u"Compute", None))
        self.p_val_details_btn.setText(QCoreApplication.translate("MainWindow", u"Show details", None))
        self.export_single_result_btn.setText(QCoreApplication.translate("MainWindow", u"Export result", None))
        self.orig_p_txt.setText("")
        self.orig_p_lbl.setText(QCoreApplication.translate("MainWindow", u"original p-value", None))
        self.failed_perm_txt.setText("")
        self.failed_perm_lbl.setText(QCoreApplication.translate("MainWindow", u"redrawn permutations", None))
        self.failed_perm_txt_warning.setText("")
        self.failed_perm_lbl_warning.setText(QCoreApplication.translate("MainWindow", u"redrawn permutations", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.conf_tab), QCoreApplication.translate("MainWindow", u"Confounding test", None))
        self.multiple_testing_warning.setText(QCoreApplication.translate("MainWindow", u"Please consider applying multiple testing correction", None))
        self.export_all_results_btn.setText(QCoreApplication.translate("MainWindow", u"Export results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results_tab), QCoreApplication.translate("MainWindow", u"Test results", None))
        self.sample_count_txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sample_count_lbl.setText(QCoreApplication.translate("MainWindow", u"Samples", None))
        self.cluster_count_txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cluster_count_lbl.setText(QCoreApplication.translate("MainWindow", u"Clusters", None))
        self.label_count_txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_count_lbl.setText(QCoreApplication.translate("MainWindow", u"Imported sample labels", None))
        self.cat_label_txt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cat_label_lbl.setText(QCoreApplication.translate("MainWindow", u"Categorical sample labels", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

