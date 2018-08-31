#!/usr/bin/python

# Import necessary modules
import os
import csv
import datetime

# Gather/manipulate date information for csv naming/decisions
timestamp = datetime.datetime.now()
timestamp_string = str(timestamp)         # Make string to use split()
date, t = timestamp_string.split(' ')  # Separate into date and time
year, month, day = date.split('-')         # Split up elements of date
mon_yr = month + '-' + year               # Recombine month/year


def main():
    logfile = '/home/pi/Documents/Speedtest_Logger/Speedtest_Logfiles/'
    +mon_yr+'.csv'
    outfile = open(logfile, 'a', newline='')                    # Open file
    writer = csv.writer(outfile)                                # Create new
    print('Retrieving speed test data...')
    ping, download, upload = get_speedtest_data()               # Store data
    writer.writerow([date, t, ping, download, upload])          # Write data
    outfile.close()


def get_speedtest_data():
    '''New function to pipe in data from the speedtest terminal function'''
    speedtest_output = os.popen('speedtest-cli --simple')  # Call terminal com

    # Set variables to have no data
    ping = download = upload = 0

    for line in speedtest_output:             # Loop through lines in speedtest
        label, value, unit = line.split(' ')  # Split line into three

        # Store values in correct variable based on the label in outpu
        if 'Ping' in label:
            ping = float(value)
        elif 'Download' in label:
            download = float(value)
    # Return all values IF all values were parsed
    if all((ping, download, upload)):
        print('Data logged successfully!')
        print('Ping: ' + str(ping) + ' ms')
        print('Download: ' + str(download) + ' Mbps')
        print('Upload: ' + str(upload) + ' Mbps')
        return ping, download, upload
    else:
        print('Values not logged.')

# Runs main() function. Used to make python programs similar to C/C++.
if __name__ == '__main__':
    main()
