# vowel or consonant
char = input("Enter a character:")

match char:
    case char if char in ["a","e","i","o","u","A","E","I","O","U"]:
        print("It is a vowel")
    case char if char in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z',
                          'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']:
        print("It is consonant")
    case _:
        print("Special symbols and numbers not allowed...........")
