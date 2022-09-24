import configparser
import sys


def read_config(name):
    config_file = "../configFiles/config.txt"
    conf = configparser.RawConfigParser()
    conf.read(config_file)
    return conf.get('base', name)
