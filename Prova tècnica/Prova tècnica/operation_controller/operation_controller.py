from typing import List


class Operation:
    def __init__(self, operation) -> None:
        self.operation = operation

    def execute(self, controller) -> None:
        from operation_controller.operations.get_files_http_operation import GetFilesHTTPOperation
        from operation_controller.operations.get_files_sftp_operation import GetFilesSFTPOperation

        if isinstance(self.operation, GetFilesSFTPOperation):
            self.operation.set_controller(controller)
            self.operation.download_from_sftp()
            return 0
        elif isinstance(self.operation, GetFilesHTTPOperation):
            self.operation.set_controller(controller)
            self.operation.download_from_web()
            return 0
        else:
            return -1


class OperationController:
    def __init__(self, operations: List[Operation]) -> None:
        self.operations = operations
        self.current_operation_index = 0

    def start(self) -> None:
        print("Start operations")
        self.execute_next_operation()

    def execute_next_operation(self) -> None:
        from operation_controller.operations.get_files_http_operation import GetFilesHTTPOperation
        from operation_controller.operations.get_files_sftp_operation import GetFilesSFTPOperation

        if self.current_operation_index < len(self.operations):
            op = Operation(self.operations[self.current_operation_index])
            response = op.execute(self)

            if response == -1:
                self.operations_error()
        else:
            self.operations_completed()

    def operation_error(self, operation: Operation, message: str) -> None:
        self.operations_error()

    def operation_completed(self, operation: Operation) -> None:
        self.current_operation_index += 1
        self.execute_next_operation()

    def operations_error(self) -> None:
        print("Process finished with errors")

    def operations_completed(self) -> None:
        print("Process finished successfully")
