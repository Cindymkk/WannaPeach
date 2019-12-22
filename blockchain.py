import hashlib
import json
from time import time

class Blockchain(object):
	def __init__(self):
		self.current_transactions =[]
		self.chain = []
		# Create the genesis block
		self.new_block(previous_hash = 1, proof = 100)
	def new_block(self, proof, previous_hash = None):
		'''
		Create a new block
		:param proof: <init> The proof given by the Proof of work algorithm
		:param previous_hash: (Optional) <str> Hash of previous block
		:return: <dict> new Block
		'''
		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transaction': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}
		# reset the current list of transactions
		self.current_transactions = []
		self.chain.append(block)
		return block
	def new_transaction(self, sendor, recipient, amount):
		'''
		generate new transactions, the information will be added to the next block
		:param sendor: <str> Address of the Sendor
		:param recipient: <str> Address of the Recipient
		:param amount: <int> Amount
		:return: <int> The index of the Block the will hold this transaction
		'''
		self.current_transactions.append({
			'sendor': sendor,
			'recipient': recipient,
			'amount':amount,
		})
		return self.last_block['index'] + 1
	@property
	def last_block(self):
		return self.chain[-1]
	@staticmethod
	def hash(block):
		'''
		generate the SHA-256 hash of the block
		:param block: <dict> Block
		:return: <str>
		'''
		block_string = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(block_string).hexdigest()
