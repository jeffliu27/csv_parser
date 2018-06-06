import re


# main parsing function
def parse_csv(currency_index, conversion_factor, file_name, new_file_name):
    with open(file_name + '.csv', 'r') as read_file:
        with open(new_file_name + '.csv', 'w') as write_file:
            print('opening %s' % read_file.name)  # prints the name of the file
            
            # the first row with data will have a line number of 2
            line_number = 2

            # detecting the number of columns
            column_names = read_file.readline().split(',')
            expected_num_of_col = len(column_names)

            # writes all the column names to the new file
            write_file.write(','.join(column_names))


            # parse csv file line by line
            for line in read_file:
                # removes all whitespace
                line = "".join(line.split())

                # cannot have an odd number of quotation marks (see function description for why)
                if check_quotation_odd(line, line_number):
                    break
                # checking if the line is not empty
                if line:
                    # replace the unnecessary quotations with spaces
                    line = line.replace('""', ' ')
                    # replace extraneous commas with tabs
                    line = replace_extraneous_commas(line)

                    # delimit with commas and quotations
                    string_list = re.split('[,\"]', line)

                    # remove all the blank strings
                    string_list = list(filter(None, string_list))

                    if len(string_list) != expected_num_of_col:
                        print('Line {} Error: Too many columns'.format(line_number))
                    else:
                        # convert currency column to euro
                        string_list[currency_index] = convert_to_euros(string_list[currency_index],
                                                                       conversion_factor, line_number)
                        # reinsert all the quotations and commas we took out
                        string_list = [(string.replace(' ', '""')).replace('\t', ',')
                                       if string != string_list[currency_index]
                                       else string
                                       for string in string_list]
                        # join the list together in a string with quotations and commas between each field
                        final_line = '"' + ('","'.join(string_list)) + '"' + '\n'
                        write_file.write(final_line)

                        # increment line number
                        line_number += 1
    return


# function: check if the number of quotation marks is odd
def check_quotation_odd(any_string, line_number):
    if any_string.count('"') % 2 != 0:
        print("Line {} Error: Unformatted quotation marks detected".format(line_number))
        return True
    else:
        return False


# function: replaces any commas that don't act as delimiters in .csv
def replace_extraneous_commas(any_string):
    # this function replaces all the extraneous commas with a '\t'
    string_list = list(any_string)
    quotation = '"'
    # list of positions where quotations are found
    position_of_quotation_list = [pos for pos, char in enumerate(string_list) if char == quotation]
    # for each pair of quotations, replace all the commas inside with '\t'
    for i in range(0, len(position_of_quotation_list), 2):
        index_of_extraneous_comma = 0

        # loop until no more extraneous commas
        while index_of_extraneous_comma > -1:
            index_of_extraneous_comma = any_string.find(',', position_of_quotation_list[i],
                                                        position_of_quotation_list[i + 1])
            if index_of_extraneous_comma > -1:
                any_string = any_string.replace(',', '', 1)
                string_list[index_of_extraneous_comma] = '\t'
    any_string = "".join(string_list)
    return any_string


def convert_to_euros(initial_string, conversion_factor, line_number):
    try:
        currency_in_euros = float(initial_string)
        currency_in_euros *= conversion_factor

        # format to euros
        string_currency_in_euros = ' '.join(['€', str(round(currency_in_euros, 2))])
        string_currency_in_euros = string_currency_in_euros.replace('.', ',')

        return string_currency_in_euros
    except:

        print('Line {} Error: invalid currency'.format(line_number))
        return initial_string
