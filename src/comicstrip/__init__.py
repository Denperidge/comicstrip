# Comicstrip - extract individual frames from a comic book/strip
from .constants import _VERSION
from .Page import Page
from .Comic import Comic
from .cli import run_cli

if __name__ == "__main__":
   run_cli()