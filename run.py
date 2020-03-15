'''
Created on 9 Mar 2020

@author: lordmike
'''
import json
import update_app_source

if __name__ == '__main__':
    print(update_app_source.__revision__)
    source_file = './app_source/app_source.xml'
    # TODO: use 'update_app_source' project to create the source file
    # NOTE: for now testing with the sample
    update_app_source.source.create_sample(source_file)
    update_app_source.source.parse(source_file)
    print('APPS: ' + json.dumps(update_app_source.source.APPS,
                                 sort_keys=True, indent=2))
