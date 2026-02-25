import requests
from datetime import datetime

url_template = 'https://simurg.space/gen_file?data=obs&date={data}'
now = datetime.now()
data = now.strftime("%Y-%m-%d")
url = url_template.format(data = data)

response = requests.get(url=url, stream=True)
print(f'For date {data} got: ', response.status_code)