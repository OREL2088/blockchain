import hashlib
import json
import datetime

class Block:
    def __init__(self, index, timestamp, data, previousHash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        string = str(self.index) + self.previousHash + self.timestamp + json.dumps(self.data) + str(self.nonce)
        return hashlib.sha256(string.encode()).hexdigest()

    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
        print("Block mined: " + self.hash)

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previousHash,
            'hash': self.hash,
            'nonce': self.nonce
        }


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesis()]
        self.difficulty = 4

    def createGenesis(self):
        return Block(0, "01/01/2018", "Genesis block", "0")

    def latestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.latestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def checkValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
        return True


def main(num):
    enlightChain = Blockchain()

    timestamp = datetime.datetime.now().strftime("%d/%m/%Y")

    for i in range(1, num):
        print("Mining block...")
        enlightChain.addBlock(Block(i, timestamp, f"This is block {i}"))

    for block in enlightChain.chain:
        print(block.timestamp)
        print(block.data)
        print('Previous_hash:', block.previousHash)
        print('Hash:', block.hash)
        print('Nonce:', block.nonce)
        print()
    print("Is blockchain valid?" + str(enlightChain.checkValid()))


while True:
    try:
        num = int(input('Enter the desired number of blocks in the chain:'))
        main(num)
        break
    except ValueError:
        print("Error! Enter an integer.")
