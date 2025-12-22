import os
from PyPDF2 import PdfReader

# List of all PDF files
pdf_files = [
    r"c:\Users\David\CCNA3---Projeto-Final\topologia-CCNA2.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\mls1-2025110313412437.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\dhcp-2025110313405966.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\ap-zg-2025110313423657.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\sw2-zg-2025110313411620.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\rt1-zg-2025110313405247.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\mls2-2025110313415388.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\EnunciadoCCNA3.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\ZAGREB\sw1-zg-2025110313410926.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\PULA\sw1-pl-2025110313432264.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\PULA\rt1-pl-2025110313433157.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\SPLIT\sw1-st-2025110313400044.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\SPLIT\rt1-st-2025110313394961.pdf",
    r"c:\Users\David\CCNA3---Projeto-Final\SPLIT\ap-st-2025110313400713.pdf"
]

for pdf_path in pdf_files:
    try:
        # Read the PDF
        reader = PdfReader(pdf_path)
        
        # Extract text from all pages
        text_content = ""
        for page in reader.pages:
            text_content += page.extract_text() + "\n"
        
        # Create the output txt file path (same name, different extension)
        txt_path = pdf_path.replace('.pdf', '.txt')
        
        # Write the content to the txt file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
        
        print(f"✓ Created: {os.path.basename(txt_path)}")
        
    except Exception as e:
        print(f"✗ Error processing {os.path.basename(pdf_path)}: {str(e)}")

print("\nDone! Text files have been created for all PDFs.")
