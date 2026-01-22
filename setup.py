from setuptools import setup

APP = ['main.py']
DATA_FILES = [('database', ['database/database.json'])]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['helpers'],
    'includes': ['tkinter'],
    'resources': [
        'database',
        '/opt/homebrew/opt/tcl-tk/lib'  # Adjust this path if necessary
    ],
    'iconfile': 'ComicsHelperIcon_GuidelineReady.icns',  # Optional: include a custom icon
    'plist': {
        'NSHighResolutionCapable': True,  # Enable Retina display support
    },
}

setup(
    app=APP,
    name='ComicsHelper',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)