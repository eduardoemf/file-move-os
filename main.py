from src.classes.backup_generator import BackupManager

volume_banco_de_dados = BackupManager(
    source_dir='diretorio_origem', 
    backup_base_dir='diretorio_destino'
    )

volume_banco_de_dados.run_backup()
