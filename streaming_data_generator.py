# This is a basic script that reads in a csv and, every 10 seconds,
# randomly extract five observations from the dataset and 
# adds the observations to a folder in a csv file.
# This will allow us to simulate streaming data in an associated 
# notebook

# Loading packages
import pandas as pd
import numpy as np
import time

# Reading in the data
stream_data = pd.read_csv("power_streaming_data.csv")

# Setting a seed for random sampling
np.random.seed(5)

# Creating a loop to randomly draw observations from stream_data
# and write the data to csv files
for i in range(20): 
    # Sampling from the dataframe
    sample = stream_data.sample(5)
    
    # Sending to CSV
    sample.to_csv(f"streamed_obs/batch_{i}.csv", index = False)
    
    # Pausing for 30 seconds between batches
    time.sleep(30)