import requests  # Import the 'requests' library to send HTTP requests.


def make_request(url):
    try:
        # Send a GET request to the specified URL and return the response.
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        # If a connection error occurs, do nothing and continue.
        pass


# Set the target domain to 'google.com'.
target_input = "google.com"

# Open the 'subdomainlist.txt' file in read mode.
with open("subdomainlist.txt", "r") as subdomain_list:
    # Iterate through each line (subdomain) in the file.
    for word in subdomain_list:
        word = word.strip()  # Remove any leading or trailing whitespace from the subdomain.
        # Combine the subdomain with the target domain to form the full URL.
        url = "http://" + word + "." + target_input
        # Send a GET request to the constructed URL and get the response.
        response = make_request(url)
        # If a response is received (meaning the subdomain exists),
        if response:
            # Print the found subdomain to the console.
            print("Found subdomain ---> " + url)
