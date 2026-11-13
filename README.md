# ALU Regex Data Extraction

## Project Overview
This project implements a Python-based regular expression engine designed to parse raw string responses from an aggregated web API. It extracts and validates eight core data types while filtering out malformed inputs and edge cases.

## Features & Extracted Data Types
1. **Email Addresses**: Standard and multi-level domain emails (`user@example.com`, `firstname.lastname@company.co.uk`).
2. **URLs**: `http` and `https` links including subdomains and paths.
3. **Phone Numbers**: Supports `(123) 456-7890`, `123-456-7890`, and `123.456.7890`.
4. **Credit Card Numbers**: 16-digit numbers delimited by spaces or hyphens.
5. **Time**: 24-hour (`14:30`) and 12-hour (`2:30 PM`) formats with strict hour/minute bounds.
6. **HTML Tags**: Opening, closing, and self-closing tags with quoted attributes.
7. **Hashtags**: Alphanumeric hashtags starting with a letter or underscore.
8. **Currency Amounts**: USD amounts with optional comma-grouped thousands and two-decimal cents.

## Prerequisites & Setup
- **Python 3.8+** (uses only the built-in `re` and `typing` standard libraries).

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/alu_regex-data-extraction-YourUsername.git](https://github.com/YourUsername/alu_regex-data-extraction-YourUsername.git)
   cd alu_regex-data-extraction-YourUsername