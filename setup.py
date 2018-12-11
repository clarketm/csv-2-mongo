import setuptools, os

from csv_2_mongo import __VERSION__

with open(f"{os.path.abspath(os.path.dirname(__file__))}/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv-2-mongo",
    version=__VERSION__,
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="Import a CSV to MongoDB.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/csv_2_mongo",
    packages=setuptools.find_packages(),
    install_requires=["click", "pandas", "pymongo"],
    extras_require={"dev": ["black", "nose2"]},
    py_modules=["csv_2_mongo"],
    entry_points={"console_scripts": ["csv-2-mongo=csv_2_mongo:cli"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
