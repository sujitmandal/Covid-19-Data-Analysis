# Author : Sujit Mandal
import os
import argparse
import requests 
import pandas as pd #pin install pandas
from httpRespons import data_info
from httpRespons import userAgent
from httpRespons import httpResponseStatusCodes


def bothDose(request, date, output):
    if request.status_code == 200:
        data = request.json()

        data = data.get('sessions')
        
        for i in data:
            if 'available_capacity' in i:
                del i['available_capacity']
        
            if 'session_id' in i:
                del i['session_id']
           
            if 'fee_type' in i:
                del i['fee_type']

            if 'lat' in i:
                del i['lat']

            if 'long' in i:
                del i['long']

            if 'center_id' in i:
                del i['center_id']

        data.sort(key=lambda x: x['min_age_limit'], reverse=False)

        if len(data) != 0:
            jaon_data = pd.json_normalize(data)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_both.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_both.csv', index=False)

        else:
            jaon_data = pd.json_normalize(data_info)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_both.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_both.csv', index=False)

    else:
        print('HTTP Response Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

def doseOne(request, date, output):
    if request.status_code == 200:
        data = request.json()

        data = data.get('sessions')
        
        for i in data:
            if 'available_capacity_dose2' in i:
                del i['available_capacity_dose2']

            if 'available_capacity' in i:
                del i['available_capacity']

            if 'session_id' in i:
                del i['session_id']
           
            if 'fee_type' in i:
                del i['fee_type']

            if 'lat' in i:
                del i['lat']

            if 'long' in i:
                del i['long']

            if 'center_id' in i:
                del i['center_id']

        data.sort(key=lambda x: x['min_age_limit'], reverse=False)

        if len(data) != 0:
            jaon_data = pd.json_normalize(data)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_dose_one.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_dose_one.csv', index=False)

        else:
            jaon_data = pd.json_normalize(data_info)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_dose_one.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_dose_one.csv', index=False)

    else:
        print('HTTP Response Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))

def doseTwo(request, date, output):
    if request.status_code == 200:
        data = request.json()

        data = data.get('sessions')
        
        for i in data:
            if 'available_capacity_dose1' in i:
                del i['available_capacity_dose1']

            if 'available_capacity' in i:
                del i['available_capacity']

            if 'session_id' in i:
                del i['session_id']
           
            if 'fee_type' in i:
                del i['fee_type']

            if 'lat' in i:
                del i['lat']

            if 'long' in i:
                del i['long']

            if 'center_id' in i:
                del i['center_id']


        data.sort(key=lambda x: x['min_age_limit'], reverse=False)

        if len(data) != 0:
            jaon_data = pd.json_normalize(data)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_dose_two.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_dose_two.csv', index=False)

        else:
            jaon_data = pd.json_normalize(data_info)

            if output == 'html' or output == 'HTML':
                jaon_data.to_html(date + '_dose_two.html', index=False)

            if output == 'csv' or output == 'CSV':
                jaon_data.to_csv(date + '_dose_two.csv', index=False)

    else:
        print('HTTP Response Status : {}'.format(httpResponseStatusCodes.get(request.status_code)))


def main():
    my_parser = argparse.ArgumentParser(description='Covid-19 Vaccine Information')
    my_parser.add_argument("-dose", "-dose", required=True, help="Vaccine Dose")
    my_parser.add_argument("-d", "-d", required=True, help="Date")
    my_parser.add_argument("-p", "-p", required=True, help="PinCode")
    my_parser.add_argument("-o", "-o", required=False, help="File Extention")
    
    args = vars(my_parser.parse_args())

    dose = args['dose']
    date = args['d']
    pincode = args['p']
    output = args["o"]


    api_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode, date)
    headers = {'user-agent' : userAgent}
    API = requests.get(api_url, headers=headers)


    if dose == 'both' or dose == 'BOTH':
        bothDose(API, date, output)
        
        print('\n')
        print('{}'.format(date + '_both.' + output) + ' file is created.')
        print('Directory : {}'.format(os.getcwd()))

    if dose == 'one' or dose == 'ONE':
        doseOne(API, date, output)
        
        print('\n')
        print('{}'.format(date + '_dose_one.' + output) + ' file is created.')
        print('Directory : {}'.format(os.getcwd()))

    if dose == 'two' or dose == 'TWO':
        doseTwo(API, date, output)

        print('\n')
        print('{}'.format(date + '_dose_two.' + output) + ' file is created.')
        print('Directory : {}'.format(os.getcwd()))
        

if __name__ == "__main__":
    main()