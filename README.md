# Sample Simple Command Bundles

The bundles in this repository are examples of enforcing and non-enforcing commands.

###Simple Commands:
1. **netstat**: The netstat command is used as an example to demonstrate enforcing bundles
2. **ping**: The ping command is used as an example to demonstate non-enforcing bundles

###Enforcing vs Unenforcing
1. **enforcing** bundles refer to whether or not permission to execute the commands in 
the bundle are necessary. If a bundle is enforcing, there **must** be rules and
permissions listed in the `config.yaml` file as well. 
2. **unenforcing** bundles do not need rules or permissions listed in the `config.yaml` file.


###How to Install simple bundle in your instance of Cog.

1. Be sure that you have an instance of Relay installed (See <http://docs.operable.io/docs/installation> for more details on how to do this.)
2. Place the corresponding script in a directory of your choosing.
3. Ensure that the permissions on the script are set such that it is executable
4. Change the YAML file to set the command's "executable" path to point to the corresponding script
5. Place the YAML file in Relay's `pending` directory
6. Relay should pick up the bundle and you should see a message in the log that states "Bundle file /path/to/relay/pending/bundle_file has been successfully deployed to /path/to/relay/bundles/bundle_file"
