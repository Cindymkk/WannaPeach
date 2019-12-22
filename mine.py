import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

def mine():
	# we run the proof of work algorithm to get the next proof
	last_block = blockChain.last_block
	last_proof = last_block['proof']
	proof = blockChain.proof.proof_of_work(last_proof)
	# 给工作量证明的节点提供奖励，发送者为“0”表明是新挖出来的区块
	blockChain.new_transaction(sender="0", recipient=node_identifier, amount=1)
	#for the new block by adding it to the chain
	block = blockChain.new_block(proof)
	response = {
		'message' : "New Block",
		'index' : block['index'],
		'transactions' : block['transactions'],
		'proof' : block['proof'],
		'previous_hash' : block['previous_hash'],
	}
	return jsonify(response), 200