# ComicsHelper

A macOS desktop application for managing and organizing your digital comic book collection. Automatically tracks your reading list, sorts new releases, and maintains a database of your comics library.

## Features

- **Automated Comic Organization**: Crawls directories and sorts comics by series
- **Reading List Management**: Tracks which series you're following and which issues you own
- **Database Creation**: Parses comic filenames to build structured JSON database
- **GUI Interface**: PyQt5-based graphical interface for easy interaction
- **Smart File Parsing**: Extracts series names and issue numbers from various filename formats
- **New Issue Detection**: Identifies first issues and standalone comics for review

## Tech Stack

- **Python 3.x**
- **PyQt5**: Modern GUI framework
- **tkinter**: Alternative GUI implementation
- **JSON**: Database storage

## Project Structure

```
ComicsHelper/
├── main.py                        # Application entry point
├── setup.py                       # Package configuration
├── helpers/
│   ├── database_handling.py       # JSON database CRUD operations
│   ├── file_crawlers.py           # Directory scanning & file parsing
│   ├── gui.py                     # PyQt5 interface
│   ├── old_gui.py                 # Legacy tkinter interface
│   └── text_parser.py             # Filename parsing logic
├── database/
│   ├── database.json              # Main comics database
│   ├── database-test.json         # Test environment
│   └── database backup.json       # Backup copy
└── ComicsHelperIcon.icns          # macOS app icon
```

## Key Functionality

### Database Management (`database_handling.py`)
- **Create Database**: Scans comic directory and builds JSON index
- **Write Database**: Adds new comics and issues to tracking
- **Check Database**: Validates if a comic is in reading list

### File Crawling (`file_crawlers.py`)
- Scans weekly comic folders
- Identifies standalone issues and first issues for manual review
- Automatically sorts comics into reading list
- Handles various filename formats and edge cases

### Text Parsing (`text_parser.py`)
- Extracts series names from filenames
- Parses issue numbers (including special formats like annuals, TPBs)
- Handles edge cases like publisher prefixes and special characters

## Setup

1. Install dependencies:
```bash
pip install PyQt5
```

2. Run the application:
```bash
python main.py
```

3. Build as macOS app:
```bash
python setup.py py2app
```

## Usage Workflow

### Initial Setup
1. Create database from existing comic collection:
```python
database.create_database()
```

2. Database structure:
```json
{
  "Batman": ["Batman #0", "Batman #1", "Batman #2"],
  "Spider-Man": ["Spider-Man #0", "Spider-Man #1"]
}
```

### Weekly Comics Management
1. Specify the new week's folder
2. Application sorts comics into:
   - **Reading List**: Matches existing series in database
   - **First Issues**: New series (#1) for manual review
   - **Standalones**: One-shots and graphic novels

3. Review and approve first issues
4. Add approved series to reading list

## Database Format

```json
{
  "Series Name": [
    "Series Name",           // Base entry
    "Series Name #1",        // Issue tracking
    "Series Name #2",
    "Series Name Annual #1"
  ]
}
```

## Filename Parsing Examples

Supported formats:
- `Batman #1 (2024).cbz`
- `Amazing Spider-Man 001 (2023).cbr`
- `Detective Comics Annual #1.cbz`
- `Batman - The Long Halloween.cbz`

## Configuration

Default paths (customizable):
```python
MAIN_PATH = '/Users/oleksiikol/Desktop/temp current comics/'
DATABASE_PATH = '/Users/oleksiikol/Documents/ComicsHelper/database/database.json'
```

## GUI Features

- Browse and manage comic library
- Add/remove series from reading list
- View statistics and collection overview
- Batch operations on comics

## Limitations

- macOS specific (uses .icns icons and macOS paths)
- Requires consistent filename formatting
- Manual review needed for edge cases

## Future Enhancements

- [ ] Cross-platform support (Windows, Linux)
- [ ] Cloud sync for reading lists
- [ ] Integration with ComicVine API for metadata
- [ ] Cover art display and management
- [ ] Reading progress tracking
- [ ] Export reading list to various formats

## Building for Distribution

```bash
# Create standalone macOS app
python setup.py py2app

# Output: dist/ComicsHelper.app
```

## License

Personal project - educational purposes

## Author

Oleksii Kolumbet
