import subprocess
import json

def load_config():
    """Carga la configuración desde el archivo config.json"""
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config['container_name'], config['site_name']

def rename_fields(fields: dict):
    """
    Recibe un diccionario de campos: {current_name: new_name}
    Ejecuta el comando de renombramiento por cada par.
    """
    # Cargar configuración desde el archivo JSON
    CONTAINER_NAME, SITE_NAME = load_config()

    results = {}
    for current_name, new_name in fields.items():
        command = [
            "docker", "exec", CONTAINER_NAME,
            "bench", "--site", SITE_NAME,
            "execute", "frappe.rename_doc",
            "--args", f'["Custom Field", "{current_name}", "{new_name}"]',
            "--kwargs", '{"force": true}'
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            results[current_name] = ("✅", new_name)
        else:
            results[current_name] = ("❌", result.stderr.strip())

    return results
