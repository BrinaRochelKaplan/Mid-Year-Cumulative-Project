import math
import functools
from multiprocessing import Pool

lead_time_list = [3, 7, 23, 30, 50, 90, 120, 150, 300, 350]


def create_frequency_table(column):
    lead_time_frequency_dict = {}
    for n in lead_time_list:
        lead_time_frequency_dict[n] = 0#df[column].count(n).sum()
        for each in df[column]:
            if each == n:
                lead_time_frequency_dict[n] += 1
    return lead_time_frequency_dict

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    pool = Pool(num_processes)
    chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

# merging the dictionaries returned from previous function
def reducer_str(dict1, dict2):
    for d in dict2:
        if d in dict1:
            dict1[d] += dict2[d]
        else:
            dict1[d] = dict2[d]
    return dict1