import os
import json
from lighthouseweb3 import Lighthouse

API_TOKEN = os.environ["LIGHTHOUSE_API_TOKEN"]
FOLDER_DATA = os.environ["LIGHTHOUSE_FOLDER_DATA"]


class LightHouse: 

    def __init__(self):
        """
        Init class
        """
        self.lh = Lighthouse(token=API_TOKEN)

    def send_data_lh(self, path: str, tag: str = ""):
        """
        TODO: In case of images, check the image and resize it so it does not use uneccessary space
        
        This function upload data to lighthouse
        :param path: local path of data
        :return: True if file upload successful
        """

        tagged_source_file_path = path
        try:
            index_data = self.lh.upload(path, tag=tag)
        except Exception as e:
            print("Error uploading file to lighthouse")
            print(e)
            return {"error": "Error uploading file to lighthouse"}

        print("File Upload Successful!")
        return index_data

    def download_data_lh(self, cid: str):
        """
        This function download data from IPFS lighthouse
        :param cid:
        :return: True if file download successful
        """

        destination_path = FOLDER_DATA

        file_info = self.lh.download(cid)

        file_content = file_info[0]

        with open(destination_path, 'wb') as destination_file:
            destination_file.write(file_content)

        print("Download successful!")

        if file_content:
            estatus = True
        else:
            estatus = False

        return estatus
