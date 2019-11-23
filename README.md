# awsc

Simple aws profile helper utility. This was written mainly to avoid having to manually export `AWS_PROFILE` 
every time I wanted to switch accounts.

## Installation

You might want to run this from your main environment, but who am I to judge. Do it in a venv if that's better for you.

```
$ pip install -U git+ssh://git@github.com/ryanjameslett/awsc.git
```

## Usage

To get a list of available profiles:

```
awsc list
```
Will result in output like this:

```
 [1] * Account-1
 [2]   Account-2
 [3]   Account-3
 [4]   Account-4
```
The * shows the currently active profile.

To set a new profile, run

```
awsc set <profile_number>  # e.g. awsc set 3
```

This will print out the following:

```
Run the following command:
source ./update_profile.sh
```
Because python doesn't have the ability to modify environment variables in the shell
in any lasting way, this generates a script to do it instead. If you know how to make
it so this is automatic, please make a pull request.

So do what it says and run `source ./update_profile.sh`. The script will update the environment variable and delete itself.
