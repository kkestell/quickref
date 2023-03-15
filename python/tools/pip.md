```
# Install a package
pip install <package_name>

# Install a specific version of a package
pip install <package_name>==<version_number>

# Upgrade a package
pip install --upgrade <package_name>

# Uninstall a package
pip uninstall <package_name>

# Show a list of installed packages
pip list

# Show details about a specific package
pip show <package_name>

# Search for packages
pip search <search_term>

# Create a requirements file for an environment
pip freeze > requirements.txt

# Install packages from a requirements file
pip install -r requirements.txt

# Install a package to the user directory
pip install --user <package_name>

# Install a package from a local directory
pip install <path_to_package_directory>

# Install a package in editable mode (i.e. symlinked)
pip install -e <path_to_package_directory>

# Ignore cache and use the internet to install a package
pip install --no-cache-dir <package_name>

# Ignore dependencies when uninstalling a package
pip uninstall <package_name> --no-dependencies

# Show outdated packages
pip list --outdated

# Upgrade all outdated packages
pip install --upgrade-strategy eager --upgrade `pip list --outdated | awk '{ print $1 }' | tail -n +3`

# Upgrade pip itself
pip install --upgrade pip

# Check for security vulnerabilities in installed packages
pip check

# Install packages in parallel
pip install --parallel <number_of_processes> <package_name>
```