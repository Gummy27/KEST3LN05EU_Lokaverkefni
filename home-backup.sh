#! /bin/bash

#
# Home Directory Backup Script
#

for filename in /home/*; do 
    name=${filename:6};
    mkdir -p /media/Backup/$name/ && tar - cJpf /media/backup/$name/home-backup/-`date +%d-%m-%Y`.tar.xz /home/$name/{Documents,Downloads,Pictures,Music};
done