import numpy as np
import pandas as pd

# Python Task 1

# Question 1: Car Matrix Generation
def generate_car_matrix():
    df = pd.read_csv('dataset-1.csv')
    matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    for i in range(min(matrix.shape)):
        matrix.iloc[i, i] = 0

    return matrix

generate_car_matrix()

# Question 2: Car Type Count Calculation
import pandas as pd

def get_type_count(df):
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices))

    type_count = df['car_type'].value_counts().to_dict()

    sorted_type_count = {key: type_count[key] for key in sorted(type_count)}

    return sorted_type_count

get_type_count()

# Question 3: Bus Count Index Retrieval
import pandas as pd

def get_bus_indexes(df):
    bus_mean = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_indexes.sort()

    return bus_indexes

get_bus_indexes()

# Question 4: Route Filtering
import pandas as pd

def filter_routes(df):
    avg_truck_by_route = df.groupby('route')['truck'].mean()
    routes_filtered = avg_truck_by_route[avg_truck_by_route > 7].index.tolist()
    routes_filtered.sort()

    return routes_filtered

filter_routes()

# Question 5: Matrix Value Modification
import pandas as pd
def multiply_matrix(matrix):
    modified_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

multiply_matrix()

# Question 6. Time Check
import pandas as pd

def verify_timestamp_completeness(df):

    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])


    df['duration'] = df['end_timestamp'] - df['start_timestamp']


    grouped = df.groupby(['id', 'id_2'])


    def check_completeness(group):

        completeness = group.groupby(group['start_timestamp'].dt.date)['duration'].sum() >= pd.Timedelta(days=1)

        completeness &= len(completeness) == 7

        return not completeness.all()

    completeness_result = grouped.apply(check_completeness)

    return completeness_result

verify_timestamp_completeness()
