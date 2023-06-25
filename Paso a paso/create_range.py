# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:45:14 2023

@author: Nico
"""
import numpy as np

def create_range(limit_latitude_start, limit_latitude_end, step_size, num_samples):
  """Creates a range of latitude values between the start and end limits, with a specified step size and number of samples.

  Args:
    limit_latitude_start: The starting latitude limit.
    limit_latitude_end: The ending latitude limit.
    step_size: The step size between values.
    num_samples: The number of samples to generate.

  Returns:
    A NumPy array of latitude values.
  """

  # Calculate the number of values in the range.
  num_values = int((limit_latitude_end - limit_latitude_start) / step_size) + 1

  # Clip the start limit to the end limit.
  limit_latitude_start = np.clip(limit_latitude_start, limit_latitude_end, None)

  # Create a NumPy array of latitude values.
  latitude_range = np.linspace(limit_latitude_start, limit_latitude_end, num=num_values, endpoint=True)

  # Return the latitude range.
  return latitude_range[:num_samples]

if __name__ == "__main__":
  # Set the latitude limits.
  limit_latitude_start = -17.025
  limit_latitude_end = -17.075

  # Set the step size.
  step_size = 0.001

  # Set the number of samples.
  num_samples = 100

  # Create the latitude range.
  latitude_range = create_range(limit_latitude_start, limit_latitude_end, step_size, num_samples)

  # Print the latitude range.
  print(latitude_range)








