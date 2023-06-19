import urllib.parse
import datetime
import csv
from tabulate import tabulate
from urllib import parse as urlparse
from selenium import webdriver
import pandas as pd
def shorten_url(url):
    parsed_url = urlparse.urlparse(url)
    shortened_url = parsed_url.netloc + parsed_url.path
    if parsed_url.query:
        shortened_url += "?" + parsed_url.query
    return shortened_url
# Fetch the current timestamp
tracked_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Read network data from file
with open(
    "C:/Users/Harshita.Betala/Documents/intel_project/intel-collection/outputs/fmoviefree.sc/network_data.txt",
    "r",
) as file:
    network_data = file.readlines()
# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser
# Function to get the redirected domain using Selenium
def get_redirected_domain(url):
    driver.get(url)
    redirected_url = driver.current_url
    shortened_url = shorten_url(redirected_url)
    return shortened_url
def convert_to_dict():
    df = pd.read_csv(
        "C:/Users/Harshita.Betala/Documents/intel_project/intel-collection/outputs/network_call_object_table.csv"
    )
    data_dict = {}
    for index, row in df.iterrows():
        data_dict[row["Object ID"]] = {
            "Keywords": str(row["Keywords"]).split(", ") if row["Keywords"] else []
        }
    return data_dict
def add_object_ids(data_dict, specific_url):
    object_ids = []
    for key, value in data_dict.items():
        for v in value["Keywords"]:
            if v in specific_url:
                object_ids.append(key)
                break
    return object_ids
# Categorize the URLs and retrieve the object ID
categorized_data = []
for line in network_data:
    parts = line.strip().split(" ", 2)
    url = parts[0]
    status_code = parts[1]
    content_type = parts[2] if len(parts) > 2 else "None"
    domain = urllib.parse.urlparse(url).hostname
    if domain.startswith("www."):
        domain = domain[4:]
    else:
        domain = domain.split("//")[-1]
    data_dict = convert_to_dict()
    redirected_domain = get_redirected_domain(url)
    specific_url = shorten_url(url)
    service_type = "vod"  # Default service type is "vod"
    object_ids = add_object_ids(data_dict, url)
    categorized_data.append(
        [
            tracked_date,
            domain,
            redirected_domain,
            specific_url,
            status_code,
            service_type,
            object_ids,
        ]
    )
# Prepare table data
table_data = categorized_data
headers = [
    "Tracked Date",
    "Domain",
    "Redirected Domain",
    "Specific URL",
    "Status Code",
    "Service Type",
    "Object IDs",
]
# Generate the table
table = tabulate(table_data, headers, tablefmt="grid")
# Convert table data to CSV format
csv_data = []
csv_data.append(headers)
csv_data.extend(table_data)
# Write the table to a CSV file
with open(
    "C:/Users/Harshita.Betala/Documents/intel_project/intel-collection/outputs/fmoviefree.sc/network_call_data_table.csv",
    "w",
    newline="",
) as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
# Close the Selenium WebDriver
driver.quit()