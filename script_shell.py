# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:35:44 2021

@author: LENOVO
"""


### Ce code teste si git est installé et il le fait
## et il clone ton projet sur google cloud

## Le projet est hébergé sur github 
## https://github.com/Kemadjou-Elodie/Deep-Learning-Projet/blob/master/Projet_Test_Reylens.ipynb

url=https://github.com/Kemadjou-Elodie/Deep-Learning-Projet.git


R=`git --version | grep "git version 2.24.1"`; if [ -n "$R" ]; then echo 'pass'; PASS="pass" ; else echo 'fail'; fi

 

if [ "$PASS" != "pass" ];  then

 

sudo yum remove git*
sudo yum -y install https://packages.endpoint.com/rhel/7/os/x86_64/endpoint-repo-1.7-1.x86_64.rpm
yum sudo install git
fi

 

git config --global http.sslVerify false

 

git  clone $url