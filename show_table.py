from tabulate import tabulate

class Table():
    def __init__(self):
        pass

    def create_table(self, data):
        table = tabulate(data, headers=["Address","Status", "Response Time", "MAC Address", "Vendor"],tablefmt="grid")
        return table
