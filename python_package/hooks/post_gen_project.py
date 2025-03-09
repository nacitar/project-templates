import sys
from pathlib import Path
from string import Template


def main() -> int:
    license = r"{{ cookiecutter.license }}"
    if license != "None":
        source_file = (
            Path(r"{{ cookiecutter._repo_dir }}").resolve().parent
            / ".shared"
            / "Licenses"
            / r"{{ cookiecutter.license }}.txt"
        )
        destination_file = Path().resolve() / "LICENSE"
        license_template = Template(source_file.read_text())
        destination_file.write_text(
            license_template.substitute(
                copyright_year=r"{{ cookiecutter.copyright_year }}",
                author=r"{{ cookiecutter.author }}",
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
