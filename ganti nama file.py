# Script untuk mengganti nama file di folder tertentu, sesuai dengan format yang diinginkan

import os
from pathlib import Path
import re

# Folder lo
folder_path = Path("C:/Users/MyBook Hype AMD/Downloads/RKA 2027")

# Ambil file dan urutin dari waktu modifikasi
files = sorted(folder_path.iterdir(), key=lambda f: f.stat().st_mtime)

# Pola buat motong bagian awal (dari 'Sistem Informasi...' sampai kode 5.x.x.x)
pattern = r"Sistem Informasi Pemerintahan Daerah - Cetak RKA Rincian Belanja [\d\.]+ "

# Proses rename
for i, file in enumerate(files, start=1):
    if file.is_file():
        original_name = file.stem  # nama file tanpa ekstensi
        ext = file.suffix          # ekstensi file
        
        # Hapus bagian depannya pake regex
        new_name_part = re.sub(pattern, '', original_name).strip()
        new_name = f"{i}. {new_name_part}{ext}"
        
        # Rename
        new_path = file.with_name(new_name)
        print(f"Renaming: {file.name} -> {new_name}")
        file.rename(new_path)
