import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse
import warnings
import sys
warnings.filterwarnings("ignore")


def split(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    try:
        pdf = PdfFileReader(path, strict=False)
    except:
        print("can't read file {0} with error {1}".format(
            path, sys.exc_info()[0].__name__))
        quit()

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('created: {}'.format(output_filename))


def merge(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        try:
            pdf_reader = PdfFileReader(path, strict=False)
        except:
            print("can't read file {0} with error {1}".format(
                path, sys.exc_info()[0].__name__))
            quit()
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split or merge pdfs')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--split', dest='split',
                       help='split a pdf into multiple files')
    group.add_argument('--merge', dest='merge', nargs='+',
                       help='merge multiple files into one')

    args = parser.parse_args()
    if args.split:
        split(args.split)
    if args.merge:
        if len(args.merge) > 1:
            merge("merged.pdf", args.merge)
        else:
            print("multiple files required")
