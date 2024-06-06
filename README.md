# Instagram Login Checker

This script checks the login credentials for Instagram accounts from a CSV file and saves the result in a separate CSV file.

## Prerequisites

- Python 3.x
- requests library
- CSV library

## Installation

1. Download the script.
2. Install the required libraries using the command `pip install requests csv`.
3. Run the script.

## Usage

1. Create a CSV file with the login credentials for the Instagram accounts. The first column should contain the password and the second column should contain the username.
2. Run the script and enter the path to the CSV file when prompted.
3. The script will check the login credentials for each account and save the result in a file named "InstagramResult.csv".

## Notes

- Make sure to have a valid proxy configuration in the `proxies` variables if you want to use one.
- The headers in the `headers` variable may vary depending on the Instagram version. Update them accordingly to ensure the script works properly.

## License

This script is licensed under the MIT License. For more information, see the [License file](LICENSE).
