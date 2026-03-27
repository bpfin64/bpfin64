def handler(event, context):
    """Répond un message de bienvenue simple."""
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }
