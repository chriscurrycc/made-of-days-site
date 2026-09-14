# made-of-days-site

The public site for **Made of Days** (溯日 in Simplified Chinese) — home page,
privacy policy and support page, each in English and 简体中文. Plain static HTML,
no build step. Every other language reads the English pages.

Everything that ships lives in **`public/`**, and that is the Cloudflare Pages
**build output directory**. Anything outside it (this file, `serve.py`) stays in
the repo but is never published.

| | |
|---|---|
| Live | https://madeofdays.pages.dev |
| Home (en / zh-Hans) | `/` · `/zh-hans/` |
| Privacy Policy URL (en / zh-Hans) | `/privacy/` · `/privacy/zh-hans/` |
| Support URL (en / zh-Hans) | `/support/` · `/support/zh-hans/` |

## Local preview

```sh
python3 serve.py 8788      # http://127.0.0.1:8788
```

It serves `public/` and sends `Cache-Control: no-store`. `python -m http.server`
sends no cache headers at all, which lets browsers quietly keep serving a stale
stylesheet — that cost an afternoon once.

## Deploy

Push to `main`; Cloudflare Pages rebuilds. Settings that must stay as they are:

| | |
|---|---|
| Framework preset | None |
| Build command | *(empty)* |
| **Build output directory** | **`public`** |

Bump the `?v=` on the `_style.css` link in all seven pages (index, zh-hans,
privacy, privacy/zh-hans, support, support/zh-hans, 404) when the stylesheet
changes, so no one is served the old one: `grep -rl '_style.css?v=' public`.

The screenshots and og images are generated from the app repo's store captures by
`Launch/site/gen-site-images.py` there (Launch/ is not committed).
