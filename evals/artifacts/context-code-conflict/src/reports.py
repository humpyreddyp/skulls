SUPPORTED_FORMATS = ("pdf",)

def download(format):
    if format not in SUPPORTED_FORMATS:
        raise ValueError("Unsupported format")
    return "report"
