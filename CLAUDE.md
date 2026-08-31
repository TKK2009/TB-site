# TechnoBotz 23542 — Team Website

Static site for FIRST Tech Challenge team 23542, Frisco, Texas.
No build step. No framework. Plain HTML, CSS, and vanilla JS, deployed to GitHub Pages.

## Commands

```bash
python3 -m http.server 8000   # preview at localhost:8000
open index.html               # also works: no server needed, all paths are relative
git add -A && git commit -m "..." && git push   # deploys via GitHub Pages
```

## Structure

One file, `index.html` (~135KB), containing **eight** pages switched client-side by the
router in the main IIFE. Page ids: `p-home`, `p-team`, `p-robots`, `p-outreach`,
`p-updates`, `p-post-mentorship`, `p-sponsors`, `p-involved`.

Images live in `images/` (originals, never edited) and `images/web/` (the 25 derivatives
the site actually references). `images/embed/` holds smaller copies used only when
building the standalone file. `technobotz-site-standalone.html` is a portable build with
every image inlined as a data URI; it is generated, not hand-edited.

Splitting into separate HTML files was discussed and **deferred** — it is not started, and
the focus-management fixes were to be done in the same pass.

## Who this site is for

Not judges. A parent, a student, or a sponsor with thirty seconds of attention.
Four jobs, in order:

1. Look genuinely impressive in the first three seconds
2. Show who we are as people, with photos, names, and roles
3. Show the robots
4. Get someone to contact us

The site was originally written from the engineering portfolio and read like one. Do not
let portfolio voice back in. Every page ends with a clear action.

## Design system — do not drift from this

Palette comes from the team logo. Never introduce colors outside it.

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#0B2450` | page background |
| `--deep` | `#061731` | darker sections, footer |
| `--lift` | `#12315F` | cards on dark |
| `--orange` | `#F58B4C` | primary accent, CTAs |
| `--yellow` | `#F5C842` | secondary accent (hard hat) |
| `--pink` | `#F2938E` | tertiary (the pig) |
| `--mint` | `#7FD1B9` | rare fourth accent |
| `--paper` / `--warm` | `#F3F6FB` / `#E8EEF7` | light sections |

Type: **Archivo** 800/900 for display, **IBM Plex Sans** for body, **IBM Plex Mono** for
eyebrows, stats, labels. No other families.

## The signature

The team is named after **Technoblade**, the Minecraft YouTuber who played as a crowned pig.
The logo is a pixel-art pig in a hard hat. An FTC field is a 12x12 grid of tiles.

Those two facts produce one visual system used everywhere:
- Interactive hero tile field (cursor proximity lights tiles)
- Tile curtain page transitions
- Tile bar section dividers that animate up in sequence

**Every animation should belong to that system.** Do not add unrelated effects.

The explicit "we are named after a Minecraft YouTuber" section was **removed** by request.
The visual system stays; the explanation does not.

## Non-negotiables

- Do not touch: the palette, Archivo/IBM Plex, the tile system in all three forms, the
  interactive hero field, or the curtain page transitions
- Respect `prefers-reduced-motion` on every animation added
- Keyboard focus must stay visible (`:focus-visible` outline)
- Must work down to 360px wide
- No frameworks, no build step, no npm dependencies
- Never invent team facts. If a number or result is unknown, leave the `EDIT:` marker
- Photos: never stretch, squash, or upscale. Aspect ratio is always preserved; crop with
  `object-fit: cover` plus a deliberate `object-position`

## Verified facts

**Who we are** — Middle school *and* high school students. The nonprofit is
**TechnoBotz Nonprofit**. Contact `techno23542@gmail.com`.

**Robots** (one per season, names confirmed by the team):

| Season | Robot |
|---|---|
| DECODE 2025–26 | **Porkchop** |
| INTO THE DEEP 2024–25 | **Nautilus** — intake pincher, 2-way scoring, 18x18 |
| CENTERSTAGE 2023–24 | **Metal Scraps** — starter bot, rookie season, max endgame |
| BIOBUZZ 2026–27 | no robot yet, no entry on the site |

**Headline accolades** — Texas House Resolution No. 941 (2023) · UIL 5A State Runner-Up
(CENTERSTAGE, 2024, rookie year) · Ruby Division Finalists, North Texas Championship
(DECODE, 2026). Think Awards are *not* a headline accolade; they appear at most once in
passing on the robots page.

**Stats bar** — 2,700+ people reached · 320+ outreach hours · 12 teams mentored ·
6 seasons in FIRST.

**Teams** — Only **FLL Techno Raiders** counts as a team we started. FTC 32329
CoZmicMonkeyZ and FLL Robocoders are teams we **mentor**, not teams we started.

**Other verified** — FLL 2021–2023 · FTC team founded 2023 · 45 recruited into FIRST ·
Sandeepan School, Karnataka has 2,000 students total and we reached 1,700 of them (both
numbers are correct, they are not a contradiction) · presented to 50+ school administrators.

**Sponsorship** — Four tiers: $250 / $1,000 / $2,500 / $5,000, compared across Brand
Promotion, Community Involvement, Program Involvement, Reminders of Gratitude. Tax
deductible through The Hack Foundation. Donate:
`https://hcb.hackclub.com/donations/start/technobotz`. Eight sponsor logos, one grid,
equal size, no featured tier: ally-health, c2-education, chase, cold-stone, polymaker,
simple-interact, snapmaker, texas-instruments.

## Things that were removed — do not reintroduce

R-CADA · AI FTC Judge · "three-time Think Award winner" as a headline · "$15,000 made the
team free" and every dues-eliminated claim · all UK and "two continents" references ·
the Technoblade explainer section · "How Porkchop works" · the five-step funding plan ·
"Systems, not vibes" · the mentors section · the four outreach objectives · the full event
log · "we recruit in late summer" · "There are towns with nothing" · "Come watch".

## Newsletter

EmailOctopus, form id `bc46b9ca-9f27-11f1-b06f-7f41f19c1b0a`. Their form is configured as a
**popup**, not an inline embed, and appears on Home, Outreach, and Get Involved behind a
`[data-newsletter]` button.

Two constraints that cost real debugging time:

- Never modify the script tag, the `src`, or the `data-form` attribute, and never rebuild
  the form by hand. Those values are what connect it to the list.
- Their script mounts `.modal-container` to `<body>` with **`style="display:none"` inline**
  and reveals it on its own trigger. An inline style outranks their own `.active`
  stylesheet rule, so opening the popup means clearing the inline value, not just adding
  the class. `nlOpen()` does this and returns whether the modal is *actually* on screen.
  If it never becomes visible (ad blockers block eomail5.com), the button falls back to
  `mailto:`.

## Voice

Plain, direct, specific. No marketing language. No em dashes. No exclamation marks.
Numbers over adjectives. If a sentence could appear on any team's site, rewrite it.

## Open items

- **Google Form sign-in wall** — `forms.gle/1kyidNzhAGq9CZub8` is the join CTA in 11
  places and currently demands a Google sign-in. Fix in Google Forms settings
  (Responses → Collect email addresses → Do not collect; remove the domain restriction).
  This is a change only the team can make.
- **Dues wording** — the site says "Ask us about dues and what sponsorship covers before
  you decide" as a placeholder. Awaiting the real policy.
- **Missing photos** — `09-fll-years` and `24-snapmaker-machines` have no file yet. Do not
  hide those sections and do not substitute other photos into them.
- **C2 Education logo** is a JPEG with a dark square baked in; a better file was requested.
- **Deferred** — the page split and the focus-management fixes, to be done together.
