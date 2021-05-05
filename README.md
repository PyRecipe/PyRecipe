# PyRecipe

## How to contribute
1) Pull the latest changes with `git pull`.
2) Pick a issue to work (in this case the issue should be attachted to you).
3) Create a branch and name it like that: pyr_issueCode (ex: pyr_1 for the Issue Code 1) and pyr stands for "PyRecipe".
4) Start working on the issue.
5) Write at least 1 test for your issue and make sure all the tests are working (including older tests).
6) Rebase your commits to master branch to keep our history tidy.
7) After finishing the issue, create a pull request and pick the reviewer (__!! we will decide how to do that !!__).
8) If your pull request is confirmed by your reviewer, it'll be merged with main branch.
9) Cycle this steps again and again until the first version is released.

### Code submission policy
- Choose expressive variable, function and class names. Make it as obvious as possible what the code is doing.
- Split your changes into separate, atomic commits.
- Squash all your small "fix" commits in to their suitable parent commit.
- The first line of the commit message should have the format "Category: Brief description of what's being changed". The "category" can be a subdirectory, but also something like function or class name.
- Do not touch anything outside the stated scope of the PR.
- Do not use words like "refactor" or "fix" to avoid explaining what's being changed.

## Useful git commands

### Pulling latest changes

`git pull`

### Creating new branch
To create a new branch and switch to it at the same time

`git checkout -b branch_name`

To just create a new branch

`git branch branch_name`

### Checkout existing branch

`git checkout branch_name`

### How to create a new commit
First you have to stage the changes you want to add into commit

`git add file_name`

To stage all the unstaged files:

`git add .`

To commit your staged files:

`git commit -m "Your commit title" -m "Your commit description"`
