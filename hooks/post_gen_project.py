from subprocess import call


# Format generated project with Black
call(["pipenv", "install", "--dev"])
call(["pipenv", "run", "black", "."])
