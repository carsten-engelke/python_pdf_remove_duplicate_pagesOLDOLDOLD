"""Console script for python_pdf_remove_duplicate_pages."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for python_pdf_remove_duplicate_pages."""
    click.echo("Replace this message by putting your code into "
               "python_pdf_remove_duplicate_pages.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    click.echo("Hi! this works")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
