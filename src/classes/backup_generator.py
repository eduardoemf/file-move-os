import os
import shutil
from datetime import datetime, timedelta
import logging

class BackupManager:
    
    def __init__(self, source_dir, backup_base_dir, retention_days):
        """
        Inicializa a classe com os diretórios de origem e destino do backup, 
        e o período de retenção dos backups.

        Args:
            source_dir (str): O caminho do diretório de origem.
            backup_base_dir (str): O caminho do diretório base onde o backup será armazenado.
            retention_days (int): O número de dias para manter os backups.
        """
        self.source_dir = source_dir
        self.backup_base_dir = backup_base_dir
        self.retention_days = retention_days
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


    def delete_old_backups(self):
        """
        Avalia os backups existentes e exclui aqueles que são mais antigos do que 
        o número de dias de retenção especificado.

        Returns:
            bool: True se a exclusão foi realizada com sucesso, False caso contrário.
        """
        now = datetime.now()
        cutoff_date = now - timedelta(days=self.retention_days)
        backup_created_today = False

        for folder_name in os.listdir(self.backup_base_dir):
            folder_path = os.path.join(self.backup_base_dir, folder_name)
            if os.path.isdir(folder_path):
                try:
                    folder_date_str = folder_name.split('_backup_')[-1]
                    folder_date = datetime.strptime(folder_date_str, "%Y-%m-%d")
                    if folder_date >= now.replace(hour=0, minute=0, second=0, microsecond=0):
                        backup_created_today = True
                    if folder_date < cutoff_date:
                        shutil.rmtree(folder_path)
                        logging.info(f"Backup antigo excluído: {folder_path}")
                except Exception as e:
                    logging.error(f"Erro ao avaliar ou excluir o diretório {folder_path}: {e}")
                    return False
        
        if not backup_created_today:
            logging.error("O backup de hoje não foi criado com sucesso. A exclusão de backups antigos foi abortada.")
            return False
        
        return True

    def run_backup(self):
        """
        Executa todos os métodos necessários para realizar o backup em sequência.
        """
        self.setup_logging()
        if self.backup_directory():
            self.delete_old_backups()