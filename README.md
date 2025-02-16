Deployment link: [Heroku Link](https://gpa-monitoring-tool-da929fb1fdda.herokuapp.com/)

Assumptions:

- Each student is taught by the same teacher for the entire schooling period of 8 semesters
- All students take the same course in each semester

## Running the backend locally

### 1. Create a virtual environment:

```bash
python3 -m venv .venv
```

### 2. Activate the virtual environment:

For Unix/macOS

```bash
source .venv/bin/activate
```

For Windows

```bash
py -m venv .venv
```

### 3. Install dependencies for the project by entering this command:

For Unix/macOS

```bash
python3 -m pip install -r requirements.txt
```

For Windows

```bash
py -m pip install -r requirements.txt
```

### 4. Seed the database

```bash
python3 seed.py
```

### 5. Run the app:

```bash
flask run
```
