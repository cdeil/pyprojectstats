"""Command line interface"""
import click
from .project import Project


@click.command()
@click.argument("path", type=click.Path(exists=True))
def cli(path):
    """Quick and simple Python project statistics"""
    click.echo(f"path: {path}")

    project = Project(path)
    project.find_files()
    project.analyse_files()
    project.make_report()
    print(project.report.to_text())
    print(project.report.to_pandas())


if __name__ == "__main__":
    cli()
