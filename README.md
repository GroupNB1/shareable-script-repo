# shareable-script-repo

A simple FastAPI starter application for Windows.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files
2. Open Command Prompt or PowerShell in the project directory
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Using the batch file (Windows)
Simply double-click the `run_server.bat` file or run it from the command prompt:
```bash
run_server.bat
```

### Option 2: Using Python directly
```bash
python run_server.py
```

### Option 3: Using uvicorn directly
```bash
uvicorn app.app:app --reload --host 127.0.0.1 --port 8000
```

## Accessing the Application

Once the server is running, you can access:
- **Main page**: http://localhost:8000/
- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Returns a welcome message
- `GET /items/{item_id}` - Returns item information with optional query parameter

## Project Structure

```
shareable-script-repo/
├── app/
│   └── app.py          # Main FastAPI application
├── requirements.txt     # Python dependencies
├── run_server.py       # Python server runner
├── run_server.bat      # Windows batch script
└── README.md           # This file
```

## Troubleshooting

If you encounter any issues:
1. Make sure Python is installed and added to your PATH
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Check that port 8000 is not being used by another application