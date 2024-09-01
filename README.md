#Audiobook Text-to-Speech Converter
Overview
This project is a simple Python application that converts the text content of a PDF file into speech. The application uses the PyPDF2 library to extract text from PDF files and the pyttsx3 library to convert the extracted text into speech. It provides a basic GUI using Tkinter to allow users to select the PDF file they want to convert.

Features
Extracts text from PDF files.
Converts the extracted text into speech.
Provides a simple file selection dialog for choosing the PDF file.
Prerequisites
Before running this application, ensure you have the following installed:

Python 3.x
Install required libraries: Install the required Python packages using pip:

pip install pyttsx3 PyPDF2 tkinter

A file dialog will open allowing you to select the PDF file you wish to convert into speech.
Listen to the audiobook:

The application will read out the text from the selected PDF file.
Code Overview
audiobook.py: Main script that handles the text-to-speech conversion.
pyttsx3: Library used for text-to-speech conversion.
PyPDF2: Library used for extracting text from PDF files.
Tkinter: Library used for creating the file selection dialog.
Troubleshooting
EOF Marker Not Found: If you encounter an error stating "EOF marker not found," it usually indicates that the PDF file is corrupted or incomplete. Try using a different PDF file.
Missing Libraries: Ensure that all required libraries are installed correctly. If a library is missing, you can install it using pip as shown above.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
