import subprocess
import os

def build_package():
    """Build the package distribution."""
    print("Building the package...")
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)

def upload_package():
    """Upload the package to PyPI."""
    print("Uploading the package to PyPI...")
    # Prompt the user for their PyPI API token
    api_token = input("Enter your PyPI API token: ")
    
    # Set the API token as an environment variable for twine
    os.environ["TWINE_PASSWORD"] = api_token
    
    # Run the twine upload command
    subprocess.run(["twine", "upload", "dist/*"], check=True)

def main():
    """Main function to run the automation."""
    build_package()
    upload_package()
    print("Package successfully uploaded to PyPI!")

if __name__ == "__main__":
    main()
