"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
import tui

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""


# 16 To retrieve total number of records
def total_num_records(records):
    tot_num = len(records)
    return tot_num


# 17
# To retrieve a record with serial number specified
def record_by_serial(records):
    serial_num = tui.serial_number()
    serial_num1 = serial_num - 1
    data = [records[serial_num1]]
    return data


# 18 To retrieve records by observation dates
def records_with_obs_dates(records):
    dates = tui.observation_dates()
    records_with = []
    for record in records:
        if record[1] in dates:
            records_with.append(record)
    return records_with


# 19 To group records by country/region
def records_by_country_region(records):
    records_dict = {}
    for record in records:
        if record[3] not in records_dict:
            records_dict[record[3]] = []
            records_dict[record[3]].append(record)
    return records_dict


# 20 To retrieve summary of all records
def ret_summary(records):
    summary_dict = {}
    for record in records:
        summary_dict[record[3]] = {"Confirmed": 0, "Death": 0, "Recovery": 0}
    for record in records:
        cof = summary_dict[record[3]]["Confirmed"] + int(record[5])
        det = summary_dict[record[3]]["Death"] + int(record[6])
        rec = summary_dict[record[3]]["Recovery"] + int(record[7])
        summary_dict[record[3]]["Confirmed"] = cof
        summary_dict[record[3]]["Death"] = det
        summary_dict[record[3]]["Recovery"] = rec
    return summary_dict
