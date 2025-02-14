# Basic Server

> **Note**: This project is no longer maintained (since January 2020) and is preserved here as a showcase of past work. The code may need updates to work with current website structures and Python dependencies.

## Overview

This is a simple Python-based HTTP server that provides basic authentication functionality. It can be used to quickly share files or serve a small web application while requiring users to enter a username and password.

## Features
- **Basic Authentication**: Users must enter a valid username and password to access the server, providing a layer of security for shared files and applications.
- **File Sharing**: The server allows users to share files easily, making it suitable for quick file transfers.
- **Small Web Application Serving**: It can serve small web applications, allowing developers to test their applications locally.

## Functionality
1. **Starting the Server**: The server can be started from the command line, specifying authentication credentials and optional binding address and port.
2. **Access Control**: Only authenticated users can access the files and applications hosted on the server.
3. **File Management**: Users can upload and download files through the server interface.

## Installation and Setup
1. Ensure you have Python 3 installed on your system.
2. Clone the repository or download the `basic-server.py` file.
3. Navigate to the directory containing the `basic-server.py` file.
4. Run the server using the following command:

   ```bash
   python basic-server.py --username <your_username> --password <your_password> [--bind <address>] [--port <port>]
   ```
   - `--username` and `--password` are required to set the authentication credentials.
   - `--bind` (optional) specifies the IP address to bind the server to (default is `127.0.0.1`).
   - `--port` (optional) specifies the port to run the server on (default is `8000`).

## Usage Examples
- To start the server, run:
   ```bash
   python basic-server.py --username admin --password secret
   ```
- Access the server from a web browser at `http://127.0.0.1:8000`.

## Author

Jared I. Raga 2018
