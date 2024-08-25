import netmiko

import netmiko.exceptions

connectionConfig = {
    'ip' : '172.20.20.6', 
    'device_type' : 'nokia_srl',
    'username' : 'admin',
    'password' : 'NokiaSrl1!',
}

netmiko_exceptions = (netmiko.exceptions.NetMikoTimeoutException, netmiko.exceptions.NetMikoAuthenticationException,
                      netmiko.exceptions.SSHException)

async def sendCommand(command):
    try:
        connection = netmiko.ConnectHandler(**connectionConfig)
        response = connection.send_command(command)
        connection.disconnect()
        return response
    except netmiko_exceptions as e:
        return f"Exception: {str(e)}"
    

