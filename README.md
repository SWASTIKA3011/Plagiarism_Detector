This repository contains a Python script for detecting plagiarism between two text files. The script compares the contents of two files and determines the percentage of similarity between them.

Usage:
To use this script, follow these steps:
1. Place the two text files you want to compare in the specified file paths:
   > text1.txt in /file_path/Plagiarism_Detector.py/
   > text2.txt in /file_path/Plagiarism_Detector.py/
2. Open the Python script Plagiarism_Detector.py and locate the following code:
   > file1 = open(r"/file_path/Plagiarism_Detector.py/text1.txt")
   > file2 = open(r"/file_path/Plagiarism_Detector.py/text2.txt")
   Replace /file_path/Plagiarism_Detector.py/ with the actual file paths where you placed the text files.
3. Run the script using a Python interpreter.
4. The script will compare the contents of the two files and display the following results:
   > The copied sentences found in text2.txt
   > The percentage of plagiarism between the two files

Note:
  > The script treats each sentence as a separate entity for comparison.
  > The script uses a simple matching approach, checking if each sentence in text1.txt exists in text2.txt.
  > The script assumes that sentences are separated by periods ('.').
  > The script counts the total number of sentences in text1.txt and compares them to find the percentage of plagiarism.
