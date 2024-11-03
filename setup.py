from setuptools import setup, find_packages
setup(
     name="myPackage",
     version="1.0",
     packages=find_packages(exclude=["tests*"]),
     license="MIT",
     install_requires = ["numpy"]
     
 )