import uuid
from ssh_manager import SSHManager

SERVER_IP = "46.8.113.99"

VLESS_TEMPLATE = (
    "vless://{uuid}@46.8.113.99:443"
    "?encryption=none"
    "&flow=xtls-rprx-vision"
    "&security=reality"
    "&sni=www.cloudflare.com"
    "&fp=chrome"
    "&pbk=AgCoRiPrJsVr5u_BrPsaAdFV1GlDEKKhk1dFUWqYkVI"
    "&sid=6ba85179e30d4fc2"
    "&type=tcp"
    "#VPN0Problem-🇨🇿"
)


def create_vless_client():
    new_uuid = str(uuid.uuid4())

    ssh = SSHManager()
    ssh.connect()

    config = ssh.download_config()

    # добавляем клиента в первый inbound
    config["inbounds"][0]["settings"]["clients"].append({
        "id": new_uuid,
        "flow": "xtls-rprx-vision"
    })

    ssh.upload_config(config)
    ssh.restart_xray()
    ssh.close()

    link = VLESS_TEMPLATE.format(uuid=new_uuid)
    return new_uuid, link