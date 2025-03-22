# Selenium Automation Script

## Overview
This script automates the login process and customer addition on the Automation Playground CRM website using Selenium WebDriver.

## Prerequisites
Ensure you have the following installed before running the script:

- Python (version 3.x recommended)
- Google Chrome browser
- Chrome WebDriver (compatible with your Chrome version)
- Selenium library

## Installation
1. Install Python if not already installed: [Download Python](https://www.python.org/downloads/)
2. Install Selenium via pip:
   ```sh
   pip install selenium
   ```
3. Download and set up Chrome WebDriver:
   - Visit [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)
   - Ensure it matches your Chrome version
   - Add the WebDriver path to system environment variables (if necessary)

## Usage
1. Clone or download the script to your local machine.
2. Update the following variables in the script as needed:
   - `Email_Address`: Your login email
   - `password`: Your login password
   - `first_name`, `last_name`, `city`, `state_of_origin`: Customer details
3. Run the script:
   ```sh
   python script_name.py
   ```

## Script Workflow
1. Opens the CRM login page.
2. Enters login credentials and submits the form.
3. Navigates to the customer creation page.
4. Fills in customer details.
5. Selects the gender and promo code options.
6. Submits the form.

## Notes
- The script includes `time.sleep(wait)` for handling delays. You may optimize this by implementing `WebDriverWait` for better efficiency.
- Ensure the WebDriver is updated to avoid compatibility issues.
- Modify the element locators if the website structure changes.

## License
This script is free to use and modify for educational and testing purposes.