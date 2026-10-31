# Help Desk Ticketing System

## Project Overview

The Help Desk Ticketing System is a Python-based learning project that applies programming fundamentals to a practical IT support scenario. It is designed to help record, organise, and retrieve support requests raised by users.

Each ticket can contain information such as the user's name, department, reported issue, priority, ticket number, status, and support response. The application is organised into separate Python modules and currently uses a text file for persistent storage, allowing ticket records to remain available after the program closes.

This project is part of my ongoing effort to strengthen my Python programming skills by building a practical application and learning through implementation, debugging, and iterative improvement.

## Project Objectives

- Apply Python programming concepts to an IT support scenario.
- Separate functionality into individual Python modules.
- Practice using dictionaries and lists to organise ticket records.
- Implement basic input validation and exception handling.
- Create, view, and search support tickets.
- Store ticket information in a text file.
- Learn how to read, modify, and rewrite existing records safely.
- Establish a foundation for future interface, database, testing, and security improvements.

## Features

### 1. Create a Support Ticket
The ticket creation functionality collects relevant details about a support request, such as the user's name, department, issue description, and priority. The ticket number and other fields depend on the current implementation.

### 2. View Tickets
The application includes functionality for displaying existing ticket records so that support requests can be reviewed.

### 3. Search by Ticket Number
Users can search for a specific support request using its ticket number.

### 4. Text-File Storage
Ticket records are stored in a text file, providing basic persistence between application runs. The project explores reading records into Python, modifying a selected record, and writing the records back to the file.

### 5. Basic Input Validation
Exception handling is used to manage certain invalid inputs, such as a non-numeric ticket ID. The program also checks whether the ticket file exists before attempting to read it.

### 6. Modular Structure
The code is separated into modules for the main menu and ticket operations, making the project easier to follow and extend.

## Technologies and Python Concepts

- **Python 3** — main programming language.
- **Functions** — organise operations into reusable units.
- **Lists and dictionaries** — represent and manage ticket records.
- **Loops and conditional statements** — control program flow and search records.
- **Exception handling** — manage selected input errors.
- **File handling** — read and write ticket records.
- **`os` module** — check whether the ticket storage file exists.
- **`ast.literal_eval()`** — interpret stored Python literal representations of dictionaries.

## Project Structure

```text
HelpDesk/
├── main.py
├── create_ticket.py
├── view_ticket.py
├── Search_ticket.py
├── update_ticket.py
├── ASSESSMENT/
│   └── tickets.txt
└── README.md
```

| File or directory | Purpose |
|---|---|
| `main.py` | Displays the main menu and routes the user to an operation. |
| `create_ticket.py` | Contains ticket creation functionality. |
| `view_ticket.py` | Contains functionality for viewing ticket records. |
| `Search_ticket.py` | Contains functionality for searching by ticket ID. |
| `update_ticket.py` | Contains the developing ticket-update functionality. |
| `ASSESSMENT/tickets.txt` | Stores ticket records. |
| `README.md` | Documents the project and how to run it. |

*Adjust this structure if your actual filenames or folders differ. The update feature should be described as complete only after it has been implemented and tested successfully.*

## Installation and Setup

### Prerequisites
- Python 3
- A code editor or terminal
- A local copy of this repository

### 1. Clone the repository
Replace the placeholder with your actual repository URL:

```bash
git clone https://github.com/lanrekeele/CSC_44102_ASSESSMENT.git
```

### 2. Enter the project directory

```bash
cd HelpDesk
```

### 3. Check Python

```bash
python3 --version
```

### 4. Run the application

```bash
python3 main.py
```

The application should display a menu similar to:

```text
===== HELP DESK TICKET SYSTEM =====
1. Create a new ticket
2. View all tickets
3. Search for a ticket by ID
4. Update ticket
5. Exit
```

Select the relevant menu option and follow the prompts.

## Key Learning Outcomes

### Data structures
I have practised representing each ticket as a dictionary and managing multiple tickets with a list.

### Modular programming
I have separated different operations into individual Python files, improving readability and making the application easier to maintain.

### File handling
I have learned how to read records from a file and write information back to persistent storage. An important lesson is that opening a file in write mode (`"w"`) truncates its existing contents. To preserve other records when updating one ticket, all records must first be read into memory and then written back after the change.

### Input validation and debugging
I have practised handling invalid input and debugging issues caused by indentation, loop placement, variable assignment, file modes, and program control flow.

## Planned Enhancements

- Complete and test ticket updates.
- Add a Tkinter graphical user interface.
- Consider JSON or SQLite for more robust data storage.
- Validate ticket status and priority against allowed values.
- Add ticket assignment and reporting.
- Add automated tests for the main functions.
- Improve error handling and security controls.

## Limitations

This is a learning project, not a production-ready help desk platform. Text-file storage is useful for practising file handling but is not designed for concurrent users, large datasets, or complex access control. The application needs further validation, testing, and security improvements before it could be used for real organisational support data.

## Author

Developed as part of my ongoing Python learning journey, with an interest in practical IT support automation and software development fundamentals.

Feedback and constructive suggestions are welcome.

## License

No license has been specified yet. Add a suitable license if you intend to permit others to reuse the project.