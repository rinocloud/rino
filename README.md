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

This will create some config files in a hidden `.rino` folder.

Then set the remote directory on Rinocloud that you want to push files toolkit

```
rino remote set data/notebooks
```

Then push a new notebook (can be any filetype)

```
rino notebook push some_notebook.ipynb
```

When you've edited your notebook, and you want it updated:

```
rino notebook update some_notebook.ipynb
```

You can fetch a notebooks from Rinocloud with

```
rino notebook fetch rinocloud/path/notebook.md
```

## Hooks

You can also build a pre-push hook that will attach new metadata to the file,
or reject the push if some conditions are not met.
