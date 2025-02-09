# IPv4 Address Validator

## About the Project
This project implements a Python script to validate IPv4 addresses. It uses regular expressions to check the format and ensures that each octet is within the valid range (0-255).

## How It Works
1. The script prompts the user to input an IPv4 address.
2. It uses a regular expression to check if the input matches the IPv4 format.
3. If the format is correct, it further validates that each octet is between 0 and 255.
4. The script returns True for valid IPv4 addresses and False for invalid ones.

## Getting Started

### Prerequisites
- Python 3.x
- pytest (for running tests)

### Installation
1. Clone the repository:

git clone https://github.com/BernardoMarta/IPv4_validator
cd IPv4_validator

2. Install pytest (if not already installed):

pip install pytest

## Usage
Run the script from the command line:

python numb3rs.py

Enter an IPv4 address when prompted.

## Running Tests
To run the unit tests:

pytest test_numb3rs.py

## Example

**Input:**
When prompted, enter an IPv4 address, e.g., "192.168.0.1"

**Output:**
The script will print True for valid IPv4 addresses and False for invalid ones.

## Features
- IPv4 address validation using regular expressions
- Octet range checking (0-255)
- Unit tests for various scenarios

## Contributing
Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/IPv4_validator)!

## License
This project is licensed under the MIT License.

## Acknowledgments
Inspired by the need for robust IPv4 address validation in network-related applications.
