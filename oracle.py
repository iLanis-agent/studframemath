import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

OC = 40.6
HEADER_H = 14
BEARING = 15

def stud_plan(wallCm):
    if not (wallCm > 0):
        return {"error": "the wall must be positive"}
    studs = math.ceil(wallCm / OC) + 1
    if studs <= 6: verdict = "a closet wall"
    elif studs <= 12: verdict = "a room wall"
    else: verdict = "a whole-side wall"
    return {"studs": studs, "verdict": verdict}

def header_plan(openingCm):
    if not (openingCm > 0):
        return {"error": "the opening must be positive"}
    header = round1(openingCm + BEARING)
    if openingCm < 90: verdict = "a narrow header"
    elif openingCm <= 180: verdict = "a wide header"
    else: verdict = "a beam-scale header"
    return {"header": header, "verdict": verdict}

def cripple_plan(wallCm, openingCm):
    if not (wallCm > 0) or not (openingCm > 0):
        return {"error": "the wall height and the opening must be positive"}
    if openingCm + HEADER_H >= wallCm:
        return {"error": "the opening leaves no room for the labeled header"}
    cripple_height = round1(wallCm - openingCm - HEADER_H)
    cripples = math.ceil(openingCm / OC) + 1
    if cripple_height < 30: verdict = "stub cripples"
    elif cripple_height <= 90: verdict = "working cripples"
    else: verdict = "tall cripples"
    return {"cripples": cripples, "crippleHeight": cripple_height, "verdict": verdict}

def render_stud(r, wallCm):
    return ("A wall " + fmt(wallCm) + " cm takes " + plural(r["studs"], "stud")
            + " on the labeled 40.6 cm spacing - " + r["verdict"] + ".")

def render_header(r, openingCm):
    return ("An opening " + fmt(openingCm) + " cm takes a labeled " + fmt(r["header"])
            + " cm header with a jack and a king each side - " + r["verdict"] + ".")

def render_cripple(r, wallCm, openingCm):
    return ("A wall " + fmt(wallCm) + " cm with a " + fmt(openingCm) + " cm opening takes "
            + plural(r["cripples"], "cripple") + " each " + fmt(r["crippleHeight"])
            + " cm tall over the labeled header - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[366],[200],[0],[240],[480],[40.6],[81.2],[120],[600],[355.5]]:
    add("studPlan", stud_plan, render_stud, a)
for a in [[90],[0],[45],[200],[180],[181],[80],[120],[60],[95.5]]:
    add("headerPlan", header_plan, render_header, a)
for a in [[240,90],[240,180],[240,240],[0,90],[240,0],[240,45],[250,120],[240,200],[280,150],[243.5,90]]:
    add("cripplePlan", cripple_plan, render_cripple, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
