

from ipaddress import ip_address


class SocketConector():

    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port

    def equals(self, connector):
        if connector.ip == self.ip and connector.port == self.port:
            return True
        else:
            return False