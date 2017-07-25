#!/bin/bash
#Author: timo (greycd@gmail.com)
#for tc and iptables to control network flow
. /etc/profile

#run as root
if [ $UID -gt 0 ];then
  echo "please run as root"
  exit 1
fi

#确定默认变量
limit=${limit:-1bps}
choice=${choice:IP}

if [ $# -le 4 ];then
  echo "please input argument"
  exit 1
fi

#get option
while getopts "i:p:l:c:" arg
#选项后面的冒号表示该选项需要参数
do
        case $arg in
             i)
                device=$OPTARG #参数存在$OPTARG中
                ;;
             p)
                port=$OPTARG
                ;;
             l)
                limit=$OPTARG
                ;;
             c)
                choice=$OPTARG
                ;;
             ?)  #当有不认识的选项的时候arg为?
            echo "unkonw argument"
        exit 1
        ;;
        esac
done

#判断tc和iptables2个程序是否存在
test -e /usr/sbin/tc  || yum install iproute -y
test -e /usr/sbin/iptables || yum install iptables -y
#
##
##echo $device
##echo $port
##echo $limit

tc=/usr/sbin/tc
iptables=/usr/sbin/iptables

if [ $choice == "TC" ];then

##创建队列规则添加到eth0上,root表示根规则,设置句柄为1：,htb default 1表示没有进行分类的数据包都走1:1缺省类
  $tc qdisc add dev $device root handle 1: htb default 1
##在父类1:的基础上,创建一个子类1:1,使用令牌桶(htb)队列,保证子类的带宽为1000Mbit(根据实际带宽设置)
  $tc class add dev $device parent 1: classid 1:1 htb rate $limit
fi

if [ $choice == "IP" ];then
  $iptables -F
  $ipatlbes -I INPUT -i $device -p tcp –dport $port  -j DROP
fi

if [[ $choice == "DTC" ]];then
  $tc qdisc del dev $device root 2>/dev/null
fi

if [ $choice == "DIP" ];then
  $iptables -F
fi

