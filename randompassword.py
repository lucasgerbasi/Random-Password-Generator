import random
import string

def gerar_senha(comprimento=12):
    """Gerar uma senha aleatória."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

if __name__ == "__main__":
    num_senhas = 5  # Você pode alterar esse número para gerar mais senhas
    senhas = [gerar_senha() for _ in range(num_senhas)]
    for i, senha in enumerate(senhas, start=1):
        print(f"Senha {i}: {senha}")