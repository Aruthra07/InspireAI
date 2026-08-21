import json
import random
import logging
import boto3

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS Clients
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
ses = boto3.client("ses", region_name="us-east-1")

# Configuration
MODEL_ID = "amazon.nova-lite-v1:0"

SENDER_EMAIL = "YOUR_VERIFIED_EMAIL@gmail.com"
RECIPIENT_EMAIL = "YOUR_VERIFIED_EMAIL@gmail.com"

# Prompt ideas
PROMPTS = [
    "Write an inspiring motivational message to help someone begin their day with confidence.",
    "Generate a short motivational quote that encourages perseverance and personal growth.",
    "Write a positive morning affirmation that inspires productivity and optimism.",
    "Create an uplifting message reminding someone to stay focused on their dreams.",
    "Write an encouraging motivational thought for students and young professionals."
]


def generate_motivation():

    prompt = random.choice(PROMPTS)

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    )

    motivation = response["output"]["message"]["content"][0]["text"]

    return motivation


def send_email(message):

    subject = "🌅 Your Daily AI Motivation | InspireAI"

    body = f"""
Hello!

Here's your AI-generated motivation for today.

--------------------------------------------

{message}

--------------------------------------------

Have an amazing day!

Generated automatically by InspireAI 🚀
Powered by Amazon Bedrock + AWS Lambda
"""

    ses.send_email(
        Source=SENDER_EMAIL,
        Destination={
            "ToAddresses": [
                RECIPIENT_EMAIL
            ]
        },
        Message={
            "Subject": {
                "Data": subject
            },
            "Body": {
                "Text": {
                    "Data": body
                }
            }
        }
    )


def lambda_handler(event, context):

    logger.info("InspireAI execution started.")

    try:

        motivation = generate_motivation()

        logger.info("Motivation generated successfully.")

        send_email(motivation)

        logger.info("Email sent successfully.")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email sent successfully.",
                "motivation": motivation
            })
        }

    except Exception as error:

        logger.error(str(error))

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(error)
            })
        }
