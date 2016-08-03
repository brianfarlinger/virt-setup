#!/bin/bash

#run this script on an existing vm to prepare a standard vm template

#copy standard image template to a new location. If this image file is attached to a vm, make sure the vm is shutdown.
cp var/lib/libvirt/images/template-machine.qemu /home/kvm/templates/template.qemu

#use virt-sysprep to prepare the image. Uses default operations settings.
virt-sysprep -a /home/kvm/templates/template.qemu --operations abrt-data, bash-history, crash-data, fs-uuids, kerberos-data, logfiles, lvm-uuids, machine-id, net-hwaddr, yum-uuid
