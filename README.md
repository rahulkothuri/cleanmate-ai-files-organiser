# CleanMate – Smart File Organizer & Summarizer

A smart file organization tool built for the AWS Q Developer Challenge #1 that helps remote workers and students manage digital clutter.

## Problem Solved

Digital clutter across desktops and Downloads folders leads to disorganization, reduced productivity, and wasted time searching for files. CleanMate solves this by automatically organizing files into smart folders based on both file type and content.

## What CleanMate Does

- **Automatic File Organization**: Scans and moves files into smart folders (e.g., PDFs, Images, Videos, Code, etc.) based on file type.
  
- **Content-Based Intelligence**: Uses Amazon Q CLI to summarize the content of supported files (PDFs, TXT, DOCX) and intelligently suggest or rename folders (e.g., "Project Reports", "Assignments", "Bills").
  
- **Cleanup Tracking**: Maintains a cleanup log with timestamps and summary reports.
  
- **Scheduled Cleaning**: Can be scheduled to run daily or weekly with a single CLI command.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rahulkothuri/cleanmate-ai-files-organiser.git
   cd cleanmate-ai-files-organiser
   ```

2. Make sure you have Python 3.6+ installed.

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Make the scripts executable:
   ```
   chmod +x src/cleanmate.py src/schedule_cleanmate.py
   ```

5. Make sure you have Amazon Q CLI installed and configured.

## Usage

### Basic Usage

```bash
python src/cleanmate.py --source path --dest path
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

# Clean up your Downloads folder and keep files organized within it
python src/cleanmate.py --source ~/Downloads --dest ~/Downloads/Organized
```

### Important Note

CleanMate now **moves** files instead of copying them. This means files will be removed from their original location and placed in the organized folders. Make sure you're aware of this behavior before running the tool. 
You can check the logs of the cleanmate for every cleanup in the cleanmate/logs folder.

### Scheduling Regular Cleanups

You can use the included scheduling helper to set up regular cleanups:

```bash
# Schedule daily cleanup
python src/schedule_cleanmate.py add daily

# Schedule weekly cleanup
python src/schedule_cleanmate.py add weekly

# Schedule with a specific time (e.g., 10:30 PM)
python src/schedule_cleanmate.py add daily --time 22:30

# List scheduled cleanups
python src/schedule_cleanmate.py list

# Remove scheduled cleanups
python src/schedule_cleanmate.py remove
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

3. **Content Analysis**: For supported file types, CleanMate uses Amazon Q CLI to generate a summary of the file's content.

4. **Smart Organization**: Based on the content summary, CleanMate suggests appropriate folder names and organizes files accordingly.

5. **Reporting**: A detailed report is generated after each run, showing statistics and organization details.

## How Amazon Q Helped

Amazon Q CLI was instrumental in building CleanMate:

1. **Content Summarization**: Amazon Q analyzes file content to create concise summaries.

2. **Intelligent Folder Naming**: Amazon Q suggests appropriate folder names based on file content.

3. **Code Development**: Amazon Q assisted in writing efficient Python code and handling edge cases.

4. **Error Handling**: Amazon Q helped implement robust error handling and logging.

## Screenshots
<img width="914" height="602" alt="before-org" src="https://github.com/user-attachments/assets/5103d931-7cdf-4bca-833d-c69e9221400d" />
<img width="1326" height="712" alt="terminal" src="https://github.com/user-attachments/assets/35c437b4-6e09-4cc4-b20a-da2c5099261a" />
<img width="915" height="604" alt="after-org" src="https://github.com/user-attachments/assets/94f26eb4-8f7a-43d8-a10e-d1eaeb89dd7b" />
<img width="640" height="414" alt="report" src="https://github.com/user-attachments/assets/064c32ed-3e66-4fe3-8c39-e553cace7aee" />


## Future Enhancements

- Integration with cloud storage services (Google Drive, Dropbox)
- Machine learning to improve folder suggestions over time
- GUI interface for easier configuration
- Support for more file types and languages
