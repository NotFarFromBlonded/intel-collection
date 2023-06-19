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
with open("intel-collection/outputs/fmoviefree.sc/network_data.txt", "r") as file:
    network_data = file.readlines()

# Read intel object data from file
with open("intel-collection/outputs/network_call_object_table.csv", "r") as file:
    reader = csv.reader(file)
    object_table_data = list(reader)

# Remove the header row from object table data
object_table_data = object_table_data[1:]

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser


# Function to get the redirected domain using Selenium
def get_redirected_domain(url):
    driver.get(url)
    redirected_url = driver.current_url
    shortened_url = shorten_url(redirected_url)
    return shortened_url


# Function to check if a URL matches any keyword
def check_keywords(url, keywords):
    for keyword in keywords:
        if keyword in url:
            return True
    return False


# Function to fetch the object ID from the intel_object table based on the URL
def fetch_object_id(url):
    for row in object_table_data:
        if len(row) > 4:
            object_id = row[0].strip()
            keywords = row[4].split(", ") if row[4] else []
            if check_keywords(url, keywords):
                return object_id
    return None

def convert_to_dict():
    df = pd.read_csv("/home/debashishmajumdar/Documents/GitHub/intel-collection/outputs/network_call_object_table.csv")
    data_dict = {}
    for index, row in df.iterrows():
        data_dict[row["Object ID"]] = {"Keywords":str(row["Keywords"]).split(", ") if row["Keywords"] else []}
    return data_dict

def add_object_ids(data_dict, specific_url):
    object_ids = []
    for key, value in data_dict.items():
        for v in value['Keywords']:
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
    intel_object_id = fetch_object_id(url)
    service_type = "vod"  # Default service type is "vod"
    object_ids = add_object_ids(data_dict, url)
    categorized_data.append(
        [
            tracked_date,
            domain,
            redirected_domain,
            specific_url,
            intel_object_id,
            status_code,
            service_type,
            object_ids
        ]
    )


# Prepare table data
table_data = categorized_data
headers = [
    "Tracked Date",
    "Domain",
    "Redirected Domain",
    "Specific URL",
    "Intel Object ID",
    "Status Code",
    "Service Type",
    "Object IDs"
]

# Generate the table
table = tabulate(table_data, headers, tablefmt="grid")

# Convert table data to CSV format
csv_data = []
csv_data.append(headers)
csv_data.extend(table_data)

# Write the table to a CSV file
with open(
    "../outputs/fmoviefree.sc/network_call_data_table.csv",
    "w",
    newline="",
) as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Close the Selenium WebDriver
driver.quit()
