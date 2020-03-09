'''
Created on 9 Mar 2020

@author: lordmike
'''
import update_app_source

if __name__ == '__main__':
    print(update_app_source.__revision__)
    source_file = './app_source/app_source.xml'
    update_app_source.source.create_sample(source_file)
    update_app_source.source.parse(source_file)
