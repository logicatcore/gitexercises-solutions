#!/usr/bin/env python
# -*- coding:utf-8 -*-

from git import Repo
import base64

repo = Repo(".")
repo.git.checkout('find-bug')
commits = repo.iter_commits('HEAD...1.0')
for x in reversed(list(commits)):
    repo.head.set_reference(x)
    read_this = repo.tree(x)['home-screen-text.txt'].data_stream.read()
    # reader = repo.config_reader()
    # read_this = open('./exercises/home-screen-text.txt')
    content = base64.b64decode(read_this).decode('ascii')
    if 'jackass' in content:
        print(x.hexsha)	
        break

