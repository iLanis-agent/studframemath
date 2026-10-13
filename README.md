# Stud frame math

Stud frame math lays out the wall before the lumber cart: the wall at
the labeled spacing becomes the stud count, the opening plus the
labeled bearing becomes the header, and the wall minus the opening and
the labeled header becomes the cripples.

Live site: https://ilanis-agent.github.io/studframemath/

## The three tools

- **Stud plan** - `ceil(wall / labeled 40.6 cm) + 1` studs, with a
  closet / room / whole-side wall verdict.
- **Header plan** - `opening + labeled 15 cm bearing` of header with a
  jack and a king each side, with a narrow / wide / beam-scale verdict.
- **Cripple plan** - `ceil(opening / 40.6) + 1` cripples each
  `wall - opening - labeled 14 cm header` tall, with a stub / working /
  tall verdict.

## Limits

Every default is labeled and illustrative. Real framing carries real
loads: spans, bearing and fastening follow the local code, the span
tables and, where it matters, the engineer. This is layout arithmetic,
not a structural design or a load rating.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 142 checks)

Run the tests: `python3 oracle.py && node test.js`
