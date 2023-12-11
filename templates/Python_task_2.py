# Question 1: Distance Matrix Calculation

import pandas as pd

def calculate_distance_matrix(df):
    pivot = df.pivot_table(index='start', columns='end', values='distance', aggfunc='sum', fill_value=0)
    distance_matrix = pivot.add(pivot.T, fill_value=0)
    distance_matrix.values[[range(distance_matrix.shape[0])]*2] = 0

    return distance_matrix

calculate_distance_matrix()

# Question 2: Unroll Distance Matrix

import pandas as pd

def unroll_distance_matrix(distance_matrix):
    distance_df = distance_matrix.reset_index()
    melted = pd.melt(distance_df, id_vars='index', var_name='id_end', value_name='distance')
    melted.columns = ['id_start', 'id_end', 'distance']
    unrolled_distance = melted[melted['id_start'] != melted['id_end']]

    return unrolled_distance

unroll_distance_matrix()

# Question 3: Finding IDs within Percentage Threshold

def find_ids_within_ten_percentage_threshold(df, reference_value):

    average_distance = df[df['id_start'] == reference_value]['distance'].mean()
    threshold = 0.1 * average_distance
    within_threshold = df[(df['distance'] >= average_distance - threshold) & (df['distance'] <= average_distance + threshold)]
    values_within_threshold = within_threshold['id_start'].unique()
    sorted_values = sorted(values_within_threshold)

    return sorted_values

find_ids_within_ten_percentage_threshold()

# Question 4: Calculate Toll Rate

def calculate_toll_rate(df):
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle, rate in rate_coefficients.items():
        df[vehicle] = df['distance'] * rate

    return df

calculate_toll_rate()

# Question 5: Calculate Time-Based Toll Rates

import pandas as pd
from datetime import time

def calculate_time_based_toll_rates(df):
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    def calculate_rate(row):
        day_of_week = row['start_time'].strftime('%A')

        if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            if time(0, 0) <= row['start_time'].time() <= time(10, 0):
                return 0.8
            elif time(10, 0) <= row['start_time'].time() <= time(18, 0):
                return 1.2
            else:
                return 0.8
        else:
            return 0.7

    df['start_day'] = df['start_time'].dt.day_name()
    df['end_day'] = df['end_time'].dt.day_name()
    df['moto'] = df.apply(lambda row: row['moto'] * calculate_rate(row), axis=1)
    df['car'] = df.apply(lambda row: row['car'] * calculate_rate(row), axis=1)
    df['rv'] = df.apply(lambda row: row['rv'] * calculate_rate(row), axis=1)
    df['bus'] = df.apply(lambda row: row['bus'] * calculate_rate(row), axis=1)
    df['truck'] = df.apply(lambda row: row['truck'] * calculate_rate(row), axis=1)

    df['start_time'] = df['start_time'].dt.time
    df['end_time'] = df['end_time'].dt.time

    return df

calculate_time_based_toll_rates()
