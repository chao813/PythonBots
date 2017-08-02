from distutils.core import setup
import py2exe

setup(windows=['WolframBotGUI.py'], options = {'py2exe':{'includes': ["wolframalpha","jaraco"]}})


