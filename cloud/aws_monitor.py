def detect_aws_iam_abuse(event):
    return event.get("eventName") in {"CreateAccessKey", "AttachUserPolicy", "PutUserPolicy"}
