from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description= f.read()

setup(
    name="src",
    version="0.0.1",
    author="anoopmonu02",
    description="A small package for ANN implementation",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anoopmonu02/ANN_Demo",
    author_email="anoopmonu02@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ]
)