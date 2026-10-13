(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }
  var OC = 40.6, HEADER_H = 14, BEARING = 15;

  function studPlan(wallCm) {
    if (!(wallCm > 0)) return { error: "the wall must be positive" };
    var studs = Math.ceil(wallCm / OC) + 1;
    var verdict;
    if (studs <= 6) verdict = "a closet wall";
    else if (studs <= 12) verdict = "a room wall";
    else verdict = "a whole-side wall";
    return { studs: studs, verdict: verdict };
  }

  function headerPlan(openingCm) {
    if (!(openingCm > 0)) return { error: "the opening must be positive" };
    var header = round1(openingCm + BEARING);
    var verdict;
    if (openingCm < 90) verdict = "a narrow header";
    else if (openingCm <= 180) verdict = "a wide header";
    else verdict = "a beam-scale header";
    return { header: header, verdict: verdict };
  }

  function cripplePlan(wallCm, openingCm) {
    if (!(wallCm > 0) || !(openingCm > 0)) return { error: "the wall height and the opening must be positive" };
    if (openingCm + HEADER_H >= wallCm) return { error: "the opening leaves no room for the labeled header" };
    var crippleHeight = round1(wallCm - openingCm - HEADER_H);
    var cripples = Math.ceil(openingCm / OC) + 1;
    var verdict;
    if (crippleHeight < 30) verdict = "stub cripples";
    else if (crippleHeight <= 90) verdict = "working cripples";
    else verdict = "tall cripples";
    return { cripples: cripples, crippleHeight: crippleHeight, verdict: verdict };
  }

  function renderStud(r, wallCm) {
    return "A wall " + wallCm + " cm takes " + plural(r.studs, "stud") + " on the labeled 40.6 cm spacing - " + r.verdict + ".";
  }

  function renderHeader(r, openingCm) {
    return "An opening " + openingCm + " cm takes a labeled " + r.header + " cm header with a jack and a king each side - " + r.verdict + ".";
  }

  function renderCripple(r, wallCm, openingCm) {
    return "A wall " + wallCm + " cm with a " + openingCm + " cm opening takes " + plural(r.cripples, "cripple") + " each " + r.crippleHeight + " cm tall over the labeled header - " + r.verdict + ".";
  }

  var api = { studPlan: studPlan, headerPlan: headerPlan, cripplePlan: cripplePlan, renderStud: renderStud, renderHeader: renderHeader, renderCripple: renderCripple };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.StudframeMath = api;
})(this);
