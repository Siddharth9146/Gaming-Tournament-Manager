# For Vanshita 💕

A little hand-built love letter — a soft pink, animated memory gallery
made just because she deserves to smile today.

## How to open it

Just open `index.html` in any browser. No server, no setup, no fuss.

```bash
# from the repo root
open for-vanshita/index.html
# or on Linux
xdg-open for-vanshita/index.html
```

## What's inside

- A glowing intro page with her name
- A gallery of six "memories" with romantic placeholder captions
- An animated "Reasons I love you" list that reveals as you scroll
- A clickable envelope with a hidden love letter (and a heart burst when it opens)
- Soft floating hearts drifting up the screen, the whole time

## Adding your real photos

The gallery is already wired up to use real photos. Just drop the 5 pictures
into `photos/` with these exact filenames:

- `photos/photo1.jpg` — the blackboard selfie (caption: *"Side by side, always"*)
- `photos/photo2.jpg` — Vanshita on the balcony at night (caption: *"You, lighting up the night"*)
- `photos/photo3.jpg` — the daytime outdoor selfie (caption: *"Quiet afternoons with you"*)
- `photos/photo4.jpg` — the cozy bed selfie with the duck plushie (caption: *"Home is wherever you are"*)
- `photos/photo5.jpg` — the Holi photo (caption: *"Colour, chaos, and you"*)

See `photos/README.md` for more details. If any photo is missing the page still
looks lovely — it shows a soft pink fallback card instead.

## Making it yours

Everything is editable in plain HTML — open `index.html` and:

- Edit any memory caption inside the `.memory` blocks
- Edit the letter text inside `.letter-content`
- Tweak the list items inside `.reasons-list`

Colors live at the top of `styles.css` under `:root` if you want a different shade of pink.

Hope she loves it. 💗
