# PyQt5 Login & Registration App

A desktop application built with **Python** and **PyQt5** featuring user registration, login, and a home screen, backed by a PostgreSQL database.

![Login screen](login.png)

## Features

- User registration
- Login with credential check against the database
- Home page shown after successful login
- UI designed in Qt Designer (`.ui` files) with bundled icons via a Qt resource file

## Tech stack

- Python 3
- PyQt5 (UI + Qt Designer)
- PostgreSQL via `psycopg2` (see `Database.py`)

## Project structure

```
.
├── main.py            # App entry point
├── Login.py / .ui     # Login window
├── Register.py / .ui  # Registration window
├── HomePage.py / .ui  # Home window after login
├── Database.py        # PostgreSQL connection
├── resourc.qrc        # Qt resource file (icons)
└── feather/           # Icon set
```

## Getting started

```bash
git clone https://github.com/Jaysivaram/Pyqt5.git
cd Pyqt5
pip install PyQt5 psycopg2-binary mysql-connector-python
# Create a local PostgreSQL database and update the connection details in Database.py
python main.py
```

## What I learned

- Separating UI layouts (`.ui`) from application logic
- Handling navigation between multiple windows with signals and slots
- Connecting a desktop UI to a database layer
