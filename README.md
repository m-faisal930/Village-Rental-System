
# Village Rentals System

The Village Rentals System is a Python application built with Tkinter and MySQL. It provides a user-friendly interface for managing equipment rentals and client information.

## Features

Add Equipment: Allows users to add new equipment to the system, including details such as name, description, category, and daily rental cost.
Add Client: Enables users to add new clients with their personal information like last name, first name, contact phone, and email.
Delete Equipment: Provides functionality to delete equipment from the system. This action also removes any associated rentals.
Display Equipment: Displays all equipment currently available in the system.
Display Clients: Shows a list of all clients stored in the system.
Process Rental: Allows users to process a rental transaction by specifying the client, equipment, rental date, return date, and cost.

## Requirements

- Python 3.x
- MySQL Server
- MySQL Connector for Python
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/village-rentals.git
    ```

2. Install MySQL Server and create a new database named `village_rentals`.

3. Install the required Python packages:

    ```bash
    pip install mysql-connector-python
    ```

4. Run the application:

    ```bash
    python village_rentals.py
    ```

## Usage

1. Launch the application.
2. Use the tabs to navigate between different functionalities (Add Equipment, Add Client, Delete Equipment, Display Equipment, Display Clients, Process Rental).
3. Fill in the required information and click the corresponding buttons to perform actions like adding equipment or clients, deleting equipment, displaying data, or processing rentals.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
