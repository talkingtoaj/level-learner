# Python Regular Expressions (RE) Tutorial

This project is an interactive web application designed to teach Python's regular expressions (RE) through a series of tutorials and quizzes. Users can progress through different levels, learning various aspects of regular expressions and testing their knowledge.

## Features

- Seven levels of tutorials covering different aspects of regular expressions
- Interactive quizzes for each level
- User progress tracking
- Dynamic tutorial navigation based on user's current level

## Technologies Used

- Python 3.12
- FastHTML: A Python library for creating HTML content
- HTMX: For dynamic content updates without full page reloads
- SQLite: For user data storage
- Pydantic: For data validation and settings management
- Markdown: For rendering tutorial content

## Project Structure

- `main.py`: The main application file containing route definitions and core logic
- `models.py`: Pydantic models for data structures
- `database.py`: Database operations using SQLite
- `content/`: Directory containing tutorial markdown files and quiz JSON files
- `static/`: Directory containing CSS styles

## Setup and Running

1. Ensure you have Python 3.12 installed.
2. Install the required packages:
   ```
   pip install python-fasthtml pydantic markdown
   ```
3. Run the application:
   ```
   python main.py
   ```
4. Open a web browser and navigate to `http://localhost:5001`

## Usage

1. Enter a username to start or continue your progress.
2. Read through the tutorial for each level.
3. Complete the quiz for each level to advance.
4. Use the tutorial buttons on the right to review previous levels.

## Contributing

Contributions to improve the tutorials, add more quiz questions, or enhance the application are welcome. Please submit a pull request with your changes.

## License

This project is open-source and available under the MIT License.