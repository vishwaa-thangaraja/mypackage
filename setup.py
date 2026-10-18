from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.0",
    description="A simple arithmetic calculator package for Python",
    author="Vishwaa Thangaraja",
    author_email="vishwaat27@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
