import csv
from optparse import OptionParser
from data_map import map_names, big_commerce_fields
import os
from pathlib import Path
def covert_invoice_data(input_file = None , output_file = None , format_name = 'pc_to_big_commerce'):
    fields_maps = map_names.get('pc_to_big_commerce')
    all_rows = []
    with open(input_file) as input_csvfile, open(output_file,"w",newline='') as output_csvfile:
        reader = csv.DictReader(input_csvfile)
        writer = csv.DictWriter(output_csvfile,fieldnames=big_commerce_fields)
        writer.writeheader()
        for row in reader:
            big_com_map_row = {}
            for key in row.keys():
                new_key = fields_maps.get(key)
                big_com_map_row[new_key] =row[key]
            #default values
            big_com_map_row['Track Inventory'] = 'Y'
            writer.writerow(big_com_map_row)

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input_file",default= os.path.join(dir_path, '../../data/pc_am_data.csv'),
                      help="Input File to read data from", metavar="input_file")
    parser.add_option("-o", "--output_file",
                      dest="output_file", default=os.path.join(dir_path,  '../../data/pc_am_data_output.csv'),
                      help="File to output the converted data")
    (options, args) = parser.parse_args()
    covert_invoice_data(options.input_file,options.output_file)