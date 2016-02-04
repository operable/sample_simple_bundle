# Sample Simple Command Bundles

The bundles in this repository are examples of enforcing and non-enforcing commands.

Commands:
 enforcing: The netstat command is used as an example to demonstrate enforcing bundles
 unenforcing: The ping command is used as an example to demonstate non-enforcing bundles

**enforcing** bundles refer to whether or not permission to execute the commands in 
the bundle are necessary. If a bundle is enforcing, there **must** be rules and
permissions listed in the `config.json` file as well.


How to Install simple bundle in your instance of Cog.

1. Be sure that you have an instance of Relay installed (See <https://github.com/operable/cog/wiki/Installation-Guide> for more details on how to do this.)
2. Place the corresponding script in a directory of your choosing.
3. Ensure that the permissions on the script are set such that it is executable
4. Change the JSON file to set the command's "executable" path to point to the corresponding script
5. Place the JSON file in Relay's `pending` directory
6. Relay should pick up the bundle and you should see a message that states "Bundle file /path/to/relay/pending/bundle_file has been successfully deployed to /path/to/relay/bundles/bundle_file"
