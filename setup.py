from setuptools import setup, find_packages

setup(
    name='goastpy',
    packages=find_packages(),
    version='0.1.1',
    license='MIT',
    description='a python wrapper for the built-in go parser using c-types',
    author='Itay Gersten',
    author_email='Itay.Gersten@gmail.com',
    url='https://github.com/itayg25/goastpy',
    download_url='https://github.com/itayg25/goastpy/archive/v_01.tar.gz',
    keywords=['GO', 'GOLANG', 'PYTHON', 'AST', 'GOPYGO'],
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
