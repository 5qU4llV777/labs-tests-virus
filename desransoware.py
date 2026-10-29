import os
from cryptography.fernet import Fernet

# 1. Carregar a chave de criptografia salva anteriormente
try:
    with open("chave_resgate.key", "rb") as arquivo_chave:
        chave = arquivo_chave.read()
except FileNotFoundError:
    print("❌ Erro: O arquivo 'chave_resgate.key' não foi encontrado no diretório atual.")
    exit()

# 2. Inicializar o motor de descriptografia
fernet = Fernet(chave)

# 3. Definir a pasta alvo (Deve ser a mesma usada no ataque)
pasta_alvo = r"C:\Users\target\Desktop\Arquivos_Importantes"
print("🔓 Iniciando processo de descriptografia...")

# 4. Varrer a pasta e descriptografar os arquivos
for raiz, diretorios, arquivos in os.walk(pasta_alvo):
    for arquivo in arquivos:
        if arquivo.endswith(".locked"):
            caminho_completo = os.path.join(raiz, arquivo)
            
            # Ler o conteúdo criptografado
            with open(caminho_completo, "rb") as f:
                conteudo_criptografado = f.read()
            
            try:
                # Descriptografar o conteúdo
                conteudo_original = fernet.decrypt(conteudo_criptografado)
                
                # Definir o nome original (removendo o .locked)
                caminho_original = caminho_completo[:-7]
                
                # Salvar o arquivo restaurado
                with open(caminho_original, "wb") as f:
                    f.write(conteudo_original)
                
                # Remover o arquivo criptografado antigo
                os.remove(caminho_completo)
                print(f"✅ Restaurado: {arquivo} -> {os.path.basename(caminho_original)}")
                
            except Exception as e:
                print(f"❌ Falha ao descriptografar {arquivo}: {e}")

# 5. Opcional: Remover a nota de resgate para limpar o ambiente
nota_resgate = os.path.join(pasta_alvo, "LEIA-ME_NOTA_DE_RESGATE.txt")
if os.path.exists(nota_resgate):
    os.remove(nota_resgate)
    print("🗑️ Nota de resgate removida.")

print("\n🎉 Processo concluído! Os arquivos voltaram ao estado original.")
