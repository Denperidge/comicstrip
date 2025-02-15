           Comic Strip - Extract individual frames of a comic book
           -------------------------------------------------------


What is it?
-----------

While it is easy to read comic books on a regular PC, it is much more
inconvenient to do so on a PDA because of its small screen size - one typically
ends up scrolling around the whole page to read it. This application breaks down
each page of a comic book into individual frames (i.e. each frame becomes an
individual page) which can then be conveniently viewed on small-screen devices
like PDAs. It can process a single image file or a whole comic book file (only
cbz files are supported currently)

Installation
------------
```bash
git clone https://github.com/Denperidge/comicstrip.git
cd comicstrip
python3 -m pip install -r requirements.txt
python3 -m src.comicstrip
```

To run tests, simply use `python3 -m unittest`


Basic Terminology Used
----------------------

A typical page of a comic book consists of a number of frames separated by
horizontal/vertical white spaces called gutters. The title page might contain an
additional heading in the beginning. The height of each frame in a page (indeed
in all pages of a book) are more-or-less the same. The frame widths, however,
usually differ.

A comic book is usually a compressed archive of images with different
extensions to indicate the type of compression. Common formats include .cbz
(which is simply a zip archive of images) and .cbr (which is an RAR archive of
images). As mentioned above, comicstrip supports only .cbz files currently.


Usage
-----

Basic Invocation:

python3 -m src.comicstrip [options] [pgfile1, pgfile2, ...]

The comicstrip application is, at the moment, a command line application.
All parameters are passed in via command line parameters. A GUI front-end is
planned down the line to make the application easier to use.

Valid Options are:

--version
    Show program's version number and exit.

-h, --help
    Show a brief help message and exit.

-q, --quiet
    Don't print progress messages to stdout [default:False].
    By default a single dot is printed for every page processed. Every 5th page
    a page number is displayed (....5....10...etc)

-d, --debug           Enable debug prints [default:False].
    Used only for debugging. Ordinary users won't need to enable this. It would
    be helpful to enable '-q' when using the -d option so that the regular
    progress display does not interfere with the debug output (and vice versa).

-f FILE, --file=FILE
    Name of the input file. Mandatory parameter
    This could be the name of an image file or the name of a .cbz file.
    comicstrip supports the image formats supported by the Python Imaging
    Library.

--prefix=PREFIX
    Prefix for output files. Mandatory parameter
    The individual frames are saved to files with names of the form:
        `<prefix>00.jpg,`
        `<prefix>01.jpg`
        `<prefix>02.jpg`
        ...
    The number of leading zeroes is automatically adjusted depending on the
    number of output frames. If you want to save the output files into a
    particular directory just add the directory prefix to the file prefix (e.g.
    --prefix /tmp/foo-)

--left-ignore=PIXELS
    How much of the left margin to ignore when detecting rows [default:0]
    Sometimes (especially for scanned comics) the edges in the middle of a page
    tend to have a shadow all along it, making the gutter "non white". This
    interferes with the gutter detection algorithm and prevents a gutter from
    being successfully detected. This parameter tells the application how much
    many pixels on the left side should be ignored when detecting gutters. Note:
    This doesn't mean the pixels on the left of the margin are discarded in the
    final output - it just means that they are not considered during gutter
    detection.

--right-ignore=PIXELS
    How much of the right margin to ignore when detecting rows [default:0].
    Same as "--left-ignore" except that this is for the right side.

--firstpage=PGFILENAME
    Name of the title page in comic archive file.
    The first page of a comic archive could be different from other pages in
    that it might have a heading on top of the page (which needs to be skipped).
    This parameter tells the application the name of the first page if the input
    file is a comic book archive. Note: This parameter is ignored if the input
    file is a single image file and not a comic book archive.

--firstpg-row=PIXELS
    From which line of the first page should the processing start [default:0]
    This parameter tells the application whether or not there is a title in the
    first page and, if so, how many pixels to skip to ignore the title. Without
    this parameter the processing might stop at the title itself instead of
    skipping over it.

--startrow=PIXELS
    From which line of the each page (other than the first page) should the
    processing start [default:0]
    For scanned comics, the gutter on the top of the page might have a shadow
    along it, thus interfering with the gutter processing algorithm. This
    parameter tells the application how many pixels to skip when detecting rows
    in a page, thus allowing the algorithm to skip over the shadow.

--glob=GLOB
    A glob expression to select files to be processed from the book. (Not
    required if a file list is provided.)
    File names of pages of a comic book archive typically have a pattern.
    Instead of specifying each page by name, this parameter allows a glob
    pattern to be specified (e.g. --glob '*[0-9][0-9].jpg'). Remember to protect
    the glob expression in quotes to prevent file expansion in the shell.

--gutter-width=WIDTH
    Minimum width of the gutter [default:15]

--min-width=WIDTH
    Minimum width of a frame [default:100]
    A more accurate value speeds up the frame extraction algorithm

--min-height=HEIGHT
    Minimum height of a frame [default:100]
    A more accurate value speeds up the frame extraction algorithm

pgfile1, pgfile2, ... is a list of the names of the page files in the comic book
archive.  These can be left out if the "--glob" parameter is supplied. On the
other hand, if you wish to extract only a few pages of a comic book archive,
then they can be specified on the command line.

Of course, for single page image files, this list is empty.


Limitations
-----------
The application might not be able to successfully extract frames from a
(slightly) rotated page (i.e. the page is not entirely horizontal).

In some pages, some images "overflow" into the gutter space (e.g. some
speech bubbles overflow into the vertical gutter). In such cases the application
will not be able to successfully separate the two frames. If it is the vertical
gutter that is "occupied" then the two adjacent frames will be extracted as one.
If, however, the horizontal gutter is "occupied" then the two rows will be
treated as one!

If the gutters in a page are not "clean" (i.e. they contain some "random",
dark pixels - typical in some scanned images of old comics) then they too might
negatively impact the gutter processing algorithm. For images where the gutter
is "clean" (all "light" colors) there shouldn't be any problems.


Contact
-------
You can reach me at: koofoss(at)g-m-x(dot)com
(remove the '-'s between the characters above).


Happy Reading!
Koo.

