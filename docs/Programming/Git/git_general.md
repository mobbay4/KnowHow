# General hints on Git

In this section, useful git commands and workflows should be collected.

## Commands

### Branches

Show branches:

```bash
git branch # to show local branches
git branch # to show local and remote branches
```

Create branches:

```bash
git checkout -b <branch> # creates and switches to <branch>
```

To make it available remotely:

```bash
git push --set-upstream origin <branch>
```

**local:**

```shell
git branch -d <branch>
```

The '-d' option stands for '-delete', and it can be used whenever the branch you want to clean up is completely merged with your upstream branch.

```shell
git branch -D <branch>
```

In this case, the '-D' option stands for '-delete -force',  and it is used when your local branches are not merged with your remote-tracking branches.

**remote**:

remote branches

```shell
git push <remote> --delete <branch>
```

### Merge

To merge another branch in your active branch:

```bash
git merge <branch>
```

Not auto-mergeable files have to be resolved manually.

To get a merge preview, one can use:

```bash
git diff <source_branch> <target_branch>
```

### log

To study the repository history:

```bash
git log
```

There are several parameters one can adjust:

```bash
--author=boy
--graph --oneline --decorate --all # shows reduced git commit history
```

### Undo current chagnes ([Reference][Undo current changes])

This discards local changes to all files permanently:

```bash
Git reset --hard
```

Unstaged but keep changes

```bash
git reset
```

## SSH Agent

One can secure his SSH keys and configure an authentication agent so that you will not have to reenter your passphrase every time you use your SSH keys.
This [tutorial explains how to configure the SSH-Agent].

[tutorial explains how to configure the SSH-Agent]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases#auto-launching-ssh-agent-on-git-for-windows
[Undo current changes]: https://docs.gitlab.com/ee/topics/git/numerous_undo_possibilities_in_git/
