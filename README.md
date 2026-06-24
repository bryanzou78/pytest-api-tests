# pytest-api-tests

API contract tests for the [RAWG Video Games Database API](https://rawg.io/apidocs) using Python and pytest.

Built as a companion testing project to [react-ecom-shop](https://github.com/bryanzou78/react-ecom-shop), which consumes the same API. Where that project covers browser-based e2e testing with Cypress, this project covers API-level contract testing in Python.

## Tech Stack

- Python 3.10
- pytest
- requests
- python-dotenv

## Getting Started

```bash
# Clone the repo
git clone git@github.com:bryanzou78/pytest-api-tests.git
cd pytest-api-tests

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your RAWG API key
cp .env.example .env
# Edit .env and add your key: RAWG_API_KEY=your_key_here
```

## Running Tests

```bash
pytest
```

## Tests

3 tests covering core RAWG API endpoints — single game fetch, 404 error handling, and games list response shape.