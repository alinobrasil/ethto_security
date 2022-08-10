rule SelfDestruct
{
    strings:
        $my_text_string = "address(this).balance" fullword
    condition:
        $my_text_string
}