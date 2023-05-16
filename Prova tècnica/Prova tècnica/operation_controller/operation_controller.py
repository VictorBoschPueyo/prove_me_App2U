from typing import List, Any


class Operation:
    def __init__(self, operation) -> None:
        self.operation = operation

    def execute(self):
        from operation_controller.operations.get_files_http_operation import GetFilesHTTPOperation
        from operation_controller.operations.get_files_sftp_operation import GetFilesSFTPOperation
        from operation_controller.operations.get_files_endpoint_operation import GetFilesEndpointOperation

        if isinstance(self.operation, GetFilesSFTPOperation):
            return self.operation.download_from_sftp()
        elif isinstance(self.operation, GetFilesHTTPOperation):
            return self.operation.download_from_web()
        elif isinstance(self.operation, GetFilesEndpointOperation):
            ret = self.operation.download_from_endpoint()
            if (ret[0:7] == "Success"):
                self.operation.data_to_csv('users_data.csv')
            return ret
        else:
            return "Unknown operation"

    def operation_info(self) -> None:
        from operation_controller.operations.get_files_http_operation import GetFilesHTTPOperation
        from operation_controller.operations.get_files_sftp_operation import GetFilesSFTPOperation
        from operation_controller.operations.get_files_endpoint_operation import GetFilesEndpointOperation

        if isinstance(self.operation, GetFilesSFTPOperation):
            print('Download from %s...' % self.operation.host)
        elif isinstance(self.operation, GetFilesHTTPOperation):
            print('Download from %s...' % self.operation.base_url)
        elif isinstance(self.operation, GetFilesEndpointOperation):
            print('Download from %s...' % self.operation.url)
        else:
            print('Unknown operation')


class OperationController:
    def __init__(self, operations: List[Any]) -> None:
        self.operations = operations
        self.current_operation_index = 0

    def start(self) -> None:
        print("Start operations")
        self.execute_next_operation()

    def execute_next_operation(self) -> None:

        if self.current_operation_index < len(self.operations):
            op = Operation(self.operations[self.current_operation_index])

            # Show operation info
            op.operation_info()

            # Execute operation
            response = op.execute()

            # Handle response
            if response == "Unknown operation":
                self.operation_error(op, "Error unknown operation")
            elif response[0:7] != "Success":
                self.operation_error(op, response)
            else:
                print("Operation completed")
                self.operation_completed(op)
        else:
            self.operations_completed()

    def operation_error(self, operation, message: str) -> None:
        self.operations_error()

        # Show error
        print(message)

    def operation_completed(self, operation) -> None:
        self.current_operation_index += 1
        self.execute_next_operation()

    def operations_error(self) -> None:
        print("Process finished with errors\n")

    def operations_completed(self) -> None:
        print("Process finished successfully\n")
