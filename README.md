# made-of-days-site

The public site for **Made of Days** — home page, privacy policy (EN / 简体中文)
and support page. Plain static HTML, no build step.

- Deployed to Cloudflare Pages → https://madeofdays.pages.dev
- Privacy Policy URL (en): `/privacy/`
- Privacy Policy URL (zh-Hans): `/privacy/zh-hans/`
- Support URL: `/support/`

## Local preview

```sh
python3 serve.py 8788      # http://127.0.0.1:8788
```

`serve.py` sends `Cache-Control: no-store`; `python -m http.server` sends no
cache headers at all, which lets browsers quietly serve a stale stylesheet.

## Deploy

```sh
npx wrangler pages deploy . --project-name madeofdays
```

Bump the `?v=` on the `_style.css` link when the stylesheet changes.
