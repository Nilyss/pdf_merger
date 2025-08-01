#!/usr/bin/env python3

import os
import sys
import re
from pathlib import Path
from pypdf import PdfWriter, PdfReader

def merge_pdfs(source_dir="source", output_dir="output", output_filename="merged.pdf"):
    source_path = Path(source_dir)
    output_path = Path(output_dir)
    
    if not source_path.exists():
        print(f"Erreur: Le dossier source '{source_dir}' n'existe pas.")
        return False
    
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
    
    def natural_sort_key(path):
        parts = re.split(r'(\d+)', path.stem)
        return [int(part) if part.isdigit() else part.lower() for part in parts]
    
    pdf_files = sorted([f for f in source_path.glob("*.pdf")], key=natural_sort_key)
    
    if not pdf_files:
        print(f"Aucun fichier PDF trouvé dans le dossier '{source_dir}'.")
        return False
    
    print(f"Fichiers PDF trouvés: {[f.name for f in pdf_files]}")
    
    writer = PdfWriter()
    
    try:
        for pdf_file in pdf_files:
            print(f"Traitement de: {pdf_file.name}")
            reader = PdfReader(pdf_file)
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                writer.add_page(page)
        
        output_file = output_path / output_filename
        with open(output_file, 'wb') as output_pdf:
            writer.write(output_pdf)
        
        print(f"Fusion réussie! Fichier créé: {output_file}")
        return True
        
    except Exception as e:
        print(f"Erreur lors de la fusion: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = "source"
    
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = "output"
    
    if len(sys.argv) > 3:
        output_filename = sys.argv[3]
    else:
        output_filename = "merged.pdf"
    
    merge_pdfs(source_dir, output_dir, output_filename)