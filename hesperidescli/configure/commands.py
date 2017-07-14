import base64
import click
from hesperidescli.configure.reader import ConfigFileReader
from hesperidescli.configure.writer import ConfigFileWriter


@click.group('configure')
def command():
    pass


@click.command('set')
@click.option('--username', prompt=True, hide_input=False, confirmation_prompt=False, default='')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False, default='')
@click.option('--hesperides_endpoint', prompt=True, hide_input=False, confirmation_prompt=False, default='hesperides')
@click.option('--hesperides_endpoint_protocol', prompt=True, hide_input=False, confirmation_prompt=False,
              default='https')
@click.option('--hesperides_endpoint_port', prompt=True, hide_input=False, confirmation_prompt=False,
              default='80')
@click.option('--format', prompt=False, hide_input=False, confirmation_prompt=False,
              default='json')
def set_config(username, password, hesperides_endpoint, hesperides_endpoint_protocol, hesperides_endpoint_port, format):
    click.echo('Configure hesperides')
    print('username: ' + username)
    print('password: **********')
    basic_auth = base64.b64encode(str.encode('%s:%s' % (username, password))).decode('UTF-8')
    print('basic_auth: ' + basic_auth)
    print('hesperides_endpoint: ' + hesperides_endpoint)
    print('hesperides_endpoint_protocol: ' + hesperides_endpoint_protocol)
    print('format: ' + format)

    config = {'endpoint': hesperides_endpoint, 'protocol': hesperides_endpoint_protocol,
              'port': hesperides_endpoint_port, 'format': format}
    credentials = {'username': username, 'auth': basic_auth}

    writer = ConfigFileWriter()
    writer.update_config(config)
    writer.update_credentials(credentials)


@click.command('list')
def list_config():
    config_reader = ConfigFileReader()
    credentials_reader = ConfigFileReader()
    config = config_reader.get_config()
    credentials = credentials_reader.get_credentials()
    print('Config')
    print('======')
    for key in config:
        print(key + ' = ' + config[key])
    print('')
    print('Credentials')
    print('===========')
    for key in credentials:
        print(key + ' = ' + credentials[key])


def get_config(key):
    reader = ConfigFileReader()
    config = reader.get_config()
    config = reader.get_credentials()
    return config[key]


command.add_command(set_config)
command.add_command(list_config)
