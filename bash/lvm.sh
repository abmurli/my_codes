yum install -y lvm2*
pvcreate /dev/sdb
pvcreate /dev/sdc

vgcreate -s 32M vg_oem /dev/sdb

vgdisplay vg_oem

"""
--- Volume group ---
  VG Name               vg_oem
  System ID
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  3
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               <39.94 GiB
  PE Size               32.00 MiB
  Total PE              1278
  Alloc PE / Size       1278 / <39.94 GiB
  Free  PE / Size       0 / 0
"""

lvcreate -L 20G -n sdb vg_oem
lvcreate -L 20G -n sdc vg_oem


lvcreate -l PE_size -n sdb vg_oem
mkfs.ext4 /dev/vg_oem/sdb
mount /dev/vg_oem/sdb /opt/apigee
cat /etc/mtab
vi /etc/fstab
mount -av

reattach

vgexport vg_oem
vgimport vg_oem
vgchange -ay vg_oem


fdisk -l
df -h
lsblk
