import urllib3

http = urllib3.PoolManager(
    # ... other connection parameters
    cert_reqs='CERT_NONE'  # Disable certificate verification
)

# Making the request (The request function returns HTTPResponse object)
resp = http.request("GET", "https://hackthissite.org/missions/")

print(resp.status)
# 200
print(resp.data)
# b"{\n  "origin": "104.232.115.37"\n}\n"
print(resp.headers)
# HTTPHeaderDict({"Content-Length": "32", ...})