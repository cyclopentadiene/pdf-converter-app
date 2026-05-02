import pymupdf4llm
import pathlib
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_pdf_paginated(pdf_path, output_md_path, image_folder):
    """Extracts text, tables, and images while maintaining strict page boundaries."""
    try:
        pathlib.Path(image_folder).mkdir(parents=True, exist_ok=True)
        
        # The magic parameter: page_chunks=True
        md_pages = pymupdf4llm.to_markdown(
            doc=pdf_path,
            page_chunks=True,            
            write_images=True,
            image_path=image_folder
        )
        
        # Write the paginated Markdown to your file
        with open(output_md_path, "w", encoding="utf-8") as file:
            file.write(f"# Extracted Content from {os.path.basename(pdf_path)}\n\n")
            
            for i, chunk in enumerate(md_pages):
                page_num = i + 1 
                page_text = chunk.get("text", "")
                
                file.write(f"## Page {page_num}\n\n")
                file.write(page_text)
                file.write("\n\n---\n\n")
                
        return True, image_folder
        
    except Exception as e:
        return False, str(e)

def run_conversion():
    # 1. Ask the user to select the input PDF
    pdf_path = filedialog.askopenfilename(
        title="Select PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not pdf_path:
        return # User cancelled

    # 2. Ask the user where to save the Markdown file
    md_path = filedialog.asksaveasfilename(
        title="Save Markdown As",
        defaultextension=".md",
        filetypes=[("Markdown Files", "*.md")]
    )
    if not md_path:
        return # User cancelled

    # 3. Automatically determine the image folder based on the md file name
    base_dir = os.path.dirname(md_path)
    md_filename = os.path.splitext(os.path.basename(md_path))[0]
    image_dir = os.path.join(base_dir, f"{md_filename}_images")

    # 4. Update UI and run
    status_label.config(text="Processing... Please wait.")
    root.update() # Force UI to show the processing text

    success, result = extract_pdf_paginated(pdf_path, md_path, image_dir)

    if success:
        status_label.config(text="Success!")
        messagebox.showinfo("Success", f"Markdown saved!\n\nImages saved to:\n{result}")
    else:
        status_label.config(text="An error occurred.")
        messagebox.showerror("Error", f"Failed to extract:\n{result}")

# --- Lightweight Mac GUI Setup ---
root = tk.Tk()
root.title("PDF to MD")
root.geometry("300x150")
root.eval('tk::PlaceWindow . center') # Center on screen

label = tk.Label(root, text="PDF to Markdown Converter", font=("Arial", 14))
label.pack(pady=15)

convert_btn = tk.Button(root, text="Select PDF & Convert", command=run_conversion)
convert_btn.pack(pady=5)

status_label = tk.Label(root, text="", fg="gray")
status_label.pack(pady=10)

root.mainloop()