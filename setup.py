from setuptools import setup, find_packages

setup(
    name="goastpy",
    version="0.1.5",
    packages=find_packages(),
    package_dir={"goastpy": "./goastpy"},
    data_files=[('goastpy', ['./goastpy/goastparser.h', './goastpy/goastparser.so'])],
    install_requires=[],
    description='a python wrapper for the built-in go parser using c-types',
    author='Itay Gersten',
    author_email='Itay.Gersten@gmail.com',
    url='https://github.com/itayg25/goastpy',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=['GO', 'GOLANG', 'PYTHON', 'AST', 'GOPY', 'PYGO', 'PARSER', 'ASTPARSER'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",

)
