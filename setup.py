from distutils.core import setup
import py2exe

setup(windows=['WinshellBots.py'], options = {'py2exe':{'packages': ["winshell"]}})


