import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setup(
    name='apod.py',
    author='Zihad-Kabir-Tanvir',
    version='0.0.1',
    description='a simple easy to use python wrapper for Nasa Astronomy Picture of the Day',
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url='https://github.com/Zihad-Kabir-Tanvir/apod.py',
    py_modules=['apod'],
    package_dir={'':'src'},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Freeware",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Education",
    ],
    install_requires=[
        "requests ~= 2.0.0",
    ],
    include_package_data=True,
)
