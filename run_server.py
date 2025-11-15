"""
Simple server runner for Windows
This script runs the FastAPI application
"""
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    try:
        # Try to use uvicorn first
        import uvicorn
        print("Starting FastAPI server with uvicorn on http://localhost:8000")
        print("Press CTRL+C to stop the server")
        print("Visit http://localhost:8000/docs for API documentation")
        uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)
    except ImportError:
        print("Uvicorn not available. Please install dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
