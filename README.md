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

Commands Available: 

* `list-professions`: Lists available crafting professions and level ranges.
* `make-crafter-csv`: Generates a single CSV file for every professions craftable items.
* `make-profession-csv <profession>`: Generates a single CSV file for a professions craftable items.

## Examples:

```bash
python main.py list-professions
python main.py make-crafter-csv
python main.py make-profession-csv blacksmith
python main.py make-profession-csv weaver
```

## Dependencies:

* Python 3.x
* BeautifulSoup4

## Contributing:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/improvement).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature/improvement).
6. Create a new Pull Request.

