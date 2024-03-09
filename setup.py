# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301

NAME = "pylivoltek"
VERSION = "1.0.1"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Livoltek API",
    author_email="",
    url="",
    keywords=["Swagger", "Livoltek API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Python API Client for the Livoltek API
    """
)
