# made-of-days-site

The public site for **Made of Days** — home page, privacy policy (EN / 简体中文)
and support page. Plain static HTML, no build step.

Everything that ships lives in **`public/`**, and that is the Cloudflare Pages
**build output directory**. Anything outside it (this file, `serve.py`) stays in
the repo but is never published.

| | |
|---|---|
| Live | https://madeofdays.pages.dev |
| Privacy Policy URL (en) | `/privacy/` |
| Privacy Policy URL (zh-Hans) | `/privacy/zh-hans/` |
| Support URL | `/support/` |

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

Bump the `?v=` on the `_style.css` link in all four pages when the stylesheet
changes, so no one is served the old one.
