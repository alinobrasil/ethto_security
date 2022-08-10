POC of a a due-dilligance and initial safety check to assess a solidity smart-contract prior to user interaction.The goal would be to have it as a browser extension to catch up transaction request prior for them to be validated by the user so they can review and decide weither they want to interact with it. The idea behind it was to make it user-friendly to interact with such information without relying on the user to manually go to different resources to validate a smart contract prior to interacting with it, wheither or not you are developper. It would be ideal that the tool act with basic scoring and/or YES/NO checks which are easy for the user to understand and to watch out for. 

Features implemented: 
[X] Check if ENS exist for address
[X] Give useful insight about metadata in the ENS
[X] Fetch the ABI and Source if available from Chain Explorer (EtherScan currently)
[X] Yara rules for basic signature of anti-features(partial)
[] Implement some output of Audit tool 
[] ABI decoding
[] Source flattening
[] Fetch IPFS 

Roadmap:
-Building the extension itself
-Prettify the output
-Add functionnality for hash based dependency(imphash), file hashes, differencial, etc...
-Create more yara rules and improve existing one to cover more hacks
-Broaden the scope of the tool to multichain
-Build a Chain Explorer
-Trust-based system of vauching
-History of "user" push of smart contract
-Add memory of contract so a diff
-Reporting system(reputation based)

