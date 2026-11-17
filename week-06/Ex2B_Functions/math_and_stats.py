import random
import math
import statistics

vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# Calculate the total, mean, and median for the 75-value sample.
sample_total = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# Calculate statistics for the 200 values chosen with replacement.
choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# Calculate the area of the circle and round up and down.
circle_area = pi * radius ** 2
area_up = math.ceil(circle_area)
area_down = math.floor(circle_area)

print('_Experimenting with a subset of integers 1-100:')
print(f'Sum of 75 sample values from 1 to 100: {sample_total}')
print(f'Average of 75 sample values: {sample_average:.2f}')
print(f'Median of 75 sample values: {sample_median:.2f}')
print('\n')
print('_Experimenting with a superset of 200 values, integers 1-100:')
print(f'Average of 200 values: {choices_average:.2f}')
print(f'Median of 200 values: {choices_median:.2f}')
print(f'Mode of 200 values: {choices_mode}')
print(f'Standard deviation of 200 values: {choices_stdev:.2f}')
print(f'Variance of 200 values: {choices_variance:.2f}')
print('\n')
print('_Modeling a random circle:')
print(f'Radius = {radius}, area = {area_up} (rounded up to the nearest integer)')
print(f'Radius = {radius}, area = {area_down} (rounded down to the nearest integer)')
