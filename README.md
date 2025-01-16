Baseball Statistics Filter Project

Overview

This Python project allows users to load and analyze baseball statistics from a CSV file. Users can filter the data based on specific criteria, such as setting minimum or maximum values for a chosen column. The project demonstrates data manipulation and user interaction through Python.

Features

Load baseball statistics from a CSV file.

Filter data based on user-specified criteria (e.g., hits greater than 2000).

Display filtered results in a user-friendly format.

Technologies Used

Python 3.8+

pandas (for data manipulation)

numpy (for numerical operations)

Installation

Clone the Repository

git clone https://github.com/yourusername/baseball-stats-filter.git
cd baseball-stats-filter

Set Up a Virtual Environment (Optional but recommended):

python -m venv venv
# Activate the virtual environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Place Your CSV File

Ensure the CSV file (e.g., baseball_stats.csv) is in the data/ folder. Replace the sample file with your own if needed.

Usage

Run the Script

python main.py

Follow the Prompts

The script will display the available columns from the CSV file.

Enter the column name you want to filter by.

Specify a minimum and/or maximum value for filtering (optional).

The filtered data will be displayed in the terminal.

Example

Suppose the CSV contains the following columns:

Player, Team, H (Hits), HR (Home Runs), RBI (Runs Batted In)

If you want to filter players with at least 2000 hits:

Enter H when prompted for the column.

Set the minimum value to 2000.

View the filtered results.

Project Structure

baseball_stats_project/
├── data/
│   └── baseball_stats.csv
├── main.py
├── requirements.txt
├── README.md

Future Improvements

Add support for multiple filters at once.

Provide sorting options (e.g., ascending or descending).

Create a graphical user interface (GUI).

Add export functionality to save filtered data to a new CSV file.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

pandas Documentation

Baseball Reference for potential data sources.