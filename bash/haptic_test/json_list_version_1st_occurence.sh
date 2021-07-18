cat test.json | jq '[.[] | select(.version|test("[0-9].[0-9].[0-9]"))][0] | .version'
