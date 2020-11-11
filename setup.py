'''
================================================ 
          VOICEBOOK REPOSITORY                     
================================================ 

repository name: voicebook 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voicebook 
author: Jim Schwoebel 
author contact: js@neurolex.co 
description: a book and repo to get you started programming voice applications in Python - 10 chapters and 200+ scripts. 
license category: opensource 
license: Apache 2.0 license 
organization name: NeuroLex Laboratories, Inc. 
location: Seattle, WA 
website: https://neurolex.ai 
release date: 2018-09-28 

This code (voicebook) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
                LICENSE TERMS                      
================================================ 

Copyright 2018 NeuroLex Laboratories, Inc. 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 

================================================ 
                SERVICE STATEMENT                    
================================================ 

If you are using the code written for a larger project, we are 
happy to consult with you and help you with deployment. Our team 
has >10 world experts in kafka distributed architectures, microservices 
built on top of Node.JS / Python / Docker, and applying machine learning to 
model speech and text data. 

We have helped a wide variety of enterprises - small businesses, 
researchers, enterprises, and/or independent developers. 

If you would like to work with us let us know @ js@neurolex.co. 

================================================ 
                SETUP.PY                  
================================================ 

setup.py

Custom script to install dependencies for Voicebook.

Since I wrote this book in 1.5 months, I may be missing some 
dependencies. If you find something that is missing, please let me
know as an issue @ https://github.com/jim-schwoebel/voicebook/issues
and I can add it here. 

Requires homebrew to be installed on endpoint device
and assumes a MacOS operating system.
'''
# Install dependencies
import os

def pip3_install():
  os.system('pip3 install -r requirements.txt')

def brew_install(modules):
  for i in range(len(modules)):
      os.system('brew install %s'%(modules[i]))
      
# things that need some custom setup 
os.system('sudo pip3 uninstall crypto')
os.system('pip3 uninstall pycryptodome')
os.system('pip3 install --upgrade setuptools')
os.system('pip3 install -U pyobjc')
os.system('brew install heroku/brew/heroku')
os.system('brew cask info google-cloud-sdk')

# mongoDB setup
os.system('brew install mongodb')
os.system('mkdir -p /data/db')
os.system('sudo chmod 777 /data/db')

# install homebrew and pip modules 
brew_modules=['opus','portaudio','sox','nginx', 'kafka', 'kubernetes-cli', 
              'ffmpeg','opus-tools','opus']

brew_install(brew_modules)
pip3_install()
# scikit-learn needs to be version 0.19.1 because some things break in newest versions
os.system('sudo pip3 uninstall scikit-learn')
os.system('pip3 install scikit-learn==0.19.1')

# customize spacy packages 
os.system('python3 -m spacy download en')
os.system("python3 -m spacy download 'en_core_web_sm'")
# download all nltk packages 
import nltk 
nltk.download('all')
