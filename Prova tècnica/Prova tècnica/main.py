from typing import Any, List

from operation_controller.operation_controller import OperationController
from operation_controller.operations.get_files_http_operation import GetFilesHTTPOperation
from operation_controller.operations.get_files_sftp_operation import GetFilesSFTPOperation
from operation_controller.operations.get_files_endpoint_operation import GetFilesEndpointOperation


def create_operations() -> List[Any]:
    ops = []

    operation = GetFilesSFTPOperation(
        '.', 'test.rebex.net', 'demo', 'password')
    ops.append(operation)

    operation = GetFilesHTTPOperation('.', 'https://www.google.com/images/branding/googlelogo/2x',
                                      'googlelogo_color_272x92dp.png')
    ops.append(operation)

    operation = GetFilesEndpointOperation('.', 'https://gorest.co.in/public-api/users',
                                          'users_data.txt')
    ops.append(operation)

    return ops


if '__main__':
    # Create the list of operations
    operations = create_operations()

    # Launch process
    OperationController(operations).start()
