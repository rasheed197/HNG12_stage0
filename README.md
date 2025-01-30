# Develop a Public API to Retrieve Basic Information
### Description
 A public API that returns the following information in JSON format
 1. Your registered email address (used to register on the HNG12 Slack workspace).
 2. The current datetime as an ISO 8601 formatted timestamp.
 3.  The GitHub URL of the project's codebase.
 
The programming language used for this project is python(fastapi).
The project was deployed to 
### Setup Instructions
1. Create a new directory in your PC
```
mkdir <directory_name>
```
2.  Navigate into this directory
```
cd <directory_name>
```
3. Create a virtual environment called **venv**

**Windows**
```
py -m venv venv
```
**Unix/MacOS**
```
py -m venv venv
```
4. Activate the virtual environment

**Windows**
```
venv\Scripts\activate.bat
```
**Unix/MacOS**
```
source venv/bin/activate
```
5. Install fastapi
```
pip install "fastapi[standard]"
```
6. Clone the github repo
```
git clone <repo-url>
```
7. Run server
```
fastapi dev main.py
```
8.  Visit the url http://127.0.0.1:8000
### API Documentation
1. Endpoint URL - http://127.0.0.1:8000/
2. Request Format - None
3. Response Format - JSON
```
{
  "email": "string",
  "current_datetime": "string",
  "github_url": "string"
}
```
### Backlink
https://hng.tech/hire/python-developers




















