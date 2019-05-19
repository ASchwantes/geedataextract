import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geedataextract",
    version="0.0.1",
    author="Amanda Schwantes",
    author_email="aschwantes@gmail.com",
    license='MIT',
    description="Download environmental and remote sensing data from Google Earth Engine for uploaded point or polygon shapefiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ASchwantes/geedataextract",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.5',
)
