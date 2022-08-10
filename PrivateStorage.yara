rule PrivateStorage
{
    strings:
        $my_text_string = "password" fullword
    condition:
        $my_text_string
}