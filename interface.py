#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import devinfo
import paho.mqtt.client as mqtt


class iMQTT(object):
    def __init__(self, topic2publish, name):
        self.topic2publish = topic2publish
        self.client_name = name + "_client"
        self.clientTx = mqtt.Client(self.client_name)
        self.clientTx.on_connect = self.on_connect
        self.clientTx.on_message = self.on_message
        self.clientTx.on_disconnect = self.on_disconnected
        server_info = devinfo.get_server_config()
        if server_info['user'] is not None:
            self.clientTx.username_pw_set(server_info['user'],
                                          server_info['password'])
        self.clientTx.connect(server_info['host'],
                              server_info['port'])
        self.clientTx.loop_start()
        # self.send_msg()

    def on_connect(self, userdata, flags, rc):
        if rc == 0:
            logging.debug(self.client_name + "MQTT Connection successful !")
        else:
            logging.debug(self.client_name + "MQTT Connection refused !")

    def on_disconnected(self, userdata, flags, rc):
        logging.debug(self.client_name + "MQTT Disconnected !")

    def on_message(self, userdata, msg):
        logging.debug(self.client_name + "MQTT MSG RXD")

    def send_msg(self,msg):
        if self.clientTx.is_connected():
            self.clientTx.publish(self.topic2publish, msg)
            logging.debug(self.client_name + 'msg send '+ msg)
        else:
            logging.debug(self.client_name + 'MQTT Disconnected !')
