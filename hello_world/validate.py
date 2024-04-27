import json


def validate_request(event):
    """Validate the request body and return an error if invalid"""

    body = event.get("body", False)

    if not body:
        return False, json.dumps({"message": "Invalid body"})

    text = json.loads(body).get("text", False)

    if not text:
        return False, json.dumps({"message": "Invalid/Missing text"})

    source_lang = json.loads(body).get("source_lang", False)

    if not source_lang or source_lang not in ["en", "hi", "fr", "es", "gr", "ja", "auto"]:
        return False, json.dumps({"message": "Invalid/Missing source language"})

    target_lang = json.loads(body).get("target_lang", False)

    if not target_lang or target_lang not in ["en", "hi", "fr", "es", "gr", "ja"]:
        return False, json.dumps({"message": "Invalid/Missing target language"})

    if source_lang == target_lang:
        return False, json.dumps(
            {"message": "Source and target language cannot be the same"}
        )

    return True, {"text": text, "source_lang": source_lang, "target_lang": target_lang}
