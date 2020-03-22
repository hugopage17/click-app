import click
from pythonping import ping
from tabulate import tabulate
from progress.bar import IncrementalBar
from scanner import Scanner

scan = Scanner()

class Functions():
    def __init__(self):
        pass

    @click.command()
    @click.option('--address')
    def run_ping(address):
        response = ping(address, size=32, timeout=10, count=1)
        click.echo(f"Response: {response.rtt_avg_ms}ms")

    @click.command()
    @click.option('--multiple', default=False)
    @click.option('--nodes')
    def view_status(multiple, nodes):
        data = []
        online_nodes = []
        offline_nodes = []
        if multiple == False:
            response = ping(nodes, size=32, timeout=1, count=1)
            res = str(response._responses[0])
            status = ''
            time = ''
            if res != 'Request timed out':
                status = 'Online'
                time = str(response.rtt_avg_ms)+'ms'
            else:
                status = 'Offline'
                time = 'Unreachable'
            data.append([nodes,status, time])
        else:
            data = scan.run_scan(nodes)
        print('\n')
        table = tabulate(data, headers=["Address","Status", "Response Time", "MAC Address", "Vendor"],tablefmt="grid")
        print(table)
        print(f"Nodes online: {len(online_nodes)} - Nodes offline: {len(offline_nodes)}")
