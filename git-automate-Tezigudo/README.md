Create a "script" of Git commands and shell commands that
someone can run in shell window (terminal) that will transform 
the starting repository to the final configuration.  

The script should:

1. use git commands to move and rename files as needed
2. delete excess files using git commands
3. commit the changes it makes
4. list all the files in the repository for the current revision

The script should be named `update.sh`.

You can run it in a bash, git-bash, or zsh shell by typing 
the shell name (e.g. `bash`) and then the scrpt name:
```
bash update.sh
```

The only operating system commands you *might* need are:
- `mkdir dirname` create a directory
- `rmdir dirname` remove a directory (must be empty)

But you shouldn't need `rmdir` (git can do that).

Final configuration of your repository should be:
```
README.md   (rename this file)
main.py     (rename a file)
app/start.py
app/finish.py
```

### What to Submit

Commit your final repository, including the `update.sh` file to Git.

### How to Test

Make *another* clone of the starter code (the initial commit in your repo
on Github), copy your update.sh to this new clone, and run it!

It should transfer the new clone into the final configuration
and then list the files.
