# Installation

`make install`


# Usage

## Read PDF files
This will read all `.pdf` files in the `data` folder and perform text extraction.
Output will be written to `.txt` files in `output` folder.

```
python read.py
```

## Process files via GPT
This will read all `.txt` files in `output` and send a completion request to GPT.
Output will be written to `.json` files in `output` folder.

```
python process.py
```