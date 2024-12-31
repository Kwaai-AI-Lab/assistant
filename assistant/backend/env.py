def check_env():
    import sys
    print("Running environment check inside Docker container.")
 
    required_modules = ['connexion', 'uvicorn', 'sqlalchemy', 'alembic', 'aiosqlite']
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Error: Required module '{module}' is not installed. Ensure it is included in the Docker image.")
            sys.exit(1)
 
    print("All required modules are installed. Environment is set up correctly.")
