from re import findall, match, compile

# validAlpha = "[A-Za-z0-9-_ ]+$"

validAlpha = "[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\-_\\s]+$"

validAlphaNumeric = "[A-Za-z0-9_À-ÿ.-_\\s]+$"

# validAlpha = "[A-Za-zÀ-ÿ^']+"

texto = "Língua .Portuguesa Acentuação de palavras"

# print("validAlpha", validAlpha)

if not match(validAlpha, texto):
    print("Texto inválido")
