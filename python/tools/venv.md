```
# Creating a virtual environment
python3 -m venv myenv        # create a new virtual environment named 'myenv'

# Activating a virtual environment
source myenv/bin/activate  # activate the 'myenv' virtual environment on Unix/Linux
.\myenv\Scripts\activate   # activate the 'myenv' virtual environment on Windows

# Deactivating a virtual environment
deactivate                 # deactivate the current virtual environment

# Installing packages in a virtual environment
pip install <package_name> # install a package in the current virtual environment

# Exporting the installed packages in a virtual environment to a requirements file
pip freeze > requirements.txt # write the installed packages to a requirements file

# Creating a new virtual environment from a requirements file
python3 -m venv myenv2       # create a new virtual environment named 'myenv2'
source myenv2/bin/activate  # activate the 'myenv2' virtual environment on Unix/Linux
pip install -r requirements.txt  # install the packages from the requirements file

# Cloning a virtual environment
python3 -m venv --system-site-packages myenv_clone # create a new virtual environment named 'myenv_clone' that uses the system site-packages directory
```