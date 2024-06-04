# setup.py

from setuptools import setup, find_packages

setup(
    name='py_tools',
    version='0.1.0',
    author='Lin Xiong',
    author_email='lxiong@umd.edu',
    description='A simple Hello World command-line tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/linxiongecu/template4cml',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'py_tools_c1=py_tools.c1:main',
            'py_tools_c2=py_tools.c2:main',
        ],
    },
)
