import re

class URLExtractor:
    def __init__(self, text):
        self.text = text

    def extract_urls(self):
        # Regular expression for extracting URLs
        url_pattern = r'http[s]?://(?:[\w-]+\.)+[\w-]+(?:/[^\s]*)?'
        return re.findall(url_pattern, self.text)

    def validate_url(self, url):
        # Check if the URL is valid
        pattern = re.compile(r'^(http://|https://).+')
        return pattern.match(url) is not None

# Example usage:
# email_content = 'Check this link: https://example.com'
# extractor = URLExtractor(email_content)
# urls = extractor.extract_urls()
# print(urls)  # Output: ['https://example.com']