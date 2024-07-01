import json
import pdfplumber

def parse_pdf_to_json(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Get the document name
        doc_name = pdf_path.split('/')[-1]
        
        # Get the total number of pages
        total_pages = len(pdf.pages)
        
        # Initialize the data list
        data = []
        
        # Iterate through each page
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            
            # Ensure the text is properly encoded
            if text:
                text = text.encode('utf-8', errors='ignore').decode('utf-8')
            
            # Append the page data to the list
            data.append({
                "page_num": page_num,
                "text": text
            })
        
        # Create the final JSON structure
        result = {
            "doc_name": doc_name,
            "total_pages": total_pages,
            "data": data
        }
        
        
        return result
    
    # Example usage
pdf_path = r".\data\ConceptsofBiology-WEB.pdf"
result = parse_pdf_to_json(pdf_path)


with open(".\data\parse_result_v2.json", 'w', encoding='utf-8') as jfile:
    json.dump(result, jfile, indent=4, ensure_ascii=False)
