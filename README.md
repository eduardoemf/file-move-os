# BackupManager

`BackupManager` é uma classe Python que realiza backups de diretórios, registrando logs do processo e excluindo backups antigos conforme um período de retenção especificado.

## Instalação

Para utilizar este script, você precisa ter Python instalado na sua máquina. Além disso, as bibliotecas `os`, `shutil`, `datetime` e `logging` são necessárias. Todas essas bibliotecas são padrões no Python.

## Uso

### Inicialização

```python
from backup_manager import BackupManager

source_dir = '/caminho/do/diretorio/de/origem'
backup_base_dir = '/caminho/do/diretorio/de/backup'
retention_days = 10

backup_manager = BackupManager(source_dir, backup_base_dir, retention_days)
```

## Métodos
**__init__**(self, source_dir, backup_base_dir)
Inicializa a classe com os diretórios de origem e destino do backup.

    Args:
    source_dir (str): O caminho do diretório de origem.
    backup_base_dir (str): O caminho do diretório base onde o backup será armazenado.
    setup_logging(self) -> Configura o logging para o script. Cria logs tanto em um arquivo backup_log.txt quanto no console.
    retention_days (int): O número de dias para manter os backups.

**create_backup_directory**(self, backup_dir_name)
Cria o diretório base do backup se não existir.

    Args:
    backup_dir_name (str): O nome do diretório de backup.
    Returns:
    str: O caminho completo do diretório de backup.
    backup_directory(self)
    Faz o backup de um diretório, adicionando a data ao nome do diretório de backup.

**run_backup(self)**

    Executa todos os métodos necessários para realizar o backup em sequência.
