'''
Created on 9 Mar 2020

@author: lordmike
'''
import json
import update_app_source
import logging
import sys

logger = update_app_source.logger

def conf_root_logger():
    # Default log level.
    logging.basicConfig(level=logging.DEBUG)

def conf_setup_apps_logger():
    logger_conf = logger
    logger_conf.addHandler(create_hand_stdout())
    logger_conf.addHandler(create_hand_stderr())

def create_hand_stdout():
    hand_stdout = logging.StreamHandler(stream=sys.stdout)
    hand_stdout.setLevel(logging.DEBUG)
    hand_stdout.setFormatter(create_formatter())
    return hand_stdout

def create_formatter():
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    #formatter = logging.Formatter('%(name)-10s - %(levelname)-4s: %(message)s')
    f_str = '[%(name)-10s] %(levelname)-4s: %(message)s'
    # TODO: parameterize: show file/line
    f_str += ' [%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(f_str)
    return formatter

def create_hand_stderr():
    hand_stderr = logging.StreamHandler(stream=sys.stderr)
    hand_stderr.setLevel(logging.ERROR)
    #hand_stderr.setFormatter(create_formatter())
    f_str = '[%(name)-10s] %(levelname)-4s: %(message)s [%(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(f_str)
    hand_stderr.setFormatter(formatter)
    return hand_stderr

if __name__ == '__main__':
    conf_root_logger()
    conf_setup_apps_logger()
    #print(update_app_source.__revision__)
    logger.info(update_app_source.__revision__)
    source_file = './app_source/app_source.xml'
    # TODO: use 'update_app_source' project to create the source file
    # NOTE: for now testing with the sample
    update_app_source.source.create_sample(source_file)
    update_app_source.source.parse(source_file)
    json_dump = json.dumps(update_app_source.source.APPS, sort_keys=True, indent=2)
    #print('APPS: ' + json_dump)
    logger.info('APPS: ' + json_dump)
