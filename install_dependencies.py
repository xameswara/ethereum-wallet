# install_dependencies.py
import subprocess

dependencies = ['web3', 'eth-utils']
subprocess.check_call(['pip', 'install'] + dependencies)
