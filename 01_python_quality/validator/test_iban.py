from iban_validator import validate_iban

def test_should_return_true_for_valid_german_iban():
    #Arrange: Um IBAN real e válido
    #(Este numero passa na regra do Módulo 97)
    valid_iban = "DE89 3704 0044 0532 0130 00"

    #Act
    is_valid = validate_iban(valid_iban)

    #Assert
    assert is_valid is True

def test_should_return_false_for_invalid_iban():
    #Arrange: O mesmo IBAN, mas com o final alterado
    invalid_iban = "DE89 3704 0044 0532 0130 99"

    #Act e Assert
    assert validate_iban(invalid_iban) is False
