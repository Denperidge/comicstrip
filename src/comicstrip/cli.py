
from .Comic import Comic
from argparse import ArgumentParser, FileType
from .constants import _VERSION

def getargs(parser):
    (options, args) = parser.parse_args()
    kw = {}
    kw["infile"] = options.infile
    if kw["infile"] is None:
     raise ValueError("Input File Not Specified")
    kw["prefix"] = options.prefix
    kw["firstPg"] = options.firstPg
    kw["firstPgRow"] = options.firstPgRow
    kw["startRow"] = options.startRow
    kw["lignore"] = options.lignore
    kw["rignore"] = options.rignore
    kw["filePat"] = options.filePat
    kw["quiet"] = options.quiet
    kw["gwidth"] = options.gwidth
    kw["fwidth"] = options.fwidth
    kw["fheight"] = options.fheight
    kw["debug"] = options.debug
    kw["fileList"] = args
    return kw


parser = ArgumentParser(usage="%prog [options] [pgfile1, pgfile2, ...]",
                        prog="comicstrip",
                        description="Split a comic page into individual frames")

parser.add_argument("-v", "--version",
                    action="version",
                    version="%%(prog)s %s" % (_VERSION))

parser.add_argument("-q", "--quiet", 
                  action="store_true", 
                  dest="quiet",
                  help="Don't print progress messages to stdout [default:%default]")

parser.add_argument("-d", "--debug", 
                  dest="debug", 
                  action="store_true",
                  help="Enable debug prints [default:%default]")

parser.add_argument("-f", "--file", 
                    dest="infile",
                    type=FileType("r"),
                    metavar="FILE",
                    help="Name of the input file",
                    required=True)

parser.add_argument("--prefix", 
                    dest="prefix",
                    help="Prefix for output files")

parser.add_argument("--left-ignore", 
                    type=int,
                    dest="lignore",
                    metavar="PIXELS",
                    help="How much of the left margin to ignore when detecting rows [default:%default]")

parser.add_argument("--right-ignore", 
                    type=int, 
                    dest="rignore", 
                    metavar="PIXELS",
                    help="How much of the right margin to ignore when detecting rows [default:%default]")

parser.add_argument("--firstpage", 
                    dest="firstPg", 
                    type=str, 
                    metavar="PGFILENAME",
                    help="Name of the title page in comic archive file")

parser.add_argument("--firstpg-row", 
                    type=int, 
                    dest="firstPgRow", 
                    metavar="PIXELS",
                    help="From which line of the first page should the processing start [default:%default]")

parser.add_argument("--startrow", 
                    type=int, 
                    dest="startRow", 
                    metavar="PIXELS",
                    help="From which line of the each page (other than the first page) should the processing start [default:%default]")

parser.add_argument("--glob", 
                    dest="filePat", 
                    metavar="GLOB",
                    help="A glob expression to select files to be processed from the book. (Not required if a file list is provided.)")

parser.add_argument("--gutter-width", 
                    dest="gwidth", 
                    metavar="WIDTH",
                    help="Minimum width of the gutter [default:%default]")

parser.add_argument("--min-width",
                    dest="fwidth", 
                    metavar="WIDTH", 
                    type=int,
                    help="Minimum width of a frame [default:%default]")

parser.add_argument("--min-height",
                    dest="fheight",
                    metavar="HEIGHT",
                    type=int,
                    help="Minimum height of a frame [default:%default]")

parser.set_defaults(quiet=False,
                    prefix="cstrip-",
                    lignore=0,
                    rignore=0,
                    firstPgRow=0,
                    startRow=0,
                    gwidth=15,
                    fwidth=50,
                    fheight=50,
                    debug=True)


def run_cli():
    kw = getargs(parser)
    book = Comic(**kw)
    book.process()
