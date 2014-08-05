# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShortcutManagerDialog
                                 A QGIS plugin
 This plugin create shortcuts in toolbar
                             -------------------
        begin                : 2014-07-18
        git sha              : $Format:%H$
        copyright            : (C) 2014 by NextGIS
        email                : info@nextgis.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from shortcut_creator import ShortcutCreator
from shortcut_manager_dialog_ui_base import Ui_ShortcutManagerDialog

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QObject, SIGNAL

class ShortcutManagerDialog(QDialog, Ui_ShortcutManagerDialog):
    def __init__(self, parent, createShortcutFunction):
        """Constructor."""
        QDialog.__init__(self)
        
        self.setupUi(self)

        QObject.connect(self.pushButton, SIGNAL("clicked()"), self.createShortcut)
        
        self._createShortcutFunction = createShortcutFunction
    
    def addShortcut(self, shortcutWidget):
        self.shorcutWidgetsContainer.addWidget(shortcutWidget, 0)
    
    def createShortcut(self):
        dlg = ShortcutCreator(self, self._createShortcutFunction)
        dlg.show()
        # Run the dialog event loop
        result = dlg.exec_()
        # See if OK was pressed
        if result:
            pass