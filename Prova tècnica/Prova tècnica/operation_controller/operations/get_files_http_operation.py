import os
import traceback

from urllib import request


class GetFilesHTTPOperation:

    def __init__(self, local_path, base_url, file_name) -> None:
        super(GetFilesHTTPOperation, self).__init__()

        self.local_path = local_path
        self.base_url = base_url
        self.file_name = file_name

    def download_from_web(self) -> None:
        # Build url
        url = '/'.join([self.base_url, self.file_name])
        try:
            # Get file
            print('Downloading file from %s...' % url)
            request.urlretrieve(url, os.path.join(
                self.local_path, self.file_name))

            # Send success message
            return 'Success downloading file from %s completed' % url

        except (IOError, ValueError, AttributeError):

            # Send error message
            message = 'Error downloading the file %s\n:%s' % (
                self.file_name, traceback.format_exc())
            return message
