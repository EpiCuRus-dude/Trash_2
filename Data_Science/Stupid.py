text = "This is the initial part of the text. Impression: Here is the part of the text that you want to extract, which continues until the end."


match = re.search(r'impression[:\s]*(.*)', text, re.IGNORECASE)


if match:
    extracted_text = match.group(1)
    print("Extracted Text:", extracted_text)
else:
    print("No 'impression' found in the text.")
