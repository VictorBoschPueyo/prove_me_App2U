import os
import traceback

from urllib import request

from operation_controller.operation_controller import OperationController


class GetFilesHTTPOperation:
    
    def __init__(self, local_path, base_url, file_name) -> None:
        super(GetFilesHTTPOperation, self).__init__()
        self.controller = None

        self.local_path = local_path
        self.base_url = base_url
        self.file_name = file_name

    def set_controller(self, controller: OperationController) -> None:
        self.controller = controller

    def download_from_web(self) -> None:
        # Build url
        url = '/'.join([self.base_url, self.file_name])
        try:
            # Get file
            print('Downloading file from %s...' % url)
            request.urlretrieve(url, os.path.join(self.local_path, self.file_name))
            self.controller.operation_completed(self)
        except (IOError, ValueError, AttributeError):
            message = 'Error downloading the file %s\n:%s' % (self.file_name, traceback.format_exc())
            self.controller.operation_error(self, message)


