# Laboratório de Simulação de Malware - Apenas Fins Educacionais

> ⚠️ **AVISO**: Este diretório contém simulações educacionais de comportamento de malware. Estas ferramentas foram projetadas **APENAS** para aprendizado de cibersegurança em ambientes isolados e controlados. Incluem múltiplas proteções de segurança para evitar danos acidentais.

## Visão Geral

Este laboratório fornece simulações seguras e controladas de dois tipos comuns de malware:
1. **Simulação de Ransomware** - Demonstra comportamento de criptografia de arquivos
2. **Simulação de Keylogger** - Demonstra comportamento de captura de teclas

Ambos os simuladores incluem extensas funcionalidades de segurança e operam **APENAS** dentro de diretórios de teste designados.

---

## Funcionalidades de Segurança (Ambos Simuladores)

| Funcionalidade | Descrição |
|----------------|-----------|
| **Diretório de Teste Isolado** | Operações restritas a caminhos de teste predefinidos |
| **Confirmação Explícita** | Requer digitar `CONFIRM` antes de qualquer ação destrutiva |
| **Limites de Auto-Parada** | Keylogger: 1000 teclas ou 5 minutos máximo |
| **Sem Comunicação de Rede** | Zero conexões externas - todos os dados ficam locais |
| **Sem Persistência** | Sem mecanismos de inicialização, registro ou tarefas agendadas |
| **Log Completo** | Todas as ações registradas em arquivos locais para revisão |
| **Capacidade de Recuperação** | Simulador de ransomware inclui funcionalidade de descriptografia |

---

## Estrutura de Diretórios

```
malware-simulation/
├── README.md                                    # Este arquivo
├── ransomware/
│   ├── safe_ransomware_sim.py                  # Simulador de ransomware
│   ├── test_files/                             # Diretório de teste (auto-criado)
│   ├── encryption_key.key                      # Chave de criptografia (gerada)
│   ├── ransomware.log                          # Log de atividades
│   └── RANSOM_NOTE.txt                         # Nota de resgate educacional
└── keylogger/
    ├── safe_keylogger_sim.py                   # Simulador de keylogger
    ├── logs/
    │   ├── keystrokes.log                      # Teclas capturadas
    │   ├── session.json                        # Metadados da sessão
    │   ├── config.json                         # Configuração
    │   └── keylogger.log                       # Log de atividades
    └── keylogger.txt                           # Referência Metasploit (veja abaixo)
```

---

## Simulador de Ransomware (`ransomware/safe_ransomware_sim.py`)

### Propósito
Demonstra como ransomware criptografa arquivos usando criptografia simétrica (Fernet/AES-128), cria notas de resgate e como a recuperação funciona com a chave de criptografia.

### Funcionalidades
- Cria arquivos de teste realistas (documentos, JSON, bancos de dados, imagens, arquivos)
- Criptografa arquivos usando Fernet (AES-128 no modo CBC com HMAC)
- Gera chave de criptografia única por sessão
- Cria nota de resgate educacional com orientações de defesa
- **Capacidade completa de descriptografia** para recuperação
- Validação de caminho impede operação fora do diretório de teste

### Uso
```bash
cd /media/dragonborn/Dados/ZEUS/scriptpentester/malware-simulation/ransomware
python3 safe_ransomware_sim.py
```

### Opções do Menu
1. **Criar arquivos de teste** - Gera arquivos de exemplo para criptografia
2. **Criptografar arquivos** - Simula ataque de ransomware (requer CONFIRM)
3. **Descriptografar arquivos** - Recupera arquivos usando chave salva (requer CONFIRM)
4. **Ver nota de resgate** - Mostra nota de resgate educacional
5. **Ver log** - Mostra log de atividades
0. **Sair**

### Pontos de Aprendizado
- Ransomware real usa criptografia similar mas se espalha lateralmente
- Atacantes deletam cópias de sombra/backups antes de criptografar
- Pagamento não garante descriptografia (não há honra entre ladrões)
- **Defesa**: Backups offline, segmentação de rede, EDR, treinamento de usuários

---

## Simulador de Keylogger (`keylogger/safe_keylogger_sim.py`)

### Propósito
Demonstra como keyloggers capturam teclas, armazenam localmente e como a exfiltração funcionaria (apenas simulada).

