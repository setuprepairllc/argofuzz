import requests

url = "https://app.swaggerhub.com/apis/MIKEARGO/argopetstore/1.0.0"
payloads = [
    "", "test", "123", "null", "{}", "[]", "<script>alert(1)</script>", "' OR 1=1 --", "A" * 1000
]

for payload in payloads:
    data = {"input": payload}
    response = requests.post(url, json=data)
    print(f"Payload: {payload!r} | Status: {response.status_code} | Response: {response.text[:100]}")
