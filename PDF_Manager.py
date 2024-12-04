import os
from PyPDF2 import PdfReader, PdfWriter

CLICK_ANYTHING = "Click anything to continue..."

def split_pdf(pdf_file, number_of_splits, output_names, prefix):
    if not os.path.exists(pdf_file):
        print(f"File '{pdf_file}' does not exist.")
        return

    try:
        reader = PdfReader(pdf_file)
        total_pages = len(reader.pages)
    
        pages_per_split = total_pages // number_of_splits
        remainder = total_pages % number_of_splits

        print(f"Total Pages\t: {total_pages}")
        print(f"Pages Per Split\t: {pages_per_split}")
        print(f"Extra Pages\t: {remainder}")

        start_page = 0
        created_files = []
        for split_num in range(number_of_splits):
            writer = PdfWriter()
            end_page = start_page + pages_per_split + (1 if remainder > 0 else 0)
            remainder -= 1

            for page_num in range(start_page, min(end_page, total_pages)):
                writer.add_page(reader.pages[page_num])

            output_file = f"{prefix + ' ' if prefix else ''}{output_names[split_num]}.pdf"
            with open(output_file, "wb") as output_pdf:
                writer.write(output_pdf)

            abs_output_file = os.path.abspath(output_file)
            created_files.append(abs_output_file)
            print(f"Created\t\t: {output_file} (Pages {start_page + 1} to {min(end_page, total_pages)})")
            start_page = end_page
        
        input()
    except Exception as e:
        print(f"An error occurred: {e}")
        input(CLICK_ANYTHING)

def merge_pdfs(pdf_files, output_file):
    try:
        writer = PdfWriter()
        for pdf_file in pdf_files:
            if not os.path.exists(pdf_file):
                print(f"File '{pdf_file}' does not exist. Skipping.")
                continue
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)

        with open(output_file, "wb") as merged_pdf:
            writer.write(merged_pdf)

        print(f"Merged PDF created: {output_file}")
        input()
    except Exception as e:
        print(f"An error occurred while merging: {e}")
        input(CLICK_ANYTHING)
        
if __name__ == "__main__":
    print("PDF_Manager")
    print("Sekber PMVBI (Pemuda Buddhayana) Provinsi Sumatera Utara")
    print("="*30)
    print("1. Split a PDF")
    print("2. Merge PDFs")
    print("="*30)
    
    choice = input("Enter your choice (1 or 2): ").strip()
    os.system('cls')

    if choice == "1":
        pdf_name = input("Enter the PDF file name (with extension) \t: ").strip()
        try:
            splits = int(input("Enter the number of splits \t\t\t: "))
            prefix = input("Enter prefix of the name \t\t\t: ")
            os.system('cls')
            if splits <= 0:
                print("Number of splits must be a positive integer.")
            else:
                output_names = []
                print(f"Enter names for each of the {splits} splits:")
                for i in range(splits):
                    name = input(f"Enter name for part {i + 1} \t: ").strip()
                    output_names.append(name)
                    
                os.system('cls')
                split_pdf(pdf_name, splits, output_names, prefix)
        except ValueError:
            print("Invalid input for number of splits. Please enter a positive integer.")
            input(CLICK_ANYTHING)

    elif choice == "2":
        num_files = int(input("Enter the number of PDF files to merge \t\t: "))
        pdf_files = []
        for i in range(num_files):
            file_name = input(f"Enter the name of PDF file {i + 1} (with extension) \t: ").strip()
            pdf_files.append(file_name)

        output_file = input("Enter the output file name (with extension) \t: ").strip()
        os.system('cls')
        merge_pdfs(pdf_files, output_file)

    else:
        print("Invalid choice. Please select 1 or 2.")
        print("="*30)
        
    os.system('cls')
    print("End of Program")
    input()
    
    