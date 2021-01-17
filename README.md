# What is this repo about?

This repo is my attempt at solving the 23 exercies from https://gitexercises.fracz.com/. While some of the solutions do match exactly with the solutions shown after one successfully solves the exercies, the following collection of solutions are bit detailed in their descriptions along with some links pointing to resources which I found to be helpful in learning and solving the exercises.

Exercise 23 is the most interesting one and is also one of the solution I have spent some time working with `gitpython` in developing an alternate method to find bug in contrast to the `git bisect` solution presented on main website.

# Solutions

## Exercise 1: master
```shell
$> git start
$> git verify
```

## Exercise 2: commit-one-file 
```shell
$> git add A.txt
# or 
$> git add B.txt
$> git commit -m "add one file"
$> git verify 
```

## Exercise 3: commit-one-file-staged
```shell
$> git reset HEAD A.txt
# or
$> git reset HEAD B.txt
$> git commit -m "destage one file"
$> git verify
```

## Exercise 4: ignore-them
```shell
$> nano .gitignore
```
```text
*.exe
*.o
*.jar
libraries/
```
```shell
$> git add .
$> git commit -m "commit useful files"
$> git verify
```

## Exercise 5: chase-branch
```shell
$> git checkout chase-branch
$> git merge escaped
$> git verify
```

## Exercise 6: merge-conflict
```shell
$> git checkout merge-conflict
$> git merge another-piece-of-work
$> nano equation.txt
```
```text
2 + 3 = 5
```
```shell
$> git add equation.txt
$> git commit -m "merge and resolve"
$> git verify
```

## Exercise 7: save-your-work
To learn about stashing and cleaning https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning
```shell
$> git stash
# or
$> git stash push
$> nano bug.txt # in the text editor delete the bud line
$> git commit -am "remove bug"
$> git stash apply
# or
$> git stash apply stash@{0}
$> nano bug.txt # in the text editor add the line "Finally, finished it!" to the end
$> git commit -am "finish"
$> git verify
```

## Exercise 8: change-branch-history
To learn about git rebase https://git-scm.com/docs/git-rebase
```shell
$> git checkout change-branch-history
$> git rebase hot-bugfix
$> git verify
```

## Exercise 9: remove-ignored
Solution and explanation https://stackoverflow.com/questions/1274057/how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore
```shell
$> git rm --cached ignored.txt
$> git commit -am "untrack ignored.txt"
$> git verify
```

## Exercise 10: case-sensitive-filename
```shell
$> git reset HEAD^
$> mv File.txt file.txt
$> git add file.txt
$> git commit -m "lowercase filename"
$> git verify
```

## Exercise 11: fix-typo
Note: **--amend** replaces the  tip of the current branch by creating a new commit.
```shell
# fix typo in the file
$> git commit -a --amend
# fix the typo in commit message
$> git verify
```

## Exercise 12: forge-date (most useless exercise, but shows that git is not a monolith)
```shell
$> git commit --amend --no-edit --date="1987-08-03"
```

## Exercise 13: fix-old-typo
```shell
$> git rebase -i HEAD^^
# change "pick" to "edit" where the typo is in the commit message
# fix the typo in the file
$> git add file.txt
$> git rebase --continue
# fix the rebase conflict
$> git add file.txt
$> git reabse --continue
$> git verify
```

## Exercise 14: commit-lost
```shell
$> git reflog
$> git reset --hard HEAD@{1}
$> git verify
```

## Exercise 15: split-commit
```shell
$> git reset HEAD^
$> git add first.txt
$> git commit -m "First.txt"
$> git add second.txt
$> git commit -m "Second.txt"
$> git verify
```

## Exercise 16: too-many-commits
```shell
$> git rebase -i HEAD~4
# replace "pick" with "squash" for the commit with the message "Crap, I have forgotten to add this line." 
# leave a commit message same as the one with which the marked commit is getting squashed with i.e.,
# "Add file.txt"
$> git verify
```

## Exercise 17: executable
Under the hood details https://stackoverflow.com/questions/40978921/how-to-add-chmod-permissions-to-file-in-git
```shell
$> git update-index --chmod=+x script.sh
$> git commit -m "make executable"
$> git verify
```

