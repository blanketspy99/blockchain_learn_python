import json
from p2pnetwork.node import Node
from BlockchainUtils import BlockchainUtils
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConector

class SocketCommunication(Node):
    def __init__(self, ip, port) -> None:
        super().__init__(ip, port, None)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConector(ip, port)

    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost', 10001)

    def startSocketCommunication(self):
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()

    def inbound_node_connected(self, connected_node):
        #print('inbound connection')
        #self.send_to_node(connected_node, "Hi I am the node you connected to")
        self.peerDiscoveryHandler.handshake(connected_node)
        #return super().inbound_node_connected(connected_node)

    def outbound_node_connected(self, connected_node):
        #print('outbound connection')
        #self.send_to_node(connected_node, "Hi I am the node who initialised the connection")
        self.peerDiscoveryHandler.handshake(connected_node)

        #return super().outbound_node_connected(connected_node)

    def node_message(self, connected_node, message):
        #print(message)
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == 'DISCOVERY':
            self.peerDiscoveryHandler.handleMessage(message)
        #return super().node_message(node, data)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)