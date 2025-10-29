from config import settings
import sys
import platform


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)

    with open(settings.allure_results_dir / 'environment.properties', 'w') as file:
        file.write(properties)
        file.write(f'\nos_info={platform.system()}, {platform.release()}\npython_version={sys.version}')
