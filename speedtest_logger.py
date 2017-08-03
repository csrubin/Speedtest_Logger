#!/usr/bin/python3

#Import necessary modules
import os
import csv
import datetime

#Gather/manipulate date information for csv naming/decisions
timestamp = datetime.datetime.now()
timestamp_string = str(timestamp)       #Make string to use split()
date,time = timestamp_string.split(' ') #Separate timestamp into date and time
year,month,day = date.split('-')        #Split up elements of date
mon_yr = month + '-' + year             #Recombine month/year --> for monthly logfiles

def main():
    logfile = '/home/pi/Documents/Speedtest_Logger/Speedtest_Logfiles/'+mon_yr+'.csv'  #Name and choose location for logfile based on month/yr
    outfile = open(logfile, 'a', newline='')                        #Open file with 'a' descriptor to append file if one already exists for that month
    writer = csv.writer(outfile)                                    #Create new writer object from csv module
    print('Retrieving speed test data...')
    ping, download, upload = get_speedtest_data()                   #Store data from get_speedtest_data() into 3 variables
    writer.writerow([date, time, ping, download, upload])           #Write data to logfile
    outfile.close()                       

#New function to pipe in data from the speedtest terminal function
def get_speedtest_data():
    speedtest_output = os.popen('speedtest-cli --simple')    #Call terminal command and pipe data into variable
    
    #Set variables to have no data
    ping = download = upload = None
    
    for line in speedtest_output:           #Loop through lines in speedtest_output
        label, value, unit = line.split(' ')   #Split line into three generic variables. Blank space = delimiter
        
        #Store values in correct variable based on the label in speedtest_output
        if 'Ping' in label:
            ping = float(value)
        elif 'Download' in label:
            download = float(value)
        elif 'Upload' in label:
                upload = float(value)
    
    #Return all values IF all values were parsed            
    if all((ping, download, upload)):
        print('Data logged successfully!')
        print('Ping: ' + str(ping) + ' ms')
        print('Download: ' + str(download) + ' Mbps')
        print('Upload: ' + str(upload) + ' Mbps')
        return ping, download, upload

#Runs main() function. Used to make python programs similar to C/C++.
if __name__ == '__main__':
    main()




