from datetime import datetime
# Get current timestamp
current_timestamp = datetime.now()
created_at = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
updated_at = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
deleted_at = None