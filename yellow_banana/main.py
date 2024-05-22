import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Interact with APIs using env variables and a prompt.'
    )
    parser.add_argument(
        'prompt',
        type=str,
        help='Prompt for the LLM'
    )
    args = parser.parse_args()

    from openai import OpenAI

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You only discuss yellow bananas."},
            {"role": "user", "content": args.prompt}
        ]
    )

    print(completion.choices[0].message.content)

if __name__ == '__main__':
    main()
