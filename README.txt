A csv parser converting USD to euros

Required: Python installed 
If Python is not installed, you can download Pythonhttps://www.python.org/downloads/ and click the add path variable

Steps: Open the command prompt and type in python ./csv_parser.py 
Then the program will guide you through the steps.

Since excel is the main program for csv, we will use excel standards for detecting any errors
this function does not deal with single quotation marks since Excel would couple the single " with another beside it

Assumptions:
    number of lines in file matches with the number of rows for csv
    if there is any commas in the field, the field must be enclosed with quotations

Make sure the csv file as well as the helper_functions_csv.py are in the same folder as the script

For Example: 

C:\Users>python ./csv_parser.py
Enter csv file name (no need to type .csv): USD_FILE
Enter the index of currency (1st Column is index 0): 1
Enter the euros conversion factor: 0.1
Enter new csv file name: EURO_FILE
Converting...
opening hello.csv
Done


