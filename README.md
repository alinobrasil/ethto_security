POC for a module that quickly and automatically undertakes an assessment of due-diligence, safety and valifity of solidity-based smart contracts and returns whether the contract is trustworthy and safe, or not (or, lacking information, may not have full confidence to decide).\

The module would function *prior* to user interaction with the new smart contract.ideally it would be factored and integrated into we web 3.0 wallets, to ensure intents from unknown and potentially untrustworthy smart contracts would have to be assessed by it prior to the dApp being permitted to interact with the wallet – full wallet integration is the end-goal; in the interim it would be like start as a browser extension with permission to interupt intents to interact with wallets, and run its routine so that the the user can then review and decide whether they want to permit further interaction with it. 

The rationale behind its design and future direction is that it ideally the application and function is not something a user ever need to even think about or interact with - it crunches data and analaytics in the background, and the user simply receives its assements for them to act on. Most users are not keen to collect data and validate code and contract for every new and unknown dApp they might come to interact with. 

Our goal is that users do regularly receive a best-judgment indication of the trustworthiness and safety of the smart contracts they interact with. Something that does not happen currently, yet aught to - akin to wandering around the web 2.0 with no antivirus/malware/spyware and just downloading files you come across, however with the web 3.9 and many of these smart contracts and dApps, you'd be wandering around with your wallet wide open

Features implemented: <br /
[X] Check if ENS exists for address<br />
[X] Retreive any present and useful metadata if ENS present<br />
[X] Fetch the ABI and Source if available from Chain Explorer (EtherScan currently)<br />
[X] Yara rules for basic signature of anti-features(partial)<br />
[] Implement some output of Audit tool <br />
[] ABI decoding<br />
[] Source flattening<br />
[] Fetch IPFS <br />

Roadmap:<br />
-Building the extension itself<br />
-Pretitify the output<br />
-Add functionality for hash-based dependency(imphash), file hashes, differencial, etc...<br />
-Build the first Smart Contract YARA rules DB (required: decude on what analytics we want and need to be collectiing to optimally create this) <br />
  -Well crafted Privacy Policy <br />
-Create more yara rules and improve existing one to cover more hacks<br />
-Broaden the scope of the tool to multichain<br />
-Build a Chain Explorer<br />
-Trust-based system of vauching<br />
-History of "user" push of smart contract<br />
-Add memory of contract so a diff<br />
-Integration with web3.0 wallets <br />
-Android and/or iOS apps depending on workability of web app <br />
-Reporting system(reputation based)<br />
