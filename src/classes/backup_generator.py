import os
import shutil
from datetime import datetime
import logging

class BackupManager:
    
    def __init__(self, source_dir, backup_base_dir):
        """
        Inicializa a classe com os diretórios de origem e destino do backup.

        Args:
            source_dir (str): O caminho do diretório de origem.
            backup_base_dir (str): O caminho do diretório base onde o backup será armazenado.
        """
        self.source_dir = source_dir
        self.backup_base_dir = backup_base_dir
        self.setup_logging()

    def setup_logging(self):
        """
        Configura o logging para o script.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("backup_log.txt", encoding='utf-8'),
                logging.StreamHandler()
            ]
        )

    def create_backup_directory(self, backup_dir_name):
        """
        Cria o diretório base do backup se não existir.

        Args:
            backup_dir_name (str): O nome do diretório de backup.

        Returns:
            str: O caminho completo do diretório de backup.
        """
        backup_dir = os.path.join(self.backup_base_dir, backup_dir_name)
        
        if not os.path.exists(self.backup_base_dir):
            os.makedirs(self.backup_base_dir)
            logging.info(f"Criado diretório base de backup: {self.backup_base_dir}")
        
        return backup_dir

    def backup_directory(self):
        """
        Faz o backup de um diretório adicionando a data ao nome do diretório de backup.
        """
        if not os.path.exists(self.source_dir):
            logging.error(f"O diretório de origem {self.source_dir} não existe.")
            return
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        base_name = os.path.basename(self.source_dir.rstrip(os.sep))
        backup_dir_name = f"{base_name}_backup_{date_str}"
        
        backup_dir = self.create_backup_directory(backup_dir_name)
        
        try:
            shutil.copytree(self.source_dir, backup_dir)
            logging.info(f"Backup realizado com sucesso! Diretório de backup: {backup_dir}")
        except Exception as e:
            logging.error(f"Ocorreu um erro ao copiar o diretório: {e}")

    def run_backup(self):
        """
        Executa todos os métodos necessários para realizar o backup em sequência.
        """
        self.setup_logging()
        self.backup_directory()