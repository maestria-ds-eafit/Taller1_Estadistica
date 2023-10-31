# %%
import numpy as np


# %%
def exponential_distribution(lambda_, n):
    return np.random.exponential(scale=1 / lambda_, size=n)


# %%
def first_estimator(data):
    return data[0]


# %%
def second_estimator(data):
    result = np.sum(data) - data[len(data) - 1]
    return result / (len(data) - 1)


# %%
def third_estimator(data):
    return np.mean(data)


# %%
def fourth_estimator(data):
    return np.min(data)


# %%
lambda_ = 1
data_lengths = [10, 100, 1000]
for length in data_lengths:
    data = exponential_distribution(lambda_, length)
    print(f"First estimator with {length} data points:", first_estimator(data))
    print(f"Second estimator with {length} data points", second_estimator(data))
    print(f"Third estimatorwith {length} data points", third_estimator(data))
    print(f"Fourth estimator with {length} data points", fourth_estimator(data))
    print("-------------------------------------------------------")
# %%
