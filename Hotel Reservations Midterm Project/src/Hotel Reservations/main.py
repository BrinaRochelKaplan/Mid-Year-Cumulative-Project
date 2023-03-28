import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import math
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
import data_analysis.cleaning as cl
import data_analysis.data_structures as ds
import sql.database_actions as da

#reading in the file
df = pd.read_csv('Hotel Reservations Midterm Project\src\Hotel Reservations\hotel_bookings.csv', na_values=[' ', '-', 'Undefined', 'None'])
    # cl.convert_to_bool(df.is_canceled)
    # cl.convert_to_bool(df.is_repeated_guest)
    # cl.convert_to_datetime(df.reservation_status_date)
    # cl.creating_date_column(df, ['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'], 'arrival_date')
    # cl.new_col_from_other_cols(df, 'direct_booking', 'agent', 'company')
    # cl.drop_col(df, ['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'])
    # cl.replace_nan(df['meal'], 'SC')
    # cl.replace_nan(df['country'], 'other')
    # cl.replace_nan(df['agent'], df.agent.mean())
    # cl.replace_nan(df['company'], df.company.mean())
    # cl.replace_nan(df['children'], 0)
    # cl.replace_nan(df['market_segment'], 'Direct')
    # cl.replace_nan(df['distribution_channel'], method='ffill')

    # da.create_tables_from_df(df)

lead_time_list = [3, 7, 23, 30, 50, 90, 120, 150, 300, 350]


def create_frequency_table(data):
    lead_time_frequency_dict = {}
    for n in lead_time_list:
        lead_time_frequency_dict[n] = 0#df[column].count(n).sum()
        for each in data:
            if each == n:
                lead_time_frequency_dict[n] += 1
    return lead_time_frequency_dict

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with ProcessPoolExecutor() as exe:
        processes = [exe.submit(mapper, data) for _ in chunks]
        results = [process.result() for process in processes]
    merge_result = reduce(reducer, results)
    return merge_result

# merging the dictionaries returned from previous function
def reducer_str(dict1, dict2):
    for d in dict2:
        if d in dict1:
            dict1[d] += dict2[d]
        else:
            dict1[d] = dict2[d]
    return dict1


    gh = create_frequency_table(df['lead_time'])
    print(gh)

if __name__ == '__main__':
    target_count = map_reduce(df['lead_time'], 8, create_frequency_table, reducer_str)
    print(target_count)