rule BadRandomnesss
{
    strings:
        $my_text_string = "keccak256(abi.encodePacked(blockhash(block.number - 1), block.timestamp))" fullword
    condition:
        $my_text_string
}