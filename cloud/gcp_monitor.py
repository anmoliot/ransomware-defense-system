def detect_gcp_iam_abuse(event):
    return "setIamPolicy" in event.get("methodName", "")