### Funcionalidades
- Captura teclas usando biblioteca `pynput`
- Sanitiza entrada (filtra apenas caracteres permitidos)
- Registra em arquivo local com timestamps
- Rastreamento de sessão com metadados JSON
- **Exfiltração de email simulada** - mostra o que atacantes enviariam (NENHUM email real)
- Auto-para nos limites de segurança (1000 teclas / 5 minutos)
- Tecla ESC para parada antecipada

### Uso
```bash
cd /media/dragonborn/Dados/ZEUS/scriptpentester/malware-simulation/keylogger
python3 safe_keylogger_sim.py
```

### Opções do Menu
1. **Iniciar keylogger** - Inicia captura (requer CONFIRM)
2. **Ver logs capturados** - Mostra teclas e dados da sessão
3. **Simular exfiltração por email** - Demo de roubo de dados (NENHUMA transmissão real)
4. **Ver configuração de segurança** - Mostra limites e caminhos atuais
0. **Sair**

### Pontos de Aprendizado
- Keyloggers reais rodam silenciosamente em background com persistência
- Exfiltração de dados via SMTP, HTTP, DNS tunneling, FTP
- **Defesa**: EDR/XDR, DLP de rede, análise comportamental, whitelist de aplicações

---

## Referência Metasploit (`keylogger/keylogger.txt`)

Este arquivo contém comandos de referência para usar o Metasploit Framework para criar um payload Meterpreter com capacidade de keylogging. **Esta é apenas uma referência educacional** - entender como atacantes usam estas ferramentas ajuda defensores a detectar e prevenir tais ataques.

### Conteúdo
- Comando `msfvenom` para gerar executável reverse shell Windows x64
- Comandos `msfconsole` para configurar handler
- Comandos Meterpreter `keyscan_start` / `keyscan_dump` para keylogging

### Notas Importantes
- **Requer autorização explícita** - Use apenas em ambientes de laboratório que você possui
- Windows moderno (10/11) tem defesas: AMSI, WDAC, ETW, CFG
- Meterpreter é fortemente assinado - facilmente detectado por EDR
- Isso demonstra fase de **pós-exploração** após comprometimento inicial

---

## Pré-requisitos

```bash
# Pacotes Python
pip install cryptography pynput

# Para referência Metasploit (opcional)
# Metasploit Framework deve ser instalado separadamente
```

---

## Diretrizes de Uso Ético

| ✅ Permitido | ❌ Proibido |
|--------------|-------------|
| Executar em VM/laboratório isolado | Executar em sistemas de produção |
| Estudar código para aprendizado | Modificar para remover proteções de segurança |
| Usar para pesquisa de defesa | Distribuir como malware funcional |
| Analisar padrões de comportamento | Alvejar sistemas não autorizados |
| Demonstrações educacionais | Qualquer uso malicioso |

---

## Aviso Legal

**Estas ferramentas são fornecidas apenas para fins educacionais e de teste autorizado.**

- Use apenas em ambientes que você possui ou tem permissão escrita explícita para testar
- Os autores não são responsáveis por qualquer uso indevido ou dano causado por estas ferramentas
- Acesso não autorizado a sistemas computacionais é ilegal na maioria das jurisdições
- Sempre cumpra leis e regulamentos locais

---

## Recursos para Aprendizado Adicional

- **MITRE ATT&CK**: https://attack.mitre.org/ (Técnicas T1056, T1486)
- **PortSwigger Web Security Academy**: https://portswigger.net/web-security
- **Análise de Malware**: Practical Malware Analysis por Sikorski & Honig
- **Blue Team**: https://www.bleepingcomputer.com/, https://www.crowdstrike.com/

---

## Resumo de Início Rápido

```bash
# Simulação de ransomware
cd ransomware && python3 safe_ransomware_sim.py
# → Opção 1 (criar arquivos) → Opção 2 (criptografar) → Opção 3 (descriptografar)

# Simulação de keylogger
cd keylogger && python3 safe_keylogger_sim.py
# → Opção 1 (iniciar) → Digite teclas de teste → ESC para parar → Opção 2 (ver logs)
```

**Lembre-se**: O objetivo é entender o comportamento do atacante para construir defesas melhores. Sempre pratique em ambientes controlados.