## Exercise 18: commit-parts
```shell
$> git add --patch file.txt
# split the hunks with 's'
# Stage this hunk [y,n,q,a,d,/,j,J,g,s,e,?]?
# 
# Here is a description of each option:
# 
#     y stage this hunk for the next commit
#     n do not stage this hunk for the next commit
#     q quit; do not stage this hunk or any of the remaining hunks
#     a stage this hunk and all later hunks in the file
#     d do not stage this hunk or any of the later hunks in the file
#     g select a hunk to go to
#     / search for a hunk matching the given regex
#     j leave this hunk undecided, see next undecided hunk
#     J leave this hunk undecided, see next hunk
#     k leave this hunk undecided, see previous undecided hunk
#     K leave this hunk undecided, see previous hunk
#     s split the current hunk into smaller hunks
#     e manually edit the current hunk
#     ? print hunk help

# select each hunk with 'y' or 'n'
$> git commit -m "task 1 related"
$> git commit -am "rest of the content"
$> git verify
```

## Exercise 19: pick-your-features
```shell
# get an idea of the logs currently and know the SHA-1's needed
$> git log --oneline --decorate --graph --all -8
$> git checkout pick-your-features

$> git cherry-pick feature-a 
# or
$> git cherry pick SHA-1 of feature-a commit

$> git cherry-pick feature-b 
# or
$> git cherry pick SHA-1 of feature-b commit

$> git merge --squash feature-c
# resolve conflict
$> git commit -am "Complete Feature C"
$> git verify
```

## Exercise 20: reabse-complex
Explanation from git-book https://git-scm.com/book/en/v2/Git-Branching-Rebasing
```shell
$> git rebase --onto your-master issue-555 rebase-complex 
# This basically says, “Take the rebase-complex branch, figure out the patches since it diverged from the issue-555 branch, 
# and replay these patches in the rebase-complex branch as if it was based directly off the your-master branch instead.” 
$> git verify
```

## Exercise 21: invalid-order
```shell
$> git rebase -i HEAD~4
# reorder the commit messages as needed
$> git verify
```

## Exercise 22: find-swearwords
```shell
$> git log -S shit
# make a note of the commits where a word "shit" was introduced
$> git rebase -i HEAD~105
# replace 'pick' with 'edit' for those commits

# check which files were modified
$> git log -p -1
# replace 'shit' with 'flower' in list.txt
$> git add list.txt
$> git commit --amend
$> git rebase --continue

# check which files were modified
$> git log -p -1
# replace 'shit' with 'flower' in words.txt
$> git add words.txt
$> git commit --amend
$> git rebase --continue

# check which files were modified
$> git log -p -1
# replace 'shit' with 'flower' in words.txt
$> git add words.txt
$> git commit --amend
$> git rebase --continue

$> git verify
```

## Exercise 23: find-bug
1. First method using `git bisect`
```shell
$> git checkout find-bug
$> git bisect start
$> git bisect bad
$> git bisect good 1.0
# the grep documentation for -v flag doesn't make sense with what the author fracz mentioned and also
# I couldn't see the binary output of '1' or '0' as given in the hints
$> git bisect run sh -c "openssl enc -base64 -A -d < home-screen-text.txt | grep -v jackass"
$> git push origin 4d2725ac4c874dbb207770001def27aed48e9ddb:find-bug
```
2. Second method using `gitpython`
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from git import Repo
import base64

# create a repo object to query
repo = Repo("./exercises/")
# switch to the required branch
repo.git.checkout('find-bug')
# get all commits between HEAD and tag 1.0
commits = repo.iter_commits('HEAD...1.0')
# iterate through the commits one-by-one from oldest to the newest and break when
# the word 'jackass' got introduced
for x in reversed(list(commits)):
    # move the head to the commit 'x'
    repo.head.set_reference(x)
    # get a tree object and query the blog based on the file name and read the content from it's data stream
    read_this = repo.tree(x)['home-screen-text.txt'].data_stream.read()
    
    # reader = repo.config_reader()
    # read_this = open('./exercises/home-screen-text.txt')
    
    # decode the base64 bytes
    content = base64.b64decode(read_this).decode('ascii')
    # check if 'jackass' is present in the file, if yes, print the SHA-1 and exit
    if 'jackass' in content:
        print(x.hexsha)	
        break
```

