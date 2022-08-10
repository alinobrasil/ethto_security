rule NoReentrancy
{
    strings:
        $my_text_string = "modifier" fullword
        $my_text_string1 = "require(!locked" fullword
        $my_text_string2 = "locked = true" fullword
        $my_text_string3 = "locked = false;" fullword
    condition:
        $my_text_string at @my_text_string1[1] and $my_text_string1 at @my_text_string2[1] and $my_text_string2 at @my_text_string3[1]
}