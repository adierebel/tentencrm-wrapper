from setuptools import setup, find_packages
from tentencrm import __VERSION__

setup(
    name="tentencrm",
    version=__VERSION__,
    description='Python API Wrapper for TentenCRM',
    author='adierebel',
    url='https://github.com/adierebel/tentencrm-wrapper',
    python_requires=">=3.10",
    packages=['tentencrm'],
    py_modules=['tentencrm'],
    include_package_data=True,
    license='MIT',
    install_requires=["flask==3.1.1", "requests==2.32.4"],
)
