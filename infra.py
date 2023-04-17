import subprocess
import os
import sys

def check_docker_installed():
   try:
      subprocess.check_output(['which', 'docker'])
      return True
   except subprocess.CalledProcessError:
        # If `which docker` command returns non-zero exit status, then Docker is not installed
        return False
def checkDockerinstallation(check):
   if check_docker_installed():
      print("Docker is installed!")
      os.system('echo "docker is already installed"')
      os.system("sudo docker volume create '{}'".format(volume_name))
      os.system("sudo docker network create '{}'".format(network_name))
   else:
      os.system("sudo apt update")
      os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
      os.system("sh get-docker.sh")
      os.system("sudo docker volume create '{}'".format(volume_name))
      os.system("sudo docker network create '{}'".format(network_name))
 # except subprocess.CalledProcessError:
      print("Docker is not installed.")
if __name__ == '__main__':
    check=False
    network_name=sys.argv[1]#'envnw'
    volume_name=sys.argv[2]#'envvol'
    checkDockerinstallation(check)
