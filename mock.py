import fitz  # PyMuPDF
import re

def extract_college_info(pdf_path):
    college_info = []

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through pages
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        
        # Extract text from the page
        page_text = page.get_text()

        print("Page Text:", page_text)  # Debugging print

        # Updated regex to find phone numbers (modify as needed)
        phone_regex = re.compile(r'\b\d{10}\b|\(\d{3}\)[\s.-]?\d{3}[\s.-]?\d{4}|\d{3}[\s.-]?\d{3}[\s.-]?\d{4}\b')

        # Find all phone numbers on the page
        numbers_on_page = phone_regex.findall(page_text)

        print("Phone Numbers on Page:", numbers_on_page)  # Debugging print

        # Check for text containing the name of the college
        if "Engineering & Technology" in page_text:
            # Add the found numbers and associated text to the list
            college_info.append({
                "phone_numbers": numbers_on_page,
                "text": page_text
            })

            print("Entered if condition")  # Debugging print

    # Close the PDF document
    pdf_document.close()

    return college_info

# Example usage
pdf_path = '/home/shahwaiz14/1656389673.pdf'
college_info = extract_college_info(pdf_path)

# Print the extracted information
for info in college_info:
    print(info["phone_numbers"])
    print("\n")

