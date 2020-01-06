"""
"""
__version__ = "0.1.0"

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name="roboatenviro",
    version=__version__,
    packages=["roboatenviro"],
    test_suite="tests",
)
