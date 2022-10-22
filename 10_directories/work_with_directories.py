from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft

# Relative path

# Path() object returns the current directory
path = Path('../9_packages/ecommerce')
print(path.exists())

# .mkdir() adds new directory
# path.mkdir()
# .rmdir() removes a directory
# path.rmdir()

# can use .glob() to find all files or all files in a folder
# or specific files in current folder
print(path.glob('*.py'))

# All .py files in the defined/current directory
for file in path.glob('*.py'):
    print (file)
