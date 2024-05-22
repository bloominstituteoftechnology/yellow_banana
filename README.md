# Yellow Banana

Yellow Banana is as a template for creating PyPI packages.

In order to create your own package, replace all occurrences of the word "yellow_banana" in the codebase, and rename the `yellow_banana` folder, to whatever you want your package to be called.

## Development

1. Clone the repository:

    ```bash
    git clone https://github.com/bloominstituteoftechnology/yellow_banana.git
    cd yellow_banana
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Build and install the package:

    ```bash
    python setup.py sdist bdist_wheel
    pip install dist/yellow_banana-0.1.1-py3-none-any.whl
    ```

5. Run the package:

    ```bash
    export OPENAI_API_KEY="xyz"
    yellow_banana "What is the meaning of life?"
    ```

## Publishing

1. Make an account at [Pypi](https://pypi.org/) and set up their token in your environment.

2. Install Twine:

    ```bash
    pip install twine
    ```

3. Build the app:

    ```bash
    python setup.py sdist bdist_wheel
    ```

4. Upload to PyPI:

    ```bash
    twine upload dist/*
    ```

## Usage of the package

Install the package using pip:

```bash
pip install yellow_banana
```

Set your environment variable:

```bash
export OPENAI_API_KEY ="some_value"
```

Use the tool:

```bash
yellow_banana "What is the meaning of life?"
```
