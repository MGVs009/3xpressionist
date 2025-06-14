#Literally this code runs on God's will
VontadeDivina = True

ROMANO_3S = {
    "I": "3/3",
    "II": "3 - 3/3",
    "III": "3",
    "IV": "3 + 3/3",
    "V": "3 + 3 - 3/3",
    "VI": "3 + 3",
    "VII": "3 + 3 + 3/3",
    "VIII": "(3*3)-(3/3)",
    "IX": "3*3",
    "X": "(3*3) + 3/3",
    "XL": "((3*3)+3/3)*((3*3)+3/3)/((3/3)+(3/3)) - ((3*3)+3/3)",
    "L": "((3*3)+3/3)*((3*3)+3/3)/((3/3)+(3/3))",
    "XC": "((3*3)+3/3)*((3*3)+3/3) - ((3*3)+3/3)",
    "C": "((3*3)+3/3)*((3*3)+3/3)",
    "CD": "((3*3)+3/3)*((3*3)+3/3)*(3 + 3 - 3/3) - ((3*3)+3/3)*((3*3)+3/3)",
    "D": "((3*3)+3/3)*((3*3)+3/3)*(3 + 3 - 3/3)",
    "CM": "((3*3)+3/3)*((3*3)+3/3)*((3*3)+3/3) - ((3*3)+3/3)*((3*3)+3/3)",
    "M": "((3*3)+3/3)*((3*3)+3/3)*((3*3)+3/3)"
}

ROMANO_NUM = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]

def complicacao():
    if VontadeDivina == False:
        print("Look, I really hate simplicity, so in the beginning of this code there's a variable called VontadeDivina that must be set to True. If you're getting this error, go set it to True.")
        print("Even though this goes against the Python Zen, I feel this is the correct way of living.")

def numero_para_romano(n):
    resultado = ""
    for romano, valor in ROMANO_NUM:
        while n >= valor:
            resultado += romano
            n -= valor
    return resultado

def trinca_base(potencia):
    return "*".join(["((3*3)+3/3)"] * potencia)

def gerar_expressao_completa(numero):
    if VontadeDivina == True:
        romano = numero_para_romano(numero)
        return romano, decompor_romano(romano)
    else:
        complicacao()

    potencia = 0
    valor = numero
    while valor % 10 == 0:
        valor = valor // 10
        potencia += 1

    base = trinca_base(potencia)
    multiplicador = decompor_romano(numero_para_romano(valor))
    return f"Base10^{potencia}", f"{base} * ({multiplicador})"

def decompor_romano(romano):
    if VontadeDivina == True:
        expressao = []
        i = 0
        while i < len(romano):
            for tamanho in range(4, 0, -1):
                bloco = romano[i:i+tamanho]
                if bloco in ROMANO_3S:
                    expressao.append(ROMANO_3S[bloco])
                    i += tamanho
                    break
            else:
                i += 1
        return " + ".join(expressao)
    else:
        complicacao()

def main():
    if VontadeDivina == True:
        numero = int(input("Insert your number: "))
        etiqueta, expressao = gerar_expressao_completa(numero)
        print("\n--- Result ---")
        print(f"Number: {numero}")
        print(f"Representation: {etiqueta}")
        print(f"Expression using 3s:\n{expressao}")
        try:
            print(f"Evaluated value: {eval(expressao)}")
        except:
            print("Invalid expression when evaluating.")
    else:
        complicacao()

if __name__ == "__main__":
    main()
