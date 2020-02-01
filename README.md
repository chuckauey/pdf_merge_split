# pdf_merge_split

cli tool to split or merge pdf files

### Installing

git@github.com:chuckauey/pdf_merge_split.git
pip install -r requirements.txt

### Usage

usage: pdf_split_merge.py [-h] (--split SPLIT | --merge MERGE [MERGE ...])

split or merge pdfs

optional arguments:  
  -h, --help → show this help message and exit  
  --split SPLIT → split a pdf into multiple files  
  --merge MERGE [MERGE ...] → merge multiple files into one

### Examples

#### Split
pdf_split_merge.py --split filename  
created: filename_page_1.pdf  
created: filename_page_2.pdf  

#### Merge
pdf_split_merge.py --merge filename1 filename2  
created: merged.pdf

* Thanks to http://www.blog.pythonlibrary.org/