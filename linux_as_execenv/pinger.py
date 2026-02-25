import requests

url_template = 'https://simurg.space/gen_file?data=obs&date={data}'
data = "2026-02-19"
url = url_template.format(data = data)

response = requests.get(url=url, stream=True)
print(f'For date {data} got: ', response.status_code)