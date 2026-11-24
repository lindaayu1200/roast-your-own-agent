"""Validate the bounty entry and copy it to the required output path."""

from pathlib import Path

entry_path = Path(__file__).with_name("entry.txt")
text = entry_path.read_text(encoding="utf-8")
content = text.rstrip("\r\n")
if any(separator in content for separator in ("\n", "\r", "\u2028", "\u2029")):
    raise ValueError("entry must contain one line")
if not 1 <= len(content) <= 200 or not content.strip():
    raise ValueError("entry must be 1-200 characters and contain non-whitespace text")

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "entry.txt"
output_path.write_text(text, encoding="utf-8")
print(f"{len(text.encode('utf-8'))} bytes")
