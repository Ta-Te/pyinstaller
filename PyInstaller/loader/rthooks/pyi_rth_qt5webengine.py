#-----------------------------------------------------------------------------
# Copyright (c) 2015-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

import os
import sys

# See ``pyi_rth_qt5.py`: use a "standard" PyQt5 layout.
if sys.platform == 'darwin':
    framework_path = os.path.normpath(os.path.join(
        sys._MEIPASS, '..', 'Resources', 'PyQt5', 'Qt', 'lib',
        'QtWebEngineCore.framework', 'Helpers'
    ))
    libexec_path = os.path.normpath(os.path.join(
        sys._MEIPASS, 'PyQt5', 'Qt', 'libexec', 'QtWebEngineProcess'
    ))
    if os.path.exists(framework_path):
        os.environ['QTWEBENGINEPROCESS_PATH'] = framework_path
    else:
        os.environ['QTWEBENGINEPROCESS_PATH'] = libexec_path
        os.environ['QT_WEBENGINE_ICU_DATA_DIR'] = os.path.normpath(
            os.path.join(
                sys._MEIPASS, 'PyQt5', 'Qt', 'resources'
            )
        )
