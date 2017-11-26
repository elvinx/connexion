#!/bin/bash

curl --request POST \
  --url http://localhost:8080/predictions \
  --header 'content-type: application/json' \
  --data '[{"text": "Angela Merkel just walked into her fourth term as chancellor of Germany.Her party, the Christian Democrats (CDU), picked up 32.5 percent of the votes in Sunday’s election, according to the first exit polls issued at 6 pm German local time."}]'