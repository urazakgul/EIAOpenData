from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name="EIAOpenData",
    version="0.1.0",
    packages=find_packages(),
    author="Uraz Akgül",
    author_email="urazdev@gmail.com",
    description="EIAOpenData is a Python package that provides easy access to various energy-related data obtained from the Energy Information Administration (EIA) API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/urazakgul/EIAOpenData",
    license="MIT",
    install_requires=[
        "requests",
        "pandas",
        "openpyxl",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.8",
)