import os
import mimetypes
from typing import List

class AttachmentHandler:
    def __init__(self, allowed_types: List[str]):
        self.allowed_types = allowed_types

    def is_safe_attachment(self, filename: str) -> bool:
        file_type, _ = mimetypes.guess_type(filename)
        return file_type in self.allowed_types

    def save_attachment(self, attachment: bytes, filename: str, save_dir: str) -> str:
        if not self.is_safe_attachment(filename):
            raise ValueError("Unsafe attachment type!")
        filepath = os.path.join(save_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(attachment)
        return filepath

    def scan_attachment(self, filepath: str):
        # Implement your scanning logic here
        pass
# Example usage:
# allowed_types = ['image/jpeg', 'image/png', 'application/pdf']
# handler = AttachmentHandler(allowed_types)
# handler.save_attachment(attachment_data, 'example.jpg', '/path/to/save')
