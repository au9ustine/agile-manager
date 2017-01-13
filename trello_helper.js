var success = function(successMsg) {
  asyncOutput(successMsg);
};

var error = function(errorMsg) {
  asyncOutput("error: " + errorMsg);
};

// for i in {80..105};do ./mgr $i | grep -Eo '[0-9]*' | xargs | awk '{print "TODO in Sprint "$1" ("$3$4"-"$6$7")"}';done
var names = [
  "TODO in Sprint 80 (0114-0127)",
  "TODO in Sprint 81 (0128-0210)",
  "TODO in Sprint 82 (0211-0224)",
  "TODO in Sprint 83 (0225-0310)",
  "TODO in Sprint 84 (0311-0324)",
  "TODO in Sprint 85 (0325-0407)",
  "TODO in Sprint 86 (0408-0421)",
  "TODO in Sprint 87 (0422-0505)",
  "TODO in Sprint 88 (0506-0519)",
  "TODO in Sprint 89 (0520-0602)",
  "TODO in Sprint 90 (0603-0616)",
  "TODO in Sprint 91 (0617-0630)",
  "TODO in Sprint 92 (0701-0714)",
  "TODO in Sprint 93 (0715-0728)",
  "TODO in Sprint 94 (0729-0811)",
  "TODO in Sprint 95 (0812-0825)",
  "TODO in Sprint 96 (0826-0908)",
  "TODO in Sprint 97 (0909-0922)",
  "TODO in Sprint 98 (0923-1006)",
  "TODO in Sprint 99 (1007-1020)",
  "TODO in Sprint 100 (1021-1103)",
  "TODO in Sprint 101 (1104-1117)",
  "TODO in Sprint 102 (1118-1201)",
  "TODO in Sprint 103 (1202-1215)",
  "TODO in Sprint 104 (1216-1229)",
  "TODO in Sprint 105 (1230-0112)"
];
var newList = {};
for(var i = 0; i < names.length; i++){
  newList = {
    name: names[i], 
    idBoard: "572ea919522f0bb27fb98d37",
    pos: "bottom"
  };
  Trello.post('/lists/', newList, success, error);

}
