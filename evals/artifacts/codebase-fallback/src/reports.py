EXPORT_COLUMNS = ("account_id", "revenue")
SUPPORTED_FORMATS = ("pdf",)

def export_report(user, rows, date, region, format="pdf"):
    if user.role != "admin":
        raise PermissionError("Only admins can export")
    if format not in SUPPORTED_FORMATS:
        raise ValueError("Unsupported format")
    return [{key: row[key] for key in EXPORT_COLUMNS} for row in rows
            if row["date"] == date and row["region"] == region]
