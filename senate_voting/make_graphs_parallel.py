# Script for grabbing congressional graph data
from joblib import Parallel, delayed  
import multiprocessing
import time
from src import write_graph

data_dir = 'graphs'
num_cores = multiprocessing.cpu_count()


print('Running on {} cores.'.format(num_cores))

def grab_data(congress):
    start = time.time()
    write_graph(congress)
    end = time.time()
    print('Finished graph for congress {}.\nElapsed time {:.03f} s.\n\n'
          .format(congress,end-start))

Parallel(n_jobs=num_cores)(delayed(grab_data)(congress)
                           for congress in range(101,115))
