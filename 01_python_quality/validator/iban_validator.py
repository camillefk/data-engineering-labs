def _rearrange_iban(iban: str) -> str:
    """Move os 4 primeiros caracteres (Country code + Check digits) para o final."""
    return iban[4:] + iban[:4]

def _convert_letters_to_numbers(iban: str) -> str:
    """Substitui letras por numeros inteiros (A=10...Z=35) de acordo com a norma ISO 13616."""
    converted = []
    for char in iban:
        if char.isdigit():
            converted.append(char)
        else:
            # Colocar em maiúsculas garante que ‘a’ se comporte como ‘A’
            val = ord(char.upper()) - 55
            converted.append(str(val))
    return "".join(converted)

def validate_iban(iban: str) -> bool:
    """
    Validates an International Bank Account Number (IBAN).
    
    Implements the Modulo 97 algorithm (ISO 7064).
    
    Args:
        iban (str): The IBAN string (spaces are allowed).
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not iban:
        return False

    clean_iban = iban.replace(" ", "")

    if len(clean_iban) < 4:
        return False

    # Step 1: Rearrange
    rearranged_iban = _rearrange_iban(clean_iban)

    # Step 2: Convert to numeric string
    numeric_iban = _convert_letters_to_numbers(rearranged_iban)

    # Step 3: Modulo 97 check
    MODULO_CONSTANT = 97
    return int(numeric_iban) % MODULO_CONSTANT == 1
