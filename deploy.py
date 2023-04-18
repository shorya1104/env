import subprocess
import sys
import os
import threading
def is_mysql_container_running(mysql_container):
   try:
      docker_ps_output=subprocess.check_output(['docker', 'ps'])
      if mysql_container in str(docker_ps_output):
         return True
      else:
         return False
   except subprocess.CalledProcessError:
        return False
   
def is_container_running(container_name):
    try:
        docker_ps_output = subprocess.check_output(['docker', 'ps'])
        if container_name in str(docker_ps_output):
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False
def mysqlContainerrun(mysql_container,mysql_image,network_name,volume_name,mysql_pass,sqlFilePath):
    try:
        is_mysql_container_running(mysql_container)
        if is_mysql_container_running(mysql_container):
            print("mysql container running")
        else:
            os.system("sudo docker container run --name '{}' -p3306:3306 --network '{}' --mount type=volume,source='{}',target=/var/lib/mysql -e MYSQL_ROOT_PASSWORD='{}' -d '{}'".format(mysql_container,network_name,volume_name,mysql_pass,mysql_image))
            a=os.path.abspath('{}').format(sqlFilePath)
            # print(a)
            os.system("echo 'mysql running'")
            print("copying sql file in db")
            os.system("sudo docker cp '{}' '{}':/".format(a,mysql_container))
    except Exception as e:
        print(e)
def deployapp(container_name,image_name):
    try:
        threading.Thread(target=mysqlContainerrun(mysql_container,mysql_image,network_name,volume_name,mysql_pass,sqlFilePath)).start()
        is_container_running(container_name)
        if is_container_running(container_name):
            print("container running")
            print(container_name,"hello")
            os.system("echo 'container runnig kill'")
            os.system("sudo docker container stop '{}'".format(container_name))
            os.system("sudo docker container remove '{}'".format(container_name))
            os.system("sudo docker image remove '{}'".format(image_name))
            os.system("sudo docker build -t '{}' .".format(image_name))
            os.system("sudo docker container run -d --name '{}' --restart unless-stopped --network '{}' -p3000:3000 '{}'".format(container_name,network_name,image_name)) 
            os.system("sudo python3 Feb9Env.py")
        else:
            print(container_name,"hello1")
            os.system("echo 'new image'")
            os.system("sudo docker build -t '{}' .".format(image_name))
            os.system("sudo docker container run -d --name '{}' --restart unless-stopped --network '{}' -p3000:3000 '{}'".format(container_name,network_name,image_name)) 
            # os.system("sudo python3 Feb9Env.py")
    except Exception as e:
        print(e)
if __name__== '__main__':
    container_name=sys.argv[1]#"env"
    image_name=sys.argv[2]#'ec2/env:1.0'
    mysql_container=sys.argv[3]#'envdb'
    mysql_image=sys.argv[4]#'mysql/mysql-server:8.0.25'
    network_name=sys.argv[5]#'envnw'
    volume_name=sys.argv[6]#'envvol'
    mysql_pass=sys.argv[7]#'shorya@123#'
    sqlFilePath=sys.argv[8]#'/home/shorya/other/env/envschema.sql'
    deployapp(container_name,image_name)
