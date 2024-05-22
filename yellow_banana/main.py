import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        description='Print a message using a CLI argument and an environment variable.'
    )
    parser.add_argument(
        'message',
        type=str,
        help='The message to print'
    )
    args = parser.parse_args()

    env_var = os.getenv('MY_ENV_VAR', 'default_value')

    print(f"Message: {args.message}")
    print(f"Environment Variable: {env_var}")

if __name__ == '__main__':
    main()
