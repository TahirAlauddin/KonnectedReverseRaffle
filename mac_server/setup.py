from setuptools import setup
import os

DATA_FILES = [('', ['config.json'])]
APP = ['reverseRaffle/flask-main.py']

DATA_DIRS = ['frontend/static', 'frontend/templates', 'frontend/media']

for data_dir in DATA_DIRS:
    for root, dirs, files in os.walk(data_dir):
        files = [os.path.join(root, file) for file in files]
        DATA_FILES.append((root, files))

OPTIONS = {
    'argv_emulation': True
}
with open('requirements-server-flask.txt', errors='ignore') as requirements_file:
    INSTALL_REQUIRES = [line.strip() for line in requirements_file.readlines()]

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=INSTALL_REQUIRES
)
