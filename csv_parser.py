# a csv parser converting USD to euros

# Since excel is the main program for csv, we will use excel standards for detecting any errors
# this function does not deal with single quotation marks since Excel would couple the single "
# with another beside it

# Assumptions:
#     number of lines in file matches with the number of rows for csv
#     if there is any commas in the field, the field must be enclosed with quotations

from helper_functions_csv import parse_csv

file_name = input("Enter csv file name (no need to type .csv): ")
str_currency_index = input("Enter the index of currency (1st Column is index 0): ")
str_conversion_factor = input("Enter the euros conversion factor: ")
new_file_name = input("Enter new csv file name: ")

print('Converting...')
try:
    # call csv parser
    currency_index = int(str_currency_index)
    conversion_factor = float(str_conversion_factor)
    parse_csv(currency_index, conversion_factor, file_name, new_file_name)

except:
    print('Conversion failed')
finally:
    print('Done')
