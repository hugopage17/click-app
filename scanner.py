from pythonping import ping
from progress.bar import IncrementalBar
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup

class Scanner(object):
    def __init__(self):
        self.online_nodes = []
        self.offline_nodes = []

    def ping_node(self, node):
        response = ping(node, size=32, timeout=1, count=1)
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
        return data

    def run_scan(self, nodes):
        data = []
        all_ips = []
        nodes = nodes.split('-')
        last_oct = nodes[1]
        first_oct = str(nodes[0]).split('.')[3]
        nodes = str(nodes[0]).split('.')
        nodes.remove(nodes[3])
        finder = int(first_oct)
        array_to_return = []
        nodes = '.'.join(nodes)
        while finder <= int(last_oct):
            ip = nodes+'.'+str(finder)
            all_ips.append(ip)
            finder+=1
        bar = IncrementalBar(max=len(all_ips))
        for i in all_ips:
            response = ping(i, size=32, timeout=1, count=1)
            res = str(response._responses[0])
            status = ''
            time = ''
            if res != 'Request timed out':
                status = 'Online'
                self.online_nodes.append(i)
                time = str(response.rtt_avg_ms)+'ms'
                try:
                    mac = MacLookup()
                    ip_mac = get_mac_address(ip=i)
                    vendor = mac.lookup(ip_mac)
                except:
                    ip_mac = 'N/A'
                    vendor = 'N/A'
            else:
                status = 'Offline'
                self.offline_nodes.append(i)
                time = 'Unreachable'
                ip_mac = 'N/A'
                vendor = 'N/A'
            data.append([i,status, time, ip_mac, vendor])
            bar.next()
        return data
