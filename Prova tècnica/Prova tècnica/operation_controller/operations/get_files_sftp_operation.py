import traceback

import os
import pysftp


class GetFilesSFTPOperation:

    def __init__(self, local_path, host, user_name, password=None, remote_path=None) -> None:

        self.local_path = local_path
        self.host = host
        self.user_name = user_name
        self.password = password
        self.remote_path = remote_path

    def download_from_sftp(self) -> None:
        # Download and delete all the files from remote SFTP
        sftp = None
        try:
            print('Downloading input files from SFTP')
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            sftp = pysftp.Connection(
                host=self.host, username=self.user_name, password=self.password, cnopts=cnopts)
            if self.remote_path:
                sftp.cwd(self.remote_path)
            remote_files = sftp.listdir()

            for file_name in remote_files:
                if not sftp.isfile(file_name):
                    continue
                # Save the file
                file_path = os.path.join(self.local_path, file_name)
                print('Downloading %s...' % file_name)
                sftp.get(file_name, file_path)

            sftp.close()

            # Send success message
            return 'Success downloading files'
        except Exception:
            if sftp:
                sftp.close()

            # Send error message
            message = 'Error downloading files: \n%s' % traceback.format_exc()
            return message
