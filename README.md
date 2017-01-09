Script to notify updates of your favaorite teachers' lessons in DMM Eikaiwa through Slack.
To use this, you have to set your configuration in lib/Config.py like following.

```
slackChannel = "slack-channel-name"
slackAccessToken = "slack-access-token"

teachers = [
	{
		"id" : "teacher-id",	
		"name" : "teacher-name",
	},
	{
		"id" : "teacher-id",	
		"name" : "teacher-name",
	},
]
```

Then, you can get notifications with the following command.

```
sh PATH_TO_HERE/script/update.sh
```
