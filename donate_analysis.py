import csv
import gc
import os
import re

import pandas as pd
import pdfplumber

column = ['TNX Date', 'Credit', 'Transactions in Detail']
use_cols=['Ngày GD','Có','Mô tả giao dịch' ]
def split_to_db(data):
    data_temp = data[1:]
    #data_temp[0] = data_temp[0][10:]
    data_final = [data[0]]
    d1_temp=''
    for index1 in range(0, len(data_temp)):
        if index1 == 0:
            d_temp = data_temp[index1].split(' ')
            data_final.append(d_temp[0])
            for index in range(1, len(d_temp)):
                if not d_temp[index].__contains__('Postal'):
                    d1_temp = d1_temp + ' ' + d_temp[index]
        else:
            d1_temp = d1_temp + ' ' + data_temp[index1]
    data_final.append(d1_temp.strip())
    #print(data_final)
    return data_final

def extract_all_data():
            entries = os.listdir('/Users/nguyenthanhtai/Downloads/MyB Media/Dự Án Cá Nhân/Data Analysis/untitled/data')
            for entry in entries:
                #Initialize header for each output's file
                df = pd.DataFrame([],columns=use_cols)
                df.to_csv('output1.csv', index=False)
                with pdfplumber.open('data/'+entry) as pdf:
                    # Initialize an empty list to store extracted tables
                    all_tables = []
                    # # Loop through all pages
                    for page in pdf.pages:
                        # Extract tables horizontally from the page
                        tables = page.extract_tables()
                        page.close()
                        # Append each table to the list
                        for table in tables:
                            all_tables.extend(table)  # add rows to the overall table data
                    # Convert the list of tables to a pandas DataFrame
                    df = pd.DataFrame(all_tables)
                    # Save DataFrame to CSV
                    cols =[]
                    if entry.__contains__('123'):
                        cols = [1,3,2]
                        df[2] =df[4]+ df[2]
                    else:
                        cols = [1,2,3]
                    df.to_csv(entry.replace('.pdf','.csv'), index=False, mode='a', columns = cols)

            del pdf  # This would ensure that the pdf object is cleaned up by the garbage collector.
            #gc.collect()


        # df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row is headers
        # df.to_csv("output.csv", index=False)

def extract_data():

        # Regular expression pattern for identifying dates (like 01/09/2024)
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        doc_no_pattern = r'(\d{4}\.\d{4,5})'
        # Define a regular expression pattern for detecting Vietnamese Dong (VND) amounts
        #vnd_pattern = r'\d{1,3}(\.\d{3})'
        vnd_pattern = r'(\d{1,3}\.\d{3})'

        df = pd.DataFrame([],columns=column)
        df.to_csv('donate.csv', index=False)
        #for pIndex in range(1,12028):
        with pdfplumber.open("donate.pdf") as pdf:
                #Prepare to write to CSV file
                with open('output.csv', mode='w', newline='', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)

                    # Write the header row to the CSV
                    writer.writerow(['TNX Date', 'Credit', 'Transactions in Detail'])

                    # Loop through all the pages (if needed)
                    #reader = PdfReader("donate.pdf")
                    for page in pdf.pages:
                        gc.set_threshold(20000,50,100)
                        # Extract text from each page
                        text = page.extract_text()
                        #print(text)
                        df_page = pd.DataFrame([],columns=column)
                        # Split the text into lines for processing
                        lines = text.split('\n')
                        #print(lines)
                        current_row = []
                        for line in lines:
                            #print(line)
                            line_strip = line.strip()
                            # Skip empty lines
                            if (not line_strip or not re.match(date_pattern, line_strip)) and not current_row:
                                continue
                            # If the line contains a date, it indicates the start of a new row
                            if re.match(date_pattern, line_strip):
                                # If we already have data in current_row, write it to the CSV
                                if current_row:
                                    #print(current_row)
                                    df_page = pd.concat([df_page, pd.DataFrame(([split_to_db(current_row)]), columns=column)])
                                # Start a new row
                                current_row = [line_strip]
                            else:
                                if re.match(doc_no_pattern,line_strip) :
                                    continue
                                # Append the rest of the columns (Doc No, Debit, Credit, etc.) to the current row
                                current_row.append(line_strip)
                        # After the loop, write the last row to the CSV
                        if current_row:
                            df_page = pd.concat([df_page, pd.DataFrame(([split_to_db(current_row)]), columns=column)])
                        df_page.to_csv('donate.csv', mode='a',index=False, header=False)
                        #gc.collect()
                        page.close()

if __name__ == '__main__':
    extract_all_data()
