import requests

status_codes = [101, 200, 306, 404, 500]

print('[INFO] Requester app started successfully')
for code in status_codes:
    url = f"https://httpstat.us/{code}"
    try:
        response = requests.get(url)
        if 100 <= response.status_code < 400:
            print(f"[INFO] Status: {response.status_code}, Body: {response.text.strip()}")
        else:
            raise Exception(f"[ERROR] Status: {response.status_code}, Body: {response.text.strip()}")
    except Exception as e:
        print(e)
print('[INFO] Requester app is shutting down')
