import json
from translate import translate_text
from validate import validate_request


def lambda_handler(event, context):
    try:
        valid, message = validate_request(event)

        if not valid:
            return {"statusCode": 400, "body": message}

        output = translate_text(
            text=message["text"],
            source_lang=message["source_lang"],
            target_lang=message["target_lang"],
        )

        return {"statusCode": 200, "body": json.dumps({"message": output})}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Error translating text: {e}"}),
        }
