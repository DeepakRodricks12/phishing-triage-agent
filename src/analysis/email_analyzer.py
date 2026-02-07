# email_analyzer.py

"""
A module to analyze email headers and content for phishing detection.
"""

import re

class EmailAnalyzer:
    def __init__(self, headers, body):
        self.headers = headers
        self.body = body

    def analyze_headers(self):
        "/"" Analyze email headers for known phishing indicators. "/""
        # Example check for sender domain
        sender = self.headers.get('From', '')
        if self.is_phishing_sender(sender):
            return "Phishing indicator found in headers"
        return "No phishing indicators in headers"

    def analyze_content(self):
        "/"" Analyze email content for phishing clues. "/""
        if self.contains_phishing_keywords(self.body):
            return "Phishing keywords found in email content"
        return "No phishing keywords in content"

    def is_phishing_sender(self, sender):
        phishing_domains = ["example.com", "scam.com"]  # Add real domains
        return any(domain in sender for domain in phishing_domains)

    def contains_phishing_keywords(self, body):
        phishing_keywords = ["urgent", "immediate action required", "click here"]
        return any(keyword in body.lower() for keyword in phishing_keywords)

# Example usage
if __name__ == '__main__':
    headers = {"From": "alert@example.com"}
    body = "Dear user, urgent action required! Click here to verify your account."
    analyzer = EmailAnalyzer(headers, body)
    print(analyzer.analyze_headers())
    print(analyzer.analyze_content())
