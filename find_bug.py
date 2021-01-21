#!/usr/bin/env python
# -*- coding:utf-8 -*-

from git import Repo
import base64

repo = Repo(".")
repo.git.checkout('find-bug')
commits = repo.iter_commits('HEAD...1.0')

# brute-force method
for x in reversed(list(commits)):
    repo.head.set_reference(x)
    read_this = repo.tree(x)['home-screen-text.txt'].data_stream.read()
    # reader = repo.config_reader()
    # read_this = open('./exercises/home-screen-text.txt')
    content = base64.b64decode(read_this).decode('ascii')
    if 'jackass' in content:
        print(x.hexsha)	
        break

# binary search method
# newest first
commits = list(commits)
search_length = len(commits)
idx = search_length//2
last_idx = 0
found_at = None

for i in range(0, round(math.log2(search_length))):
    print('idx is:', idx)
    print('last_idx is:', last_idx)
    repo.head.set_reference(commits[idx])
    read_this = repo.tree(commits[idx])['home-screen-text.txt'].data_stream.read()
    # reader = repo.config_reader()
    # read_this = open('./exercises/home-screen-text.txt')
    content = base64.b64decode(read_this).decode('ascii')
    if 'jackass' in content:
        found_at = idx
        print(commits[idx].hexsha)
        if i == 0:
            update = (search_length - idx)//2
        else:
            update = (last_idx - idx)//2
        last_idx = idx
        idx += abs(update)
    else:
        update = (idx - last_idx)//2 
        last_idx = idx
        idx -= abs(update) 

print("The commit where the bug 'jackass' was introduced is:", commits[found_at].hexsha)
