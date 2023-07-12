import csv
import json
import re

def extract_links_and_text(json_data):
    image_links = []
    regular_links = []
    text_messages = set()  # Use a set to avoid duplicate text messages
    
    # Convert JSON data to Python dictionary
    data = json.loads(json_data)
    
    # Traverse the dictionary and search for links and text messages
    def find_links_and_text(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "text" and isinstance(value, str):
                    text_messages.add(value)
                elif isinstance(value, str):
                    # Use regular expression to find links
                    url_pattern = re.compile(
                        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+' 
                        r'[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+'
                        r'|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|'
                        r'(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'"'
                        r'.,<>?«»“”‘’]))'
                    )
                    matches = re.findall(url_pattern, value)
                    for match in matches:
                        if match[0].lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                            image_links.append(match[0])
                        else:
                            regular_links.append(match[0])
                elif isinstance(value, (dict, list)):
                    find_links_and_text(value)
        elif isinstance(obj, list):
            for item in obj:
                find_links_and_text(item)
    
    find_links_and_text(data)
    
    return list(set(image_links)), list(set(regular_links)), list(text_messages)

# Example usage
json_file_path = "filename.json"
output_csv_path = "csv name"

with open(json_file_path) as file:
    json_data = file.read()

image_links, regular_links, text_messages = extract_links_and_text(json_data)

# Save links and text messages to CSV file
with open(output_csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image Links', 'Regular Links', 'Text Messages'])  # Write column headers
    num_rows = max(len(image_links), len(regular_links), len(text_messages))
    for i in range(num_rows):
        if i < len(image_links):
            img_link = image_links[i]
        else:
            img_link = ""
        if i < len(regular_links):
            reg_link = regular_links[i]
        else:
            reg_link = ""
        if i < len(text_messages):
            text_msg = text_messages[i]
        else:
            text_msg = ""
        writer.writerow([img_link, reg_link, text_msg])  # Write links and text messages row by row
