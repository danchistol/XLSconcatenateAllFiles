
import os
import pandas as pd

input_folder = r"ExcelFiles"
output_file = "output.xlsx"

def clean_text(value):
    import re
    if isinstance(value, str):
        value = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F\uFFFE\uFFFF]', '', value)
        value = ''.join(c for c in value if c.isprintable())  
    return value

if not os.path.exists(input_folder):
    print(f"Eroare: Folderul '{input_folder}' nu există!")
    exit(1)

all_data = []

for file in os.listdir(input_folder):
    if file.endswith(".xls") or file.endswith(".xlsx"):
        file_path = os.path.join(input_folder, file)

        try:
            engine = "openpyxl" if file.endswith(".xlsx") else None

            if file.endswith(".xls"):
                try:
                    import xlrd
                    engine = "xlrd"
                except ImportError:
                    print(f"Eroare: xlrd nu este instalat! Instalează-l cu 'pip install xlrd'")
                    continue

            xls = pd.ExcelFile(file_path, engine=engine)

            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)

                cols = df.select_dtypes(include=["object", "str"]).columns
                df[cols] = df[cols].map(clean_text)

                df["Sursa"] = file
                df["Sheet"] = sheet_name

                all_data.append(df)

        except Exception as e:
            print(f"Eroare la citirea fișierului {file}: {e}")

if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_excel(output_file, index=False, engine="openpyxl")
    print(f"Fișierul combinat a fost salvat ca '{output_file}'")
else:
    print("Nu s-au găsit fișiere .xls sau .xlsx valide în directorul specificat.")
