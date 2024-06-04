# template for building command line tools 
create python command line tool template

## create virtual environment
python -m venv ../virtual

source  ../virtual/bin/activate

## print files structure


```python
import os
def print_file_structure(directory, indent=''):
    for item in os.listdir(directory):
        if item.startswith('.'): continue
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(f"{indent}├── {item}")
        elif os.path.isdir(item_path):
            print(f"{indent}├── {item}/")
            print_file_structure(item_path, indent + "│   ")
# Replace 'path_to_your_directory' with the actual path to the directory you want to print
directory_path = '.'
print(f"{os.path.basename(directory_path)}/")
print_file_structure(directory_path)
```

    ./
    ├── ReadME.ipynb
    ├── README.md
    ├── py_tools/
    │   ├── setup.py
    │   ├── LICENSE
    │   ├── README.md
    │   ├── py_tools/
    │   │   ├── c2.py
    │   │   ├── __init__.py
    │   │   ├── c1.py
    │   ├── src/
    │   │   ├── __init__.py
    │   │   ├── module1.py


## install
pip install .

## use
py_tools_c1

py_tools_c2 yourname

# References
https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/

https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/


```python

```
