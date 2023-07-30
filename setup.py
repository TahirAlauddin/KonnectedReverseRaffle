from setuptools import setup

APP = ['main.py']
DATA_FILES = ['images', 'images']
OPTIONS = {
    'argv_emulation': True
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)


from setuptools import setup

import os
APP = ['manage.py']
DATA_DIRS = ['reverseRaffle', 'reverseRaffle/frontend/satic', 'reverseRaffle/frontend/templates', 'rverseRaffle/frontend/media']


DATA_FILES = []

for data_dir in DATA_DIRS:
    for root, dirs, files in os.walk(data_dir):
        files = [os.path.join(root, file) for file in files]
        DATA_FILES.append((root, files))

OPTIONS = {
    'argv_emulation': True,
}
with open('requirements-server.txt', errors='ignore') as requirements_file:
    INSTALL_REQUIRES = [line.strip() for line in requirements_file.readlines()]

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=INSTALL_REQUIRES
)