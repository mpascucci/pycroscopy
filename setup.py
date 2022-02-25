import setuptools

VERSION_MAJOR = 0
VERSION_MINOR = 1

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='Pycroscopy',
                 version='{}.{}'.format(VERSION_MAJOR, VERSION_MINOR),
                 description='Python tools for microscopy',
                 author='Marco Pascucci',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author_email='marpas.paris@gmail.com',
                 url='https://github.com/mpascucci/pycroscopy',
                 packages=['pycroscopy'],
                 install_requires=['multipagetiff',
                                   'numpy', 'matplotlib', 'tqdm', 'connected-components-3d'],
                 classifiers=[
                     "Programming Language :: Python",
                     "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                     "Operating System :: OS Independent",
                 ]
                 )