import paramiko
import json
import uuid
import io

SERVER_HOST = "46.8.113.99"
SERVER_USER = "vpn"
SERVER_PASSWORD = "privetNikita01"

XRAY_CONFIG_PATH = "/usr/local/etc/xray/config.json"
RESTART_COMMAND = "sudo systemctl restart zeroproblem"


class SSHManager:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(
            hostname=SERVER_HOST,
            username=SERVER_USER,
            password=SERVER_PASSWORD
        )

    def close(self):
        self.client.close()

    def download_config(self):
        sftp = self.client.open_sftp()
        with sftp.open(XRAY_CONFIG_PATH, "r") as f:
            config_data = f.read()
        sftp.close()
        return json.loads(config_data)

    def upload_config(self, config_data):
        sftp = self.client.open_sftp()
        with sftp.open(XRAY_CONFIG_PATH, "w") as f:
            f.write(json.dumps(config_data, indent=4))
        sftp.close()

    def restart_xray(self):
        stdin, stdout, stderr = self.client.exec_command(RESTART_COMMAND)
        stdout.channel.recv_exit_status()