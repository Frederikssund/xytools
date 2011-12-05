"""
/***************************************************************************
 XyTools
                                 A QGIS plugin
 Tools for managing tabular data with x y columns
                             -------------------
        begin                : 2011-08-19
        copyright            : (C) 2011 by webmapper
        email                : richard@webmapper.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "XyTools"
def description():
    return "Tools for managing tabular data with x y columns"
def version():
    return "Version 0.2.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.6"
def classFactory(iface):
    # load XyTools class from file XyTools
    from xytools import XyTools
    return XyTools(iface)
