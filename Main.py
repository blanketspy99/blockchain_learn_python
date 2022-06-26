from re import T
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint

from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys


if __name__ == '__main__':
    '''
    sender='sender'
    receiver='receiver'
    amount=1
    type='TRANSFER'

    
    transaction=Transaction(sender,receiver,amount,type)
    #print(transaction.toJson())

    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    print(signature)
    transaction.sign(signature)
    print(transaction.toJson())
    signatureValid=Wallet.signatureValid(transaction.payload(),signature, wallet.publicKeyString())
    print(signatureValid) '''
    '''
    wallet = Wallet()
    pool=TransactionPool()
    transaction = wallet.createTransaction(receiver, amount, type)
    #print(transaction.payload())
    #print(transaction.payload(), transaction.signature, wallet.publicKeyString())
    signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, wallet.publicKeyString())

    #print(signatureValid)
    
    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)


    #print(pool.transactions)
    #block = Block(pool.transactions, 'lastHash', 'forger', 1)
    #print(block.toJson())
    blockchain = Blockchain()
    lastHash = BlockchainUtils.hash(
        blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1

    block = wallet.createBlock(pool.transactions, lastHash, blockCount)
    signatureValid = Wallet.signatureValid(block.payload(),block.signature,wallet.publicKeyString())
    pprint.pprint(block.toJson())
    print(signatureValid) 

    if not blockchain.lastBlockHashValid(block):
        print('last block is not valid')

    if not blockchain.blockCountValid(block):
        print('blockcount is not valid')

    if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        blockchain.addBlock(block)
    #blockchain = Blockchain()
    #blockchain.addBlock(block)
    pprint.pprint(blockchain.toJson())  '''

    '''wallet = Wallet()
    accountModel = AccountModel()

    #accountModel.addAccount(wallet.publicKeyString())
    accountModel.updateBalance(wallet.publicKeyString(), 10)
    accountModel.updateBalance(wallet.publicKeyString(), -5)
    print(accountModel.balances) '''
    '''
    Blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    exchangeTransaction = exchange.createTransaction(alice.publicKeyString(),10, 'EXCHANGE')
    
    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    coveredTransaction = Blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(Blockchain.blocks[-1].payload()).hexdigest()
    
    blockCount = Blockchain.blocks[-1].blockCount + 1
    #blockOne=Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    blockOne=forger.createBlock(coveredTransaction, lastHash, blockCount)
    Blockchain.addBlock(blockOne)
    pool.removeFromPool(blockOne.transactions)
    #alice wants to send 5 tokesn to Bob
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransaction = Blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(Blockchain.blocks[-1].payload()).hexdigest()
    blockCount = Blockchain.blocks[-1].blockCount + 1
    blockTwo=forger.createBlock(coveredTransaction, lastHash, blockCount)
    #blockTwo=Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    Blockchain.addBlock(blockTwo)
    pool.removeFromPool(blockTwo.transactions)

    pprint.pprint(Blockchain.toJson())'''

    """node = Node()
    print(node.blockchain)
    print(node.transactionPool)
    print(node.wallet)"""

    ip = sys.argv[1]
    port = int(sys.argv[2])
    node = Node(ip, port)
    node.startP2P()