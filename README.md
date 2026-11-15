# davidvshih.com

Static portfolio site, served by GitHub Pages from the root of `main`.

## Layout

- `index.html`: the built site. Do not edit by hand.
- `img/`: project page images. `img/home/` holds the home tiles and portraits, copied in by the build.
- `src/template.html`: page template, CSS, cloud script, hash router.
- `src/cases.py`: data for the 21 project pages.
- `src/build.py`: builds the site.
- `src/work/`: source images for the home tiles and portraits.
- Folders such as `jeep/` and `sony-alpha-camera/`: redirects from old addresses to the hash routes. The build writes them.

## Build

    python3 src/build.py gold

Writes `index.html`, the redirects, and `404.html` at the repo root. `brown` also builds. Commit and push to publish.

New project images go in `img/`. New home tile images go in `src/work/`.
