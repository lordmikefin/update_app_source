
Update app_source list
======================

( Guide is under construction :)

This project is part of LordMike's Automatic Setup Bot for * projects.

This will update 'app_source.xml' file in 'app_source' project.


Get this project:

.. code-block:: bash

 git clone git@github.com:lordmikefin/update_app_source.git
 
 cd update_app_source/
 
 git submodule init
 git submodule update
 
 cd app_source
 
 git checkout master
 git remote -v
 git remote set-url origin git@github.com:lordmikefin/app_source.git
 
 cd ../app_source_handler
 git checkout master
 git remote -v
 git remote set-url origin git@github.com:lordmikefin/app_source_handler.git
 
 cd ../LMToyBoxPython
 git checkout master
 git remote -v
 git remote set-url origin git@github.com:lordmikefin/LMToyBoxPython.git


