import boto3

client = boto3.client("translate")

def translate_text(text, source_lang, target_lang):
    """Function to translate text using AWS Translate service"""
    try:
        response = client.translate_text(
            Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang
        )
        return response["TranslatedText"]
    except Exception as e:
        return f"Error translating text: {e}"
