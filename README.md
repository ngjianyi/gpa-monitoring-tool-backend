### Running the backend

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

3. Install dependencies for the project by entering this command:

```bash
python3 -m pip install -r requirements.txt
```

4. Seed the database

```bash
python3 seed.py
```

5. Run the app in development mode by entering this command:

```bash
flask run
```
