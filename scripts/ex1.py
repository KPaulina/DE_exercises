import requests
import zipfile
import os


download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
]


def main():
    path = os.getcwd()

    for url in download_uris:
        req = requests.get(url)
        filename = req.url[url.rfind('/')+1:]

        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        with zipfile.ZipFile(filename, 'r') as my_zip:
            for name in my_zip.namelist():
                if name.endswith('.csv'):
                    my_zip.extract(name)

    files_to_delete = [f for f in os.listdir(path) if f.endswith('.zip')]
    for f in files_to_delete:
        os.remove(os.path.join(path, f))


if __name__ == '__main__':
    main()

