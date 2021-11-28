from pprint import pprint
import requests
from  reddit import Reddit
from ya_disk import YandexDisk


TOKEN =''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type':'application/json',
            'Authorization':'OAuth{}'.format(self.token)
        }

    def get_sh(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": path_to_file, "overwrite": "true"}
        headers = self.get_headers()
        response = requests.get(upload_url, params=params, headers=headers)
        pprint(response.json())
        return response.json()

    def _upload_f(self, path_to_file: str, file):
        response_dict = self.get_sh(path_to_file=path_to_file)
        href = response_dict.get("href", "")
        response = requests.put(href, data=open(file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Получилось!")
        return

if __name__ == '__main__':
    uploader= YaUploader(token = TOKEN)
    result = uploader._upload_f("/reqYA", "test_hw.txt")
    print(result)
