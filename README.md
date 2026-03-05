# homer_to_meme.py - Python script to convert HOMER-format .motif files to MEME-format motif files

A Python3 script to convert HOMER `.motif` files [(description here)](http://homer.ucsd.edu/homer/motif/creatingCustomMotifs.html) to [MEME-format motif files](https://mitra.stanford.edu/kundaje/marinovg/oak/programs/meme-5.4.1/doc/meme-format.html), i.e. if you have done motif enrichment with [HOMER](http://homer.ucsd.edu/homer/) and want to use [MEME](https://mitra.stanford.edu/kundaje/marinovg/oak/programs/meme-5.4.1/doc/overview.html) FIMO to find instances of those motifs in the genome.

## Usage
Basic usage:<br>
`python homer_to_meme.py -d /[path/to/input/directory] -o [/path/to/output/file] -v [MEME version] [optional args]`

Full description of command line arguments:<br>
`-h, --help            show this help message and exit`<br>
`  --directory DIRECTORY, -d DIRECTORY
                        full path to directory containing HOMER .motif files
                        (input)`<br>
`  --outfile OUTFILE, -o OUTFILE
                        full path to desired output file`<br>
`  --version VERSION, -v VERSION
                        MEME-suite version`<br>
`  --alphabet ALPHABET, -a ALPHABET
                        alphabet to put in MEME header (default: ACGT)`<br>
`  --strands STRANDS, -s STRANDS
                        optional strand information for MEME header
                        (default=None)`<br>
`  --background BACKGROUND, -b BACKGROUND
                        optional background letter frequency information for
                        MEME header (default=None)`

Written under Python version 3.10.9.
