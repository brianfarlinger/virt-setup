#!/bin/bash

#run this script on an existing vm to prepare a standard vm template

#shutdown the template vm
virsh shutdown template-machine

#copy standard image template to a new location. If this image file is attached to a vm, make sure the vm is shutdown.
cp var/lib/libvirt/images/template-machine.qcow2 /home/kvm/templates/template.qcow2

#use virt-sysprep to prepare the image. Uses default operations settings.
virt-sysprep -a /home/kvm/templates/template.qcow2
