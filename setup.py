from setuptools import setup, find_packages
from .libs import __VERSION

setup(
    name="tentencrm",
    version=__VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
)
