import sys
from pathlib import Path
from string import Template


def remove_file(path: Path) -> None:
    if path.exists():
        path.unlink()


def main() -> int:
    license = r"{{ cookiecutter.license }}"
    if license != "None":
        source_file = (
            Path(r"{{ cookiecutter._repo_dir }}").resolve().parent
            / ".shared"
            / "licenses"
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
    project_type = r"{{ cookiecutter.project_type }}"
    if project_type == "library":
        package_path = Path("src") / r"{{ cookiecutter.project_slug }}"
        remove_file(package_path / "__main__.py")
        remove_file(package_path / "application.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
