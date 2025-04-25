import os
import time
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "3"))


def cleanup_uploads(directory: str, days: int):
    now = time.time()
    cutoff = now - days * 86400

    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    deleted = 0
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            mtime = os.path.getmtime(file_path)
            if mtime < cutoff:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

    print(f"Cleanup complete. {deleted} files removed.")


if __name__ == "__main__":
    cleanup_uploads(UPLOAD_DIR, RETENTION_DAYS)
