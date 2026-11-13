import re
from typing import Dict, List

REGEX_PATTERNS = {
    # Matches standard and multi-part domain emails (e.g., .co.uk)
    "emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    
    # Matches http/https URLs with subdomains, paths, or query parameters
    "urls": r"https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s<>\"']*)?",
    
    # Matches (123) 456-7890, 123-456-7890, and 123.456.7890
    "phone_numbers": r"(?:\(\d{3}\)\s|\b\d{3}[-.])\d{3}[-.]\d{4}\b",
    
    # Matches 16-digit cards separated by spaces or hyphens
    "credit_cards": r"\b(?:\d{4}[ -]){3}\d{4}\b",
    
    # Matches 12-hour (1:00 AM - 12:59 PM) and 24-hour (00:00 - 23:59) formats
    "time": r"\b(?:(?:1[0-2]|0?[1-9]):[0-5]\d\s?[APap][Mm]|(?:[01]?\d|2[0-3]):[0-5]\d)\b",
    
    # Matches opening, closing, and self-closing HTML tags with attributes
    "html_tags": r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s+[a-zA-Z0-9_-]+(?:=(?:\"[^\"]*\"|'[^']*'|[^\s>]+))?)*\s*/?>",
    
    # Matches hashtags starting with a letter/underscore, avoiding pure numbers like #123
    "hashtags": r"(?<!\w)#[a-zA-Z_][a-zA-Z0-9_]*\b",
    
    # Matches dollar amounts with proper comma grouping ($1,234.56) or plain digits ($19.99)
    "currency": r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?\b"
}


def extract_all_data(raw_text: str) -> Dict[str, List[str]]:
    """Extracts all 8 data types from a given string using compiled regex patterns."""
    extracted_results = {}
    for category, pattern in REGEX_PATTERNS.items():
        extracted_results[category] = re.findall(pattern, raw_text)
    return extracted_results