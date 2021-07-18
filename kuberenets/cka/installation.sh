#!/bin/#!/usr/bin/env bash

#install docker
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install -y wget
sudo wget http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.107-3.el7.noarch.rpm

sudo yum localinstall container-selinux-2.107-3.el7.noarch.rpm

sudo yum install -y docker-ce

# install kubeadm, kubectl, kubelet
sudo cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

# Set SELinux in permissive mode (effectively disabling it)
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes

sudo systemctl enable --now kubelet

mkdir -p $HOME/.kube
sudo cp /etc/kubernetes/admin.conf $HOME/
sudo chown $(id -u):$(id -g) $HOME/admin.conf
sudo export KUBECONFIG=$HOME/admin.conf

sudo systemctl retstart docker
sudo systemctl retstart kubelet

sudo kubeadm init --pod-network-cidr=192.168.0.0/16

sudo kubectl apply -f https://docs.projectcalico.org/v3.8/manifests/calico.yaml

sudo kubectl get pods --all-namespaces
