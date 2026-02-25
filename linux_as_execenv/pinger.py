import requests
from datetime import datetime, timedelta

url_template = 'https://simurg.space/gen_file?data=obs&date={data}'
now = datetime.now()

while True:
    data = now.strftime("%Y-%m-%d")
    url = url_template.format(data = data)

    response = requests.get(url=url, stream=True)
    print(f'For date {data} got: ', response.status_code)
    if response.status_code == 200:
        print(f"Last available data are for {data}")
        break
    else:
        now = now - timedelta(days=1)