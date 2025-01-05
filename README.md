# HumanBenchmark Automation

This project automates tests on the [humanbenchmark.com](https://humanbenchmark.com) website using Selenium WebDriver. The tests include Click Speed, Typing Speed, Number Memory, and Verbal Memory.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/KdntNinja/HumanBenchmark.git
   cd HumanBenchmark
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your HumanBenchmark username and password:
   ```sh
   USERNAME=your_username
   PASSWORD=your_password
   ```

## Usage

1. Run the main script:
   ```sh
   python main.py
   ```

2. Follow the prompts to select the test you want to run and whether to run in headless mode.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request with a clear description of your changes.
