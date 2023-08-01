# Extract Links and Text Messages from JSON and Save to CSV

## Description
This Python script is designed to extract image links, regular links, and text messages from a JSON file and then save the extracted data to a CSV file. It uses regular expressions to identify links and supports various image file formats such as PNG, JPG, JPEG, and GIF.

## How to Use
1. Ensure you have Python installed on your system.
2. Place the JSON file you want to process in the same directory as the Python script or provide the correct file path in the `json_file_path` variable.
3. Update the `output_csv_path` variable with the desired name for the CSV file where the results will be saved.
4. Run the script, and it will read the JSON file, extract the links and text messages, and save them to the specified CSV file.

## Dependencies
This script requires the `csv` and `json` modules, which are part of the Python standard library. No external libraries are needed.

## Function: `extract_links_and_text(json_data)`
This function takes a JSON data string as input and returns three lists: `image_links`, `regular_links`, and `text_messages`. Each list contains the corresponding extracted data. Image links are links to image files (ending with .png, .jpg, .jpeg, or .gif), regular links are other URLs, and text messages contain unique text messages found in the JSON data.

## Note:
- Make sure to replace `"filename.json"` and `"csv_name.csv"` with the appropriate file paths or names.
- If you encounter any issues or have questions, feel free to reach out for support.

## Important Considerations
- This script assumes that the JSON data provided adheres to the expected structure and contains the necessary information for link extraction. Ensure that the JSON data is in the correct format.
- The regular expression used for link extraction may not cover all edge cases. Depending on the data you are processing, it might be necessary to adjust the regular expression to accommodate specific link formats.
- The script uses a set to store text messages to avoid duplicates. If maintaining the order of text messages is essential, consider using a different data structure (e.g., a list) and modify the code accordingly.
- Remember to handle any potential exceptions and edge cases in your specific implementation as needed.

