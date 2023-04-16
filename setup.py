from setuptools import setup, find_packages

setup(
    name="gopyast",
    version="0.1.0",
    description="A Python wrapper for the Go AST parser",
    author="Itay Gersten",
    author_email="Itay.Gersten@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
