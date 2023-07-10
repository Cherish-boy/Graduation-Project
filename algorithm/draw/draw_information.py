import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('../jincheng.csv')
data = data.values.tolist()
print(data[5])