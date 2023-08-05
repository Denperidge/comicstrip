# Comicstrip - extract individual frames from a comic book/strip

from PIL import Image
from PIL.ImageFile import Parser
from PIL.ImageEnhance import Contrast
from PIL.ImageFilter import BLUR
from optparse import OptionParser
from PIL.ImageOps import autocontrast

from .Comic import Comic


_version = "0.1"




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


parser = OptionParser(usage="%prog [options] [pgfile1, pgfile2, ...]",
                      version="%%prog %s" % (_version),
                      description="Split a comic page into individual frames")
parser.add_option("-q", "--quiet", action="store_true", dest="quiet",
                  help="Don't print progress messages to stdout [default:%default]")
parser.add_option("-d", "--debug", dest="debug", action="store_true",
                  help="Enable debug prints [default:%default]")
parser.add_option("-f", "--file", dest="infile", type="string", metavar="FILE",
                  help="Name of the input file")

parser.add_option("", "--prefix", dest="prefix",
                  help="Prefix for output files")
parser.add_option("", "--left-ignore", type="int", dest="lignore", metavar="PIXELS",
                  help="How much of the left margin to ignore when detecting rows [default:%default]")
parser.add_option("", "--right-ignore", type="int", dest="rignore", metavar="PIXELS",
                  help="How much of the right margin to ignore when detecting rows [default:%default]")
parser.add_option("", "--firstpage", dest="firstPg", type="string", metavar="PGFILENAME",
                  help="Name of the title page in comic archive file")
parser.add_option("", "--firstpg-row", type="int", dest="firstPgRow", metavar="PIXELS",
                  help="From which line of the first page should the processing start [default:%default]")
parser.add_option("", "--startrow", type="int", dest="startRow", metavar="PIXELS",
                  help="From which line of the each page (other than the first page) should the processing start [default:%default]")
parser.add_option("", "--glob", dest="filePat", metavar="GLOB",
                  help="A glob expression to select files to be processed from the book. (Not required if a file list is provided.)")
parser.add_option("", "--gutter-width", dest="gwidth", metavar="WIDTH",
                  help="Minimum width of the gutter [default:%default]")
parser.add_option("", "--min-width", dest="fwidth", metavar="WIDTH", type="int",
                  help="Minimum width of a frame [default:%default]")
parser.add_option("", "--min-height", dest="fheight", metavar="HEIGHT", type="int",
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




def main():
    kw = getargs(parser)
    book = Comic(**kw)
    book.process()


if __name__ == "__main__":
   main()