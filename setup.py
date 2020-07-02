import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="perusethis",
    version="0.0.1",
    author="Tim Mastny",
    author_email="tim.mastny@gmail.com",
    description="Python package to create package skeletons.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='',
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True
)
