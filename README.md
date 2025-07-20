# CleanMate – Smart File Organizer & Summarizer

A smart file organization tool built for the AWS Q Developer Challenge #1 that helps remote workers and students manage digital clutter.

## Problem Solved

Digital clutter across desktops and Downloads folders leads to disorganization, reduced productivity, and wasted time searching for files. CleanMate solves this by automatically organizing files into smart folders based on both file type and content.

## What CleanMate Does

- **Automatic File Organization**: Scans and moves files into smart folders (e.g., PDFs, Images, Videos, Code, etc.) based on file type.
  
- **Content-Based Intelligence**: Uses AWS Q Developer CLI to summarize the content of supported files (PDFs, TXT, DOCX) and intelligently suggest or rename folders (e.g., "Project Reports", "Assignments", "Bills").
  
- **Cleanup Tracking**: Maintains a cleanup log with timestamps and summary reports.
  
- **Scheduled Cleaning**: Can be scheduled to run daily or weekly with a single CLI command.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cleanmate.git
   cd cleanmate
   ```

2. Make sure you have Python 3.6+ installed.

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Make the script executable:
   ```
   chmod +x src/cleanmate.py
   ```

5. Make sure you have AWS Q Developer CLI installed and configured.

## Usage

### Basic Usage

```bash
python src/cleanmate.py
```

This will organize files from your Desktop and Downloads folders (default) into the `~/CleanMate/Organized` directory.

### Advanced Options

```bash
# Use a custom configuration file
python src/cleanmate.py --config /path/to/custom_config.json

# Perform a dry run (no files will be moved)
python src/cleanmate.py --dry-run

# Specify a source folder to organize
python src/cleanmate.py --source ~/Downloads

# Specify both source and destination folders
python src/cleanmate.py --source ~/Downloads --dest ~/Organized_Files
```

### Scheduling with Cron

To run CleanMate automatically every day at 8 PM:

```bash
crontab -e
```

Add the following line:

```
0 20 * * * /path/to/cleanmate/src/cleanmate.py
```

## Configuration

The default configuration is stored in `~/CleanMate/config/config.json`. You can modify this file to customize CleanMate's behavior.

Key configuration options:

- `source_directories`: List of directories to scan for files
- `destination_directory`: Where organized files will be placed
- `file_categories`: File extensions and their corresponding categories
- `summarize_extensions`: File types that should be summarized
- `organize_by_content`: Whether to create smart folders based on file content
- `smart_rename`: Whether to suggest folder names based on content

## How It Works

1. **Scanning**: CleanMate scans the specified source directories for files.

2. **Categorization**: Files are first categorized by their extension (e.g., .pdf, .jpg, .mp4).

3. **Content Analysis**: For supported file types, CleanMate uses AWS Q Developer CLI to generate a summary of the file's content.

4. **Smart Organization**: Based on the content summary, CleanMate suggests appropriate folder names and organizes files accordingly.

5. **Reporting**: A detailed report is generated after each run, showing statistics and organization details.

## How AWS Q Developer Helped

AWS Q Developer CLI was instrumental in building CleanMate:

1. **Content Summarization**: Q Developer analyzes file content to create concise summaries.

2. **Intelligent Folder Naming**: Q Developer suggests appropriate folder names based on file content.

3. **Code Development**: Q Developer assisted in writing efficient Python code and handling edge cases.

4. **Error Handling**: Q Developer helped implement robust error handling and logging.

## Screenshots

[Include screenshots of CleanMate in action]

## Future Enhancements

- Integration with cloud storage services (Google Drive, Dropbox)
- Machine learning to improve folder suggestions over time
- GUI interface for easier configuration
- Support for more file types and languages

## License

MIT

## Author

Your Name

---

*This project was created for the AWS Q Developer Challenge #1 (July 2025)*
