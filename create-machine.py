#!/bin/python
import sys
import subprocess
from shutil import copy2

#Asks for user input to define variables.
NAME = raw_input("VM Name (Use FQDN): ")
NAME_DISK = NAME + ".qcow2"
MAC = virtinst.util.randomMAC()
RAM = raw_input("RAM [1024]: ")
if RAM == "":
  RAM = 1024
CPU = raw_input("Number of vCPUs [2]: ")
if CPU == "":
  CPU = 2
raw_input("Disk size will be 10GB. Okay to proceed? (Press any button to proceed): ")

#Defines options for customizing image
FILE = " --add /home/kvm/disks/" + NAME_DISK
HOSTNAME = " --hostname " + NAME

COMMAND1 = "echo 'this is a command'"
RUN = " --run-command " + COMMAND1

#Use this option if you'd like to run a script on first boot of machine. 
PATH_TO_SCRIPT = "/home/brian/scripts/virt-setup/first-boot.sh"
BOOTSCRIPT = " --firstboot " + PATH_TO_SCRIPT


#copies the existing template to a file a new directory and gives it a unique name. If the template doesn't exist yet, then you'll need to run the disk-setup script.
copy2("/home/kvm/templates/template.qemu", "/home/kvm/disks/" + NAME_DISK)

#runs virt-customize to edit the image.
subprocess.Popen("virt-sysprep" + FILE + HOSTNAME + RUN + BOOTSCRIPT)
