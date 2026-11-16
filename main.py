import csv
from pathlib import Path
import json
import ssl
import certifi
from urllib.request import urlopen
# %% Exercise - Read Multiple Files Using One Function

# Assign file paths to variables
txt_file = "/Users/sandy/PycharmProjects/Data_Engineering/sample.txt"
csv_file = "/Users/sandy/PycharmProjects/Data_Engineering/sales.csv"
log_file = "/Users/sandy/PycharmProjects/Data_Engineering/application.log"
json_file = "/Users/sandy/PycharmProjects/Data_Engineering/Transcations.json"
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# %% Created one reusable function
def read_file(file_path):

    with open(file_path, "r") as file:
        data = file.read()
        print(data)

# %% Created a reusable function to write data
def write_file(file_path, data):
    with open(file_path, "w") as file:
        data = file.write(data)
        print(data)

# %% Create a reusable function to append data
def append_file(file_path, data):
    with open(file_path, "a") as file:
        data = file.write(data)
        print(data)

#%% Call the same function with different arguments
read_file(txt_file)
#%%
read_file(csv_file)
#%%
read_file(log_file)
#%%
read_file(json_file)


# %%  - TXT File Write and Append

# Write data to the TXT file
write_file(txt_file, "Welcome to Python\n")

# Append new data to the TXT file
append_file(txt_file, "Learning Data Engineering\n")

# Read the updated TXT file
read_file(txt_file)


# %% CSV File - Write and Append Using Existing Functions

# Write CSV data
write_file(csv_file, "id,product,amount\n1,Laptop,1200\n2,Mouse,25\n")

# Append new CSV data
append_file(csv_file, "3,Keyboard,75\n")

# Read CSV data
read_file(csv_file)

#  CSV File - Reader and DictReader
# %% Read CSV using reader()
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# %% Read CSV using DictReader()
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

# %%  LOG File Handling
# %% Write data to LOG file
write_file(log_file, "2026-11-14 09:00:00 INFO Pipeline started\n")

# %% Append new LOG entries
append_file(log_file, "2026-11-14 09:01:00 INFO File ingested\n")
append_file(log_file, "2026-11-14 09:02:00 ERROR Database connection failed\n")
append_file(log_file, "2026-11-14 09:03:00 INFO Pipeline stopped\n")

# %% Read LOG file
read_file(log_file)



# Task 2 - Exercise 4 - JSON File Handling
# %% Create JSON data
transactions = {
    "transactions": [
        {"id": 101, "customer": "Ravi", "amount": 1200},
        {"id": 102, "customer": "Priya", "amount": 500}
    ]
}

# %% Write JSON data using existing function
write_file(json_file, json.dumps(transactions, indent=4))

# %% Read JSON data using existing function
read_file(json_file)

# %% Load existing JSON data
with open(json_file, "r") as file:
    data = json.load(file)

# %% Append a new transaction to the Python list
data["transactions"].append(
    {"id": 103, "customer": "Arjun", "amount": 750}
)

# %% Save updated JSON data
write_file(json_file, json.dumps(data, indent=4))

# %% Read updated JSON file
print("\nUpdated JSON Data:")
read_file(json_file)




# %% API Exercise 1 - Read API Data Using GET

# %% API Exercise 1 - GET Request with SSL Certificate

# Assign API URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Create reusable function
def read_api(url):

    # Create a secure SSL context
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Connect to the API
    with urlopen(url, context=ssl_context, timeout=10) as response:

        # Read JSON response
        data = json.load(response)

        # Display API data
        print(data)


# Call the function
read_api(api_url)


# %% API Exercise 2 - Write API Data Using POST

from urllib.request import Request, urlopen
# Assign API URL to a variable
api_url_post = "https://jsonplaceholder.typicode.com/posts"

# Create reusable function
def write_api(url, data):

    # Convert Python dictionary into JSON bytes
    json_data = json.dumps(data).encode("utf-8")

    # Create a secure SSL connection
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Create POST request
    request = Request(
        url,
        data=json_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    # Send request and read response
    with urlopen(request, context=ssl_context, timeout=10) as response:
        result = json.load(response)
        print(result)


# Create sample data
new_post = {
    "title": "Data Engineering",
    "body": "Learning API operations",
    "userId": 1
}

# Call the function
write_api(api_url_post , new_post)


# %% API Exercise 3A - Update API Data Using PUT

import json
import ssl
import certifi
from urllib.request import Request, urlopen

# Assign API URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Create reusable function
def update_api(url, data, method):

    # Convert Python dictionary to JSON bytes
    json_data = json.dumps(data).encode("utf-8")

    # Create secure SSL context
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Create API request
    request = Request(
        url,
        data=json_data,
        headers={"Content-Type": "application/json"},
        method=method
    )

    # Send request and read response
    with urlopen(request, context=ssl_context, timeout=10) as response:
        result = json.load(response)
        print(result)


# Data to replace
updated_post = {
    "id": 1,
    "title": "Updated Data Engineering",
    "body": "Learning PUT requests",
    "userId": 1
}

# Execute PUT request
update_api(api_url, updated_post, "PUT")


# %% API Exercise 3B - Update API Data Using PATCH

# Specify API URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Only update the title
patch_data = {
    "title": "Python Data Engineering"
}

# Execute PATCH request
update_api(api_url, patch_data, "PATCH")


# %% API - Reusable Function for GET, POST, PUT and PATCH

import json
import ssl
import certifi
from urllib.request import Request, urlopen

# Assign API URLs
get_url = "https://jsonplaceholder.typicode.com/posts/1"
post_url = "https://jsonplaceholder.typicode.com/posts"
update_url = "https://jsonplaceholder.typicode.com/posts/1"


# Create one reusable API function
def api_request(url, method, data=None):

    # Create secure SSL connection
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    # Convert Python dictionary to JSON bytes
    json_data = json.dumps(data).encode("utf-8") if data is not None else None

    # Create API request
    request = Request(
        url,
        data=json_data,
        headers={"Content-Type": "application/json"},
        method=method.upper()
    )

    # Send request and read response
    with urlopen(request, context=ssl_context, timeout=10) as response:
        result = json.load(response)

    return result


# GET - Read API data
print("GET OUTPUT:")
print(api_request(get_url, "GET"))


# POST - Create new data
new_data = {
    "title": "Data Engineering",
    "body": "Learning API functions",
    "userId": 1
}

print("\nPOST OUTPUT:")
print(api_request(post_url, "POST", new_data))


# PUT - Replace existing data
updated_data = {
    "id": 1,
    "title": "Updated Data Engineering",
    "body": "Learning PUT",
    "userId": 1
}

print("\nPUT OUTPUT:")
print(api_request(update_url, "PUT", updated_data))


# PATCH - Update specific fields
patch_data = {
    "title": "Python API Practice"
}

print("\nPATCH OUTPUT:")
print(api_request(update_url, "PATCH", patch_data))


# %%Task 1 - Read JSON using **kwargs

import json

def read_json(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

with open(json_file, "r") as file:
    data = json.load(file)

read_json(**data)


# %%
import numpy as np

a = np.array ([1,2,3,4])
print(a)

# %%
range_arr = np.arange(0, 10, 3)
print(range_arr)

# %% . Array with Evenly Spaced Values

linspace_arr = np.linspace(0, 1, 5)

print(linspace_arr)

# %% 8. Array with Random Numbers

rand_arr = np.random.rand(2, 3)

print(rand_arr)