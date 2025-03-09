# Project Templates
Templates for various project types using cookiecutter.

# Usage
Run `./install.sh` to add the templates to your user's store.
Run `./install.sh --remove` to remove the templates from your user's store.

Each template present will be prefixed with "ns_" when installed.  To list
all installed templates for your user:
```bash
cookiecutter -l
```

As an example, to create a new python package from the template:
```bash
cookiecutter ns_python_package
```
