import nmap
import json
import time
from module import *

class PortScanner(SQLite3Handle):
    def __init__(self, host, ports, db_file):
        super().__init__(db_file)  # 调用父类的 __init__ 方法
        self.host = host
        self.ports = ports
        self.nm = nmap.PortScanner()

    def scan(self):
        start_time = time.time()  # Get the current time before starting the scan
        self.nm.scan(self.host, self.ports, arguments='-T4 --min-rate 1000')

        results = []
        for host in self.nm.all_hosts():
            host_dict = {}
            host_dict['host'] = host
            host_dict['hostname'] = self.nm[host].hostname()
            host_dict['state'] = self.nm[host].state()
            host_dict['protocols'] = []
            for proto in self.nm[host].all_protocols():
                proto_dict = {}
                proto_dict['protocol'] = proto
                proto_dict['ports'] = []
                lport = list(self.nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    port_dict = {}
                    port_dict['port'] = port
                    port_dict['state'] = self.nm[host][proto][port]['state']
                    proto_dict['ports'].append(port_dict)
                host_dict['protocols'].append(proto_dict)
            results.append(host_dict)

        end_time = time.time()  # Get the current time after the scan has completed
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f'[+]Scan completed in {elapsed_time:.2f} seconds')  # Print the elapsed time in a formatted string

        return json.dumps(results, indent=4)

    def save_to_database(self):
        """保存扫描结果到数据库中"""
        self.connect()  # 连接数据库
        for host in self.nm.all_hosts():
            hostname = self.nm[host].hostname()
            state = self.nm[host].state()
            for proto in self.nm[host].all_protocols():
                lport = list(self.nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    port_state = self.nm[host][proto][port]['state']
                    data = {
                        'host': host,
                        'hostname': hostname,
                        'state': state,
                        'protocol': proto,
                        'port': port,
                        'port_state': port_state,
                    }
                    print(data)
                    self.insert('scan', data)  # 插入数据
        self.close()  # 关闭数据库连接


if __name__ == '__main__':
    scanner = PortScanner('66.203.149.116', '80-443',"./module/mydatabase.db")
    results = scanner.scan()
    scanner.save_to_database()
