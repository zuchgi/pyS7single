#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import socket
import logging

# 获取用户设置
setting = json.load(open("./config.json", encoding='utf-8'))


def get_time_config():
    return setting['time']


def get_server_config():
    return setting['server']


def get_desk_number():
    def get_host_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((get_server_config()["host"], get_server_config()["port"]))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip
    try:
        slave_ip = get_host_ip()
        slave_id = slave_ip.split('.')[2]
    except Exception as e:
        slave_id = 255
        logging.error("Can not find salve id which ip is %s!" % slave_ip)
    return slave_id


def get_plc_ip(desk_num):
    return "10.35.121."+str(100+int(desk_num))
