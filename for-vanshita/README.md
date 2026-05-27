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

## Making it yours

Everything is editable in plain HTML — open `index.html` and:

- Swap the memory captions in the `.memory` blocks for real stories you two share
- Swap the emoji "art" (`✨`, `☕`, `🌺`, etc.) for real photos by replacing each `<div class="memory-art art-N">…</div>` with `<img src="path/to/photo.jpg" alt="">`
- Edit the letter text inside `.letter-content`
- Tweak the list items inside `.reasons-list`

Colors live at the top of `styles.css` under `:root` if you want a different shade of pink.

Hope she loves it. 💗
