from web3 import Web3, HTTPProvider
from web3.contract import Contract
from web3._utils.events import get_event_data
from web3._utils.abi import exclude_indexed_event_inputs, get_abi_input_names, get_indexed_event_inputs, normalize_event_input_types
from web3.types import ABIEvent
from eth_utils import event_abi_to_log_topic, to_hex
from hexbytes import HexBytes
from pyevmasm import instruction_tables, disassemble_hex, disassemble_all, assemble_hex
from ens import ENS
import json
from cdifflib import CSequenceMatcher
import difflib
difflib.SequenceMatcher = CSequenceMatcher
import hashlib
import yara
import textdistance
import filecmp
import ipfsApi
import requests
import argparse
import subprocess
import shlex
from dotenv import dotenv_values
from flask import Flask,render_template,request
from flask_cors import CORS
# Initializing flask app
app = Flask(__name__)
CORS(app)
dot_env = dotenv_values(".env")
ETHERSCAN_API_KEY = dot_env['ETHERSCAN_API_KEY']
w3 = Web3(HTTPProvider('https://dimensional-muddy-surf.discover.quiknode.pro/ce6130ce76e55ee49c0909c063f57ee15f028315/'))
w3.enable_strict_bytes_type_checking()
Etherscan = "https://etherscan.io/address/"
Verification_URL = "https://etherscan.io/contractsVerified"
AuditVerification_URL = "https://etherscan.io/contractsVerified?filter=audit"
ns = ENS.fromWeb3(w3)




Norenentrancy = yara.compile(filepath='reentrancy.yara')
selfdestruct = yara.compile(filepath='selfdestruct.yara')
PrivateStorage = yara.compile(filepath='PrivateStorage.yara')
BadRandomness = yara.compile(filepath='BadRandomness.yara')
#Get contract events and logs 
#IPFS validator script
#4-byte signature of function call
#pyevmasm.evmasm.disassemble_all(bytecode, pc=0) in a for loop
#ManticoreEVM

def NamedContract(address):
    Name = ns.name(address)
    if Name:
        text = {}
        text['email'] = ns.get_text(Name,'email')
        text['url'] = ns.get_text(Name,'url')
        text['avatar'] = ns.get_text(Name,'avatar')
        text['description'] = ns.get_text(Name,'description')
        text['notice'] = ns.get_text(Name,'notice')
        text['keywords'] = ns.get_text(Name,'keywords')
        text['github'] = ns.get_text(Name,'com.github')
        text['twitter'] = ns.get_text(Name,'com.twitter')
        return {
        "Name" : Name,
        "Owner" : ns.owner(Name),
        "Text" : text
        }
    else:
        return {"Name" : None,
        "Owner" : None,
        "Text" : None
        }

def Comparator(text1,text2):
    for text in difflib.unified_diff(text1.split("\n"), text2.split("\n")):
        if text[:3] not in ('+++', '---', '@@ '):
            print(text)

def BuildHashFromCode(text1,text2):
    damerau_levenshtein = textdistance.damerau_levenshtein.normalized_similarity(text1,text2)
    hamming = textdistance.hamming.normalized_similarity(text1,text2)
    jaro_winkler = textdistance.jaro_winkler.normalized_similarity(text1,text2)
    return {"damerau_levenshtein" : damerau_levenshtein, "hamming" : hamming, "jaro_winkler": jaro_winkler}

def FilesToString(f,g, type):
    f = open(f,'r')
    g = open(g,'r')
    return f,g

def GetFunctionDefinitionTextSignature(Signature):
    headers = {'content-type': 'application/json'}
    r = requests.get("https://www.4byte.directory/api/v1/signatures/?text_signature=%f"%{Signature},headers=headers)
    return r.results

def GetFunctionDefinitionHexSignature(HexSignature):
    headers = {'content-type': 'application/json'}
    r = requests.get("https://www.4byte.directory/api/v1/signatures/?hex_signature=%f"%{HexSignature},headers=headers)
    return r.results

def SubmitFunctionSignature(TextSignature):
    headers = {'content-type': 'multipart/form-data'}
    payload = {"text_signature": TextSignature}
    r = requests.post(url="https://www.4byte.directory/api/v1/import-solidity/",data=payload, headers=headers)

