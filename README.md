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
The MIT and BSD licenses require an author name and email, so these templates
prompt for that information.  Because that feels like a separate category of
information than the rest of the project-centric input fields, those fields are
requested first.  This avoids mental context-switching by the user.  That said,
typing in this typically identical information every time can be annoying.
Fortunately, cookiecutter lets you specify defaults in `~/.cookiecutterrc`.

Here's a simple `~/.cookiecutterrc` to set these fields:
```yaml
default_context:
    author: "First Last"
    email: "somebody@website.com"
```
