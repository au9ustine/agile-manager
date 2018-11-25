#!/bin/zsh

START_SPRINT_NO=132
END_SPRINT_NO=157

WEEKS=$(python3 -c 'import datetime;f=lambda x:(x%4==0) and (x%100>0) or (x%400==0);lastweek=53 if f(datetime.date.today().year) else 52;print(lastweek)')

if [ `uname -s` = 'Darwin' ]; then
    if [ $(echo "`which ggrep`" | wc -m) -gt 0 ]; then
        GREP_BIN=ggrep
    else
        echo "Please 'brew install grep' first on your mac" # BSD grep works abnormally with '-o' option
        exit 1
    fi
else
    GREP_BIN=grep
fi

for i in {$START_SPRINT_NO..$END_SPRINT_NO}; do
    python3 ./manager.py $i | $GREP_BIN -Eo '[0-9]*' | xargs | awk '{print "TODO in Sprint "$1" ("$3$4"-"$6$7")";}'
done