def SubmitDefinitionSignatureFromFiles(Contract):
    headers = {'content-type': 'multipart/form-data'}
    payload = {"source_code": Contract}
    r = requests.post(url="https://www.4byte.directory/api/v1/import-solidity/",data=payload, headers=headers)

def SubmitDefinitionSignatureFromABI(ABI):
    headers = {'content-type': 'application/json'}
    payload = {"contract_abi": ABI}
    r = requests.post(url="https://www.4byte.directory/api/v1/import-solidity/",data=payload, headers=headers)

def FetchSignaturesForCaching():
    headers = {'content-type': 'application/json'}
    r = requests.get(url="https://www.4byte.directory/api/v1/signatures/",headers=headers)
    return r.results

def FetchEventSignaturesForCaching():
    headers = {'content-type': 'application/json'}
    r = requests.get(url="https://www.4byte.directory/api/v1/event-signatures/",headers=headers)
    return r.results

def GenerateHash(text):
    payload= {"input": text,
              "recipe": {"op": "Generate all hashes"}
             }
    r = requests.post(url="127.0.0.1:3000/bake",payload=payload)
    return r.value

def GetFromEtherscan(address,action):
    if action == 'getsourcecode' or action == 'getabi':
        headers = {'content-type': 'application/json'}
        r = requests.get(url="https://api.etherscan.io/api?module=contract&action=%s&address=%s&apikey=%s"%(action,address,ETHERSCAN_API_KEY),headers=headers)
        return r.text

def Run(address):
    #command_line = Would run a scanner which give a json output 
    args = shlex.split(command_line)
    p = subprocess.Popen(args)

def yara_callback(data):
  return yara.CALLBACK_CONTINUE


def ComparerAddress(args):
    result = NamedContract(args.address)
    source = GetFromEtherscan(args.address, 'getsourcecode')
    result = result | { 'source' : source }
    result = result | { 'ABI' : GetFromEtherscan(args.address, 'getabi')}
    result = result | {'EtherScanLink' : "%s%s"%(Etherscan,args.address)}
    result = result | {'EtherScanVerification' : Verification_URL}
    result = result | {'EtherScanAudit' : AuditVerification_URL }
    matches = Norenentrancy.match(data=source, callback=yara_callback, which_callbacks=yara.CALLBACK_MATCHES, timeout=60)
    if matches:
        result = result | {"Reentrancy" : False}
    else:
        result = result | {"Reentrancy" : "Potential"}
    matches = selfdestruct.match(data=source, callback=yara_callback, which_callbacks=yara.CALLBACK_MATCHES, timeout=60)
    if matches:
        result = result | {"SelfDestruct" : False}
    else:
        result = result | {"SelfDestruct" : True}
    matches = PrivateStorage.match(data=source, callback=yara_callback, which_callbacks=yara.CALLBACK_MATCHES, timeout=60)
    if matches:
        result = result | {"PrivateStorage" : matches.matches}
    else:
        result = result | {"PrivateStorage" : False}
    matches = BadRandomness.match(data=source, callback=yara_callback, which_callbacks=yara.CALLBACK_MATCHES, timeout=60)
    if matches:
        result = result | {"BadRandomness" : matches.matches}
    else:
        result = result | {"BadRandomness" : False}
    print(result)

@app.route('/index.html')
def serve():
    return render_template('index.html',form_data = {})
@app.route('/result',methods = ['POST'])
def Postserve():
    form_data = request.form
    form_data = ComparerAddress(form_data)
    return render_template('index.html',form_data = form_data)

if __name__ == '__main__':
    app.run(debug=True)

    #parser = argparse.ArgumentParser(description='Filepaths of contract to compare')
    #parser.add_argument('--path1',help='Filepath of the source contract')
    #parser.add_argument('--path2',help='Filepath of the compared contract')
    #parser.add_argument('--type',choices=['ABI','source','address'], help="Type of file provided")
    #parser.add_argument('--address', help="Address of the smart contract")
    #args = parser.parse_args()
    #if args.path1 and args.path2 and args.type in ['ABI','source']:
    #    args = parser.parse_args()
    #    Comparer(args)
    #elif args.type == 'address' and args.address:
    #    args = parser.parse_args()
    #    ComparerAddress(args)


        

