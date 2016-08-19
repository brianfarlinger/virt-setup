#!/bin/python
import sys
import subprocess
from shutil import copy2
import random

def randomMAC():
  mac = [ 0x00, 0x16, 0x3e,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
  return ':'.join(map(lambda x: "%02x" % x, mac))


def customize_image():
  #Defines options for customizing image
  file_path = " -a " + FILEPATH
  host_name = " --hostname " + NAME
  subprocess.call("virt-sysprep" + file_path + host_name + BOOT_SCRIPT, shell=True)

def create_vm():
  name_vm = " -n " + NAME
  cpu_vm = " -r " + RAM + " --cpu host --vcpus=" + CPU
  os_vm = " --os-variant=rhel7"
  disk_vm = " --disk " + FILEPATH
  network_vm = " --network bridge=br1,mac=" + MAC
  nographics = " --nographics"
  debug = " --debug"
  autostart = " --autostart"
  disk_import = " --import"
  subprocess.call("virt-install" + name_vm + cpu_vm + os_vm + disk_vm + network_vm + nographics + debug + autostart + disk_import, shell=True)

#Asks for user input to define variables.
NAME = raw_input("VM Name (Use FQDN): ")
NAME_DISK = NAME + ".qcow2"
MAC = randomMAC()
RAM = str(raw_input("RAM [1024]: "))
if RAM == "":
  RAM = '1024'
CPU = str(raw_input("Number of vCPUs [2]: "))
if CPU == "":
  CPU = '2'
raw_input("Disk size will be 10GB. Okay to proceed? (Press any button to proceed): ")

#Defines options for customizing image
FILEPATH = "/home/kvm/disks/" + NAME_DISK
HOSTNAME = " --hostname " + NAME

COMMAND1 = "echo 'this is a command'"
RUN = " --run-command " + COMMAND1

#Use this option if you'd like to run a script on first boot of machine.
PATH_TO_SCRIPT = "/home/brian/scripts/virt-tools/first-boot.sh"
BOOT_SCRIPT = " --firstboot " + PATH_TO_SCRIPT


#copies the existing template to a file a new directory and gives it a unique name. If the template doesn't exist yet, then you'll need to run the disk-setup script.
print 'Now copying the template file. Please wait..'
copy2("/home/kvm/templates/template.qcow2", FILEPATH)

#runs virt-customize to edit the image.
print 'Customizing template image. Please wait'
customize_image()

#runs virt-install
print 'Building VM'
create_vm()
