import os
import shutil
from datetime import datetime
import logging

def setup_logging():
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

def create_backup_directory(backup_base_dir, backup_dir_name):
    """
    Cria o diretório base do backup se não existir.

    Args:
        backup_base_dir (str): O caminho do diretório base onde o backup será armazenado.
        backup_dir_name (str): O nome do diretório de backup.

    Returns:
        str: O caminho completo do diretório de backup.
    """
    backup_dir = os.path.join(backup_base_dir, backup_dir_name)
    
    if not os.path.exists(backup_base_dir):
        os.makedirs(backup_base_dir)
        logging.info(f"Criado diretório base de backup: {backup_base_dir}")
    
    return backup_dir

def backup_directory(source_dir, backup_base_dir):
    """
    Faz o backup de um diretório adicionando a data ao nome do diretório de backup.

    Args:
        source_dir (str): O caminho do diretório de origem.
        backup_base_dir (str): O caminho do diretório base onde o backup será armazenado.
    """
    if not os.path.exists(source_dir):
        logging.error(f"O diretório de origem {source_dir} não existe.")
        return
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    base_name = os.path.basename(source_dir.rstrip(os.sep))
    backup_dir_name = f"{base_name}_backup_{date_str}"
    
    backup_dir = create_backup_directory(backup_base_dir, backup_dir_name)
    
    try:
        shutil.copytree(source_dir, backup_dir)
        logging.info(f"Backup realizado com sucesso! Diretório de backup: {backup_dir}")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao copiar o diretório: {e}")

def main():
    """
    Função principal que define os diretórios de origem e destino e chama a função de backup.
    """
    setup_logging()
    source_directory = "C:/Users/eduar/Documents/GitHub Eduardo/webapp-VL-Django/vlgestao/database_mysql"
    backup_directory_base = "D:/eduar/Documents/teste_backup_vl_db"
    backup_directory(source_directory, backup_directory_base)

if __name__ == "__main__":
    main()
