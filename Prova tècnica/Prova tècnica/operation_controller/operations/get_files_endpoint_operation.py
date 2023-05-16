import traceback

import os
import pysftp

from urllib import request
import csv


class GetFilesEndpointOperation:
    def __init__(self, local_path, url, data_file_name) -> None:
        super(GetFilesEndpointOperation, self).__init__()

        self.local_path = local_path
        self.url = url
        self.data_file_name = data_file_name

    def download_from_endpoint(self) -> None:
        try:
            # Get file
            print('Downloading file from %s...' % self.url)
            request.urlretrieve(self.url, os.path.join(
                self.local_path, self.data_file_name))

            # Send success message
            return 'Success downloading file from %s completed' % self.url

        except (IOError, ValueError, AttributeError):

            # Send error message
            message = 'Error downloading the file %s\n:%s' % (
                self.data_file_name, traceback.format_exc())
            return message

    def data_to_csv(self, new_filename):
        # Read info from file
        with open(self.data_file_name, 'r') as file:
            data = file.read()

        data = eval(data)  # Convert string to dict
        keys = data['data'][0].keys()

        with open(new_filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data['data'])
