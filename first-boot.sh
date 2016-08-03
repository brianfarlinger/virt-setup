#!/bin/bash

#Example of a firstboot script. This script will join the machine to a freeipa domain
ipa-client-install --server=freeipa.lilac.red --domain=lilac.red --mkhomedir --hostname=$hostname --principal=join --password=MQIZE10ruI85tVkWaJI5 --unattended
