import click
from pythonping import ping
from tabulate import tabulate
from scanner import Scanner
from show_table import Table

scan = Scanner()
tbl = Table()

class Functions():
    def __init__(self):
        pass

    @click.command()
    @click.option('--multiple', default=False)
    @click.option('--nodes')
    def view_status(multiple, nodes):
        if multiple == False:
            data = scan.ping_node(nodes)
        else:
            data = scan.run_scan(nodes)
        print('\n')
        print(tbl.create_table(data))
        print(f"Nodes online: {len(scan.online_nodes)}\nNodes offline: {len(scan.offline_nodes)}")
