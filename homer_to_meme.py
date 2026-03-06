#!/usr/bin/env python3

__author__ = "Anna Pardo"

# import modules
import argparse
import os

def write_meme_header(version,output,alphabet="ACGT",strands=None,bkgrd=None):
    """
    Arguments:
        version = desired version of MEME-suite
        output = full path to output file (to which motifs will be appended later)
        alphabet = DNA or other alphabet (DNA by default)
        strands = strand information (optional, default not provided)
        bkgrd = background letter frequencies (optional, default not provided)
    """
    with open(output,"w+") as outfile:
        outfile.write("MEME version "+version+"\n\n")
        outfile.write("ALPHABET= "+alphabet+"\n\n")
        if strands!=None:
            outfile.write("strands: "+strands+"\n\n")
        if bkgrd!=None:
            outfile.write("Background letter frequencies\n"+bkgrd+"\n\n")

def write_single_meme(infpath,output,nsites=None,e=None,alphabet="ACGT"):
    """
    Arguments:
        infpath = full path to a single-motif input file (in HOMER .motif format)
        output = full path to output file with MEME header already written
        nsites = source sites (see MEME format documentation; default 20 if not provided; default in this function None)
        e = source E-value (see MEME format documentation; default 0 if not provided to MEME; default in this function None)
        alphabet = DNA or other alphabet (DNA by default)
    """
    if nsites != None:
        nsites = " nsites= "+str(nsites)+" "
    else:
        nsites = ""

    if e != None:
        e = " E= "+str(e)+" "
    else:
        e = ""

    with open(infpath,"r") as infile:
        with open(output,"a") as outfile:
            for line in infile:
                if line.startswith(">"):
                    info = line.strip().split("\t")
                    motifname = info[1]
                    motifseq = info[0].lstrip(">")
                    outfile.write("MOTIF "+motifname+"_"+motifseq+"\n")
                    outfile.write("letter-probability matrix: alength= "+str(len(alphabet))+" w= "+str(len(motifseq))+nsites+e+"\n")
                else:
                    outfile.write(line) # note lines in HOMER-format motif files already have \n at the end
            outfile.write("\n")

def main():
    parser = argparse.ArgumentParser(description="Parse args")
    # command line arguments
    parser.add_argument("--directory","-d",type=str,help="full path to directory containing HOMER .motif files (input)")
    parser.add_argument("--outfile","-o",type=str,help="full path to desired output file")
    parser.add_argument("--version","-v",type=str,help="MEME-suite version")
    parser.add_argument("--alphabet","-a",default="ACGT",type=str,help="alphabet to put in MEME header (default: ACGT)")
    parser.add_argument("--strands","-s",default=None,type=str,help="optional strand information for MEME header (default=None)")
    parser.add_argument("--background","-b",default=None,type=str,help="optional background letter frequency information for MEME header (default=None)")
    args = parser.parse_args()
    directory = str(args.directory)
    outfile = str(args.outfile)
    version = str(args.version)
    alphabet = str(args.alphabet)
    if args.strands!=None:
        strands = str(args.strands)
    else:
        strands = args.strands
    if args.background!=None:
        background = str(args.background)
    else:
        background = args.background

    # write the header
    write_meme_header(version,outfile,alphabet,strands,background)

    # loop through files in the input directory & append them to the output file
    for f in os.listdir(directory):
        if f.endswith(".motif"):
            write_single_meme(os.path.join(directory,f),outfile)

if __name__ == "__main__":
    main()
