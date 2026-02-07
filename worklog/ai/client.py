import os, sys
from openai import OpenAI


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print(
            "\n⚠️  OpenAI API key not configured.\n\n"
            "AI features are disabled until you set an API key.\n\n"
            "Set it using:\n"
            '  export OPENAI_API_KEY="your-api-key"\n\n'
            "Then re-run the command.\n"
        )
        sys.exit(1)

    return OpenAI(api_key=api_key)