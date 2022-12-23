import dns.resolver
import socket

class DomainResolver:

    def get_ip(self, domain_name: str) -> dict:
        try:
            ip = socket.gethostbyname(domain_name)
            return {"ip": ip}
        except socket.gaierror:
            return {"error": "Unable to resolve domain name"}

    def get_records(self, domain_name: str) -> dict:
        records = []
        try:
            # Query for A records (IPv4 addresses)
            answers = dns.resolver.resolve(domain_name, "A", rdclass=dns.rdataclass.IN)
            for rdata in answers:
                records.append({
                    "type": "A",
                    "value": str(rdata)
                })

            return {"records": records}
        except dns.resolver.NoAnswer:
            return {"records": []}
        except dns.resolver.NXDOMAIN:
            return {"error": "Unable to resolve domain name"}


resolver = DomainResolver()
ip = resolver.get_records("6151027.com")
print(ip)