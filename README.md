# Yellow Banana

Yellow Banana is a simple Python package that echoes back a message and an environment variable.

## Installation

Install the package using pip:

```bash
pip install yellow_banana
```

## Usage

```bash
yellow_banana "Hello, World!"
```

Make sure to set the environment variable MY_ENV_VAR before running the command.

```bash
export MY_ENV_VAR="some_value"
yellow_banana "Hello, World!"
```

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
    pip install dist/yellow_banana-0.1.0-py3-none-any.whl
    ```

5. Run the package:

    ```bash
    export MY_ENV_VAR="TestEnvironment"
    yellow_banana "Lady Gaga"
    ```

## Publishing

