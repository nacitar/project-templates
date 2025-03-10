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

# Recommendations
Python's pyproject.toml has fields for the license, including the author name
and email address.  The MIT and BSD licenses also require an author name and
an email address in their standard formats, so these templates prompt for that
information.  Because that feels like a separate category of information than
the rest of the project-centric input fields, those fields are requested first.
This avoids mental context-switching by the user.  You can focus on the fields
not directly related to the project and then swap to those more relevant.  That
said, typing in this typically identical information every time can be
annoying. Fortunately, cookiecutter lets you specify defaults in
`~/.cookiecutterrc` which eases this.

Here's a simple `~/.cookiecutterrc` (yaml) to set these fields:
```yaml
default_context:
    author: "First Last"
    email: "somebody@website.com"
```
