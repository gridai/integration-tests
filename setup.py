#:!/usr/bin/env python
from setuptools import find_packages, setup

version = None

install_requires = [
    "black",
]


setup(
    name="lightning-pose",
    packages=find_packages(),
    version=version,
    description="Convnets for tracking body poses",
    author="Dan Biderman",
    install_requires=install_requires,  # load_requirements(PATH_ROOT),
    author_email="danbider@gmail.com",
    url="https://github.com/danbider/lightning-pose",
    keywords=["machine learning", "deep learning"],
)