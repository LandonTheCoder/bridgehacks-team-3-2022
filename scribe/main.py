#! /usr/bin/python3

import recognize, noteform

def main(passed_args=None):
    import argparse
    parser = argparse.ArgumentParser(description="Load an audio file and recognize its contents. ")
    parser.add_argument("outfile", help="The text file to write to. Must be specified.")
    parser.add_argument("infile", help="The audio file to recognize. If unspecified, assumed to be \"./speech-recognition-test.wav\"", nargs='?')
    args = parser.parse_args(passed_args)
    FNAME = "./speech-recognition-test.wav"
    if args.infile == None:
        phraselist = recognize.recognize_file(FNAME)
    else:
        phraselist = recognize.recognize_file(args.infile)
    print("phraselist:", phraselist)
    filtered_phraselist = []
    for x in phraselist:
        y = noteform.filter_sentence(x)
        filtered_phraselist.append(y)
        print(y)
    fobj = open(args.outfile, "w+")
    notestr = "\n".join(filtered_phraselist) + "\n"
    print("notestr =", notestr)
    fobj.write(notestr)
    fobj.close()
main()
