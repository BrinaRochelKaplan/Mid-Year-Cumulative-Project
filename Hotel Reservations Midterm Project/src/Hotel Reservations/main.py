import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import data_analysis.cleaning as cl

def main():
#reading in the file
    df = pd.read_csv('hotel_bookings.csv', na_values=[' ', '-', 'Undefined', 'None'])
    cl.convert_to_bool(df.is_canceled)
    cl.convert_to_bool(df.is_repeated_guest)
    cl.convert_to_datetime(df.reservation_status_date)
    cl.creating_date_column(df, ['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'], 'arrival_date')
    cl.new_col_from_other_cols(df, 'direct_booking', 'agent', 'company')
    cl.drop_col(['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month', 'agent', 'company'])
    cl.replace_nan(df['meal'], 'SC')
    cl.replace_nan(df['country'], 'other')
    print(df)

if __name__ == '__main__':
    main()