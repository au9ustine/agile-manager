#!/bin/zsh

START_SPRINT_NO=132
END_SPRINT_NO=157

for i in {$START_SPRINT_NO..$END_SPRINT_NO}; do ./mgr-dev $i | grep -Eo '[0-9]*' | xargs | awk '{print "TODO in Sprint "$1" ("$3$4"-"$6$7")";}';done
