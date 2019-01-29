import os
import subprocess
import csv


class SafariProxy():

    def __init__(self, host, port):
        print ('loaded accounts')
        self.host = host
        self.port = port

    def get_active_networks(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cwd = os.getcwd()
        generated_command = '. %s/qa/utilities/oauth/networkservice.sh' % cwd
        # process = subprocess.Popen(
        #     generated_command,
        #     stderr=subprocess.STDOUT,
        #     # stdout=subprocess.PIPE,
        #     shell=True
        # )
        # stdout, stderr = process.communicate()
        # process.wait()
        output = subprocess.check_output(
            generated_command,
            stderr=subprocess.STDOUT,
            shell=True
        ).splitlines()
        services = []
        for row in output:
            row = row.decode("utf-8").replace(' ', '\ ')
            services.append(row)
        return services


    def web_proxy_on(self, network_name, host_url, port):
        generated_command = 'networksetup setwebproxy %s %s %s' % (
                network_name,
                host_url,
                port
        )
        print(generated_command)
        process = subprocess.Popen(
            generated_command,
            stderr=subprocess.STDOUT,
            shell=True
        )
        process.wait()

    def secure_web_proxy_on(self, network_name, host_url, port):
        generated_command = 'networksetup setsecurewebproxy %s %s %s' % (
                network_name,
                host_url,
                port
        )
        print(generated_command)
        process = subprocess.Popen(
            generated_command,
            stderr=subprocess.STDOUT,
            shell=True
        )
        process.wait()


    def web_proxy_off(self, network_name):
        generated_command = 'networksetup setwebproxystate %s off' % (
            network_name
        )
        process = subprocess.Popen(
            generated_command,
            stderr=subprocess.STDOUT,
            shell=True
        )
        process.wait()


    def secure_web_proxy_off(self, network_name):
        generated_command = 'networksetup setsecurewebproxystate %s off' % (
            network_name
        )
        process = subprocess.Popen(
            generated_command,
            stderr=subprocess.STDOUT,
            shell=True
        )
        process.wait()


    def on(self):
        networks = self.get_active_networks()
        for network in networks:
            print('Enabling proxy for %s' % network)
            self.web_proxy_on(network, self.host, self.port)
            self.secure_web_proxy_on(network, self.host, self.port)


    def off(self):
        # generated_command = 'networksetup setwebproxystate Wi-Fi off &&' \
        # 'networksetup setwebproxystate Ethernet off &&' \
        # 'networksetup setsecurewebproxystate Wi-Fi off &&' \
        # 'networksetup setsecurewebproxystate Ethernet off' % (
        #     self.host_url,
        #     self.host_url,
        #     self.host_url,
        #     self.host_url,
        # )
        networks = self.get_active_networks()
        for network in networks:
            print('Enabling proxy for %s' % network)
            self.web_proxy_off(network, self.host, self.port)
            self.secure_web_proxy_off(network, self.host, self.port)
