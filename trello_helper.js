var success = function(successMsg) {
  asyncOutput(successMsg);
};

var error = function(errorMsg) {
  asyncOutput("error: " + errorMsg);
};

// for i in {80..105};do ./mgr $i | grep -Eo '[0-9]*' | xargs | awk '{print "TODO in Sprint "$1" ("$3$4"-"$6$7")"}';done

// ---- 2017 ----
// var names = [
//   "TODO in Sprint 80 (0114-0127)",
//   "TODO in Sprint 81 (0128-0210)",
//   "TODO in Sprint 82 (0211-0224)",
//   "TODO in Sprint 83 (0225-0310)",
//   "TODO in Sprint 84 (0311-0324)",
//   "TODO in Sprint 85 (0325-0407)",
//   "TODO in Sprint 86 (0408-0421)",
//   "TODO in Sprint 87 (0422-0505)",
//   "TODO in Sprint 88 (0506-0519)",
//   "TODO in Sprint 89 (0520-0602)",
//   "TODO in Sprint 90 (0603-0616)",
//   "TODO in Sprint 91 (0617-0630)",
//   "TODO in Sprint 92 (0701-0714)",
//   "TODO in Sprint 93 (0715-0728)",
//   "TODO in Sprint 94 (0729-0811)",
//   "TODO in Sprint 95 (0812-0825)",
//   "TODO in Sprint 96 (0826-0908)",
//   "TODO in Sprint 97 (0909-0922)",
//   "TODO in Sprint 98 (0923-1006)",
//   "TODO in Sprint 99 (1007-1020)",
//   "TODO in Sprint 100 (1021-1103)",
//   "TODO in Sprint 101 (1104-1117)",
//   "TODO in Sprint 102 (1118-1201)",
//   "TODO in Sprint 103 (1202-1215)",
//   "TODO in Sprint 104 (1216-1229)",
//   "TODO in Sprint 105 (1230-0112)"
// ];

// ---- 2018 ----
var names = [
  "TODO in Sprint 106 (0113-0126)",
  "TODO in Sprint 107 (0127-0209)",
  "TODO in Sprint 108 (0210-0223)",
  "TODO in Sprint 109 (0224-0309)",
  "TODO in Sprint 110 (0310-0323)",
  "TODO in Sprint 111 (0324-0406)",
  "TODO in Sprint 112 (0407-0420)",
  "TODO in Sprint 113 (0421-0504)",
  "TODO in Sprint 114 (0505-0518)",
  "TODO in Sprint 115 (0519-0601)",
  "TODO in Sprint 116 (0602-0615)",
  "TODO in Sprint 117 (0616-0629)",
  "TODO in Sprint 118 (0630-0713)",
  "TODO in Sprint 119 (0714-0727)",
  "TODO in Sprint 120 (0728-0810)",
  "TODO in Sprint 121 (0811-0824)",
  "TODO in Sprint 122 (0825-0907)",
  "TODO in Sprint 123 (0908-0921)",
  "TODO in Sprint 124 (0922-1005)",
  "TODO in Sprint 125 (1006-1019)",
  "TODO in Sprint 126 (1020-1102)",
  "TODO in Sprint 127 (1103-1116)",
  "TODO in Sprint 128 (1117-1130)",
  "TODO in Sprint 129 (1201-1214)",
  "TODO in Sprint 130 (1215-1228)",
  "TODO in Sprint 131 (1229-0111)"
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
