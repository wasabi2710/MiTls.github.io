import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(
    # ... other connection parameters
    cert_reqs='CERT_NONE'  # Disable certificate verification
)

site = "https://hackthissite.org/"

word_list = open("words.txt", "r")
with word_list as word_list:
    lines = word_list.readlines()
    for line in lines:
        word = line.strip()
        try:
            response = http.request("GET", f"{site}/{word}/", timeout=5)
            print(f"Success: {response.status}")
                
            # response = requests.get(f'{site}{word}')
            # print(response)
        except urllib3.exceptions.DecodeError as e:
            print(f"Decode Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
