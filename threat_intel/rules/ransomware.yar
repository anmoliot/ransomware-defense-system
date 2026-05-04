rule Ransomware_Note_Keyword
{
    strings:
        $a = "your files are encrypted" nocase
        $b = "bitcoin" nocase
        $c = "decrypt" nocase
    condition:
        2 of them
}

rule Shadow_Copy_Delete
{
    strings:
        $a = "vssadmin" nocase
        $b = "delete shadows" nocase
    condition:
        all of them
}
