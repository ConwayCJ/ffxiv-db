# FFXIV Wikipedia Table Parser

This Python command-line tool helps convert FFXIV Wikipedia tables into CSV files for crafting professions.

## Installation

Clone the repository:
```bash
git clone <repository_url>
cd <repository_directory>
```

## Install dependencies:

`pip install -r requirements.txt`

## Usage

# Commands Available: 

* new-craft-db: Converts FFXIV Wikipedia to CSV files for each profession.
* list-professions: Lists available crafting professions and level ranges.
* make-crafter-csv: Converts every profession's craftable items into a single CSV file.
* make-profession-csv `profession`: Converts a specific profession's craftable items into a CSV file.

## Examples:

```bash
python main.py new-craft-db
python main.py list-professions
python main.py make-crafter-csv
python main.py make-profession-csv blacksmith
```

# Dependencies:

* Python 3.x
* BeautifulSoup4

# License:

Replace `<repository_url>` and `<repository_directory>` with your actual repository details before using it. This README provides clear instructions on installation, usage examples, dependencies, and licensing information for your project.
