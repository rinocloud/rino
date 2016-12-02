# Rinocloud CLI toolkit

CLI tool to save data-science notebooks on Rinocloud.

(General file push/pull coming soon...)

## Installation

```
pip install rino
 ```

## Getting started

First you will want to login to Rinocloud so that you can push data.

```
rino login
 ```

The, in your target directory, initialize a repository

```
rino init
 ```

This will create a `rino.json` file.
Then set the Rinocloud folder you want to push notebooks to.

```
rino remote set data/notebooks
 ```

Then push a new notebook (can be any filetype)

```
rino notebook push some_notebook.ipynb
 ```

If a git repo exists, rino will automatically gather the remote origin, the
branch and the current commit hash. If the repo is not clean, the push will be
rejected unless you add the `-f`, or `--force` flag. This is so that each
version of the notebook will have a solid codebase to reference at all points in
the future.

It adds all this to a `git` metadata field of the notebook on Rinocloud.

When you've edited your notebook, and you want it updated:

```
rino notebook update some_notebook.ipynb
 ```

Same rules apply as push with respect to git.

You can fetch a notebooks from Rinocloud with

```
rino notebook fetch rinocloud/path/notebook.md
```

To see the git information of an existing local notebook just type:

```
rino git show notebook.md
```
