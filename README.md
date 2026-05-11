# 📊 XLS Concatenate All Files

A lightweight Python utility that automatically merges multiple Excel files (`.xls` and `.xlsx`) into a single consolidated workbook.

Perfect for:

* 📁 Monthly reports
* 📈 Financial exports
* 🧾 ERP/CRM generated spreadsheets
* 🔄 Bulk Excel processing

---

## ✨ Features

* ✅ Reads both `.xls` and `.xlsx`
* ✅ Automatically scans a folder for Excel files
* ✅ Merges all sheets into one dataset
* ✅ Exports a clean `output.xlsx`
* ✅ Fast and simple
* ✅ Minimal dependencies

---

## 📂 Project Structure

```bash
XLSconcatenateAllFiles/
│
├── ExcelFiles/          # Put your Excel files here
├── output.xlsx          # Generated merged file
├── main.py              # Main script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/danchistol/XLSconcatenateAllFiles.git
cd XLSconcatenateAllFiles
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Place all Excel files inside:

```bash
ExcelFiles/
```

2. Run the script:

```bash
XLSconcatenateAllFiles.py
```

3. The merged file will be generated as:

```bash
output.xlsx
```

---

## 🧪 Supported Formats

| Format  | Supported |
| ------- | --------- |
| `.xlsx` | ✅         |
| `.xls`  | ✅         |

---

## 📦 Dependencies

Main libraries used:

* `pandas`
* `openpyxl`
* `xlrd`

---

## ⚡ Example Workflow

```text
ExcelFiles/
 ├── january.xlsx
 ├── february.xlsx
 ├── march.xls
```

⬇️

```text
output.xlsx
```

---

## 🛡️ .gitignore

The repository excludes:

* `.venv`
* `__pycache__`
* temporary Excel files
* IDE configs

---

## 🤝 Contributing

Pull requests are welcome.

If you find a bug or have ideas for improvements, feel free to open an issue.

---

## 📄 License

MIT License

---

## ⭐ Support

If this project helped you, consider giving it a star ⭐ on GitHub.
