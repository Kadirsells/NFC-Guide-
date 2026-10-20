#!/usr/bin/env python3
"""Baut die statische Website kadirsells.de nach docs/ (für GitHub Pages).

Aufruf:  python3 tools/build_site.py

Alle Texte (Deutsch und Englisch) stehen in tools/content.py.
Design, Schriften und CSS stammen unverändert aus live-2026-10-20/.
"""
import html
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

LIVE = os.path.join(ROOT, "live-2026-10-20", "site")
SRC = os.path.join(ROOT, "tools", "static")
OUT = os.path.join(ROOT, "docs")

SITE_URL = "https://kadirsells.de"
CSS_FILE = "styles-r0bTjds4.css"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- Assets

def build_assets():
    from PIL import Image

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    a = os.path.join(OUT, "assets")
    os.makedirs(a)

    # Lovable-CSS: Schriftpfade relativ machen (Seite läuft auch unter /NFC-Guide-/)
    css = open(os.path.join(LIVE, "assets", CSS_FILE), encoding="utf-8").read()
    css = css.replace("url(/assets/", "url(")
    open(os.path.join(a, "styles.css"), "w", encoding="utf-8").write(css)
    for f in os.listdir(os.path.join(LIVE, "assets")):
        if f.endswith(".woff2"):
            shutil.copy(os.path.join(LIVE, "assets", f), a)
    for f in os.listdir(SRC):
        shutil.copy(os.path.join(SRC, f), a)

    l5e = os.path.join(LIVE, "__l5e", "assets-v1")
    logo = Image.open(os.path.join(l5e, "c629fd05-254a-48e2-a379-1e0d0db486c1", "logo-ks-new.png"))
    logo.resize((320, 320), Image.LANCZOS).save(os.path.join(a, "logo.png"), optimize=True)
    guide = Image.open(os.path.join(l5e, "5684965f-1db7-404b-853d-1ab8f7592623", "der-komplette-praxis-guide-5.png")).convert("RGB")
    guide.resize((1400, 990), Image.LANCZOS).save(os.path.join(a, "praxis-guide.webp"), quality=82)
    shutil.copy(os.path.join(LIVE, "assets", "nfc-supplier-Bvq_ASa4.webp"), os.path.join(a, "lieferant.webp"))
    kadir = Image.open(os.path.join(l5e, "2765dc03-f980-4096-bcf1-1e1715f50f91", "kadir.jpeg")).convert("RGB")
    w, h = kadir.size  # Hochformat -> quadratischer Ausschnitt wie auf der Live-Seite (object-cover, Mitte)
    top = (h - w) // 2
    kadir.crop((0, top, w, top + w)).resize((480, 480), Image.LANCZOS).save(os.path.join(a, "kadir.webp"), quality=82)

    # Vorschaubild für Social Media, 1200 x 630
    og = Image.new("RGB", (1200, 630), (17, 17, 20))
    g = guide.copy()
    g.thumbnail((1000, 560), Image.LANCZOS)
    og.paste(g, ((1200 - g.width) // 2, (630 - g.height) // 2))
    og.save(os.path.join(a, "og-image.jpg"), quality=85)

    shutil.copy(os.path.join(LIVE, "favicon.png"), os.path.join(OUT, "favicon.png"))
    open(os.path.join(OUT, ".nojekyll"), "w").close()


# ---------------------------------------------------------------- Seitengerüst

def rel(page_path, target_path):
    """Relativer Link von page_path nach target_path (beide wie 'en/buy/' oder '')."""
    depth = page_path.count("/")
    return ("../" * depth + target_path) or "./"


ICON_CHEVRON = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" aria-hidden="true"><path d="m15 18-6-6 6-6"></path></svg>'
NAV_LINK = "inline-flex min-h-[40px] items-center justify-center rounded-lg border border-border px-3 text-sm font-medium text-muted-foreground transition-colors hover:border-accent hover:text-foreground focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring sm:px-4"
FOOT_LINK = "text-sm text-muted-foreground transition-colors hover:text-foreground focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring"


def header(lang, pid):
    t = C.T[lang]
    p = C.PATHS[lang][pid]
    other = "en" if lang == "de" else "de"
    home = rel(p, C.PATHS[lang]["home"])
    cur = ' aria-current="page"'
    return f'''<header data-header class="fixed inset-x-0 top-0 z-50 transition-colors duration-300 motion-reduce:transition-none border-b border-transparent bg-transparent"><div class="flex items-center gap-4 px-4 py-3 sm:gap-6 sm:px-5 sm:py-4"><a aria-label="{esc(t["to_home"])}" class="inline-flex min-h-[44px] items-center justify-center rounded-md px-2 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring" href="{home}"{cur if pid == "home" else ""}><img src="{rel(p, "assets/logo.png")}" alt="{esc(t["logo_alt"])}" width="80" height="80" class="w-auto object-contain transition-all duration-300 motion-reduce:transition-none h-16 sm:h-20"/></a><nav class="flex items-center gap-2 sm:gap-3" aria-label="{esc(t["nav_label"])}"><a class="{NAV_LINK}" href="{home}"{cur if pid == "home" else ""}>{t["nav_home"]}</a><a class="{NAV_LINK}" href="{rel(p, C.PATHS[lang]["contact"])}"{cur if pid == "contact" else ""}>{t["nav_contact"]}</a></nav><a class="ks-lang {NAV_LINK}" href="{rel(p, C.PATHS[other][pid])}" hreflang="{other}" lang="{other}" aria-label="{esc(t["lang_switch_label"])}"><span aria-hidden="true">{t["lang_switch_flag"]}</span>{t["lang_switch"]}</a></div></header><div aria-hidden="true" class="h-[88px] sm:h-[112px]"></div>'''


def footer(lang, pid):
    t = C.T[lang]
    p = C.PATHS[lang][pid]
    links = [
        (rel(p, C.PATHS[lang]["imprint"]), t["f_imprint"], ""),
        (rel(p, C.PATHS[lang]["privacy"]), t["f_privacy"], ""),
        (rel(p, C.PATHS[lang]["withdrawal"]), t["f_withdrawal"], ""),
        (rel(p, C.PATHS[lang]["contact"]), t["f_contact"], ""),
        (f"mailto:{C.EMAIL}", t["f_mail"], ""),
        (C.INSTAGRAM, "Instagram", ' target="_blank" rel="noreferrer"'),
    ]
    nav = "".join(f'<a href="{h}" class="{FOOT_LINK}"{x}>{n}</a>' for h, n, x in links)
    return f'''<footer class="border-t border-border px-5 pb-28 pt-12 sm:pb-12"><div class="mx-auto flex max-w-3xl flex-col gap-4"><nav class="flex flex-wrap gap-x-6 gap-y-3" aria-label="{esc(t["footer_label"])}">{nav}</nav><p class="text-sm text-muted-foreground">© 2026 Kadirsells · {C.LEGAL_NAME}. {t["rights"]}</p></div></footer>'''


def head(lang, pid, extra_ld=None):
    t = C.T[lang]
    meta = C.META[lang][pid]
    p = C.PATHS[lang][pid]
    canon = f"{SITE_URL}/{p}"
    alt = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{C.PATHS[l][pid]}"/>' for l in ("de", "en")
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{C.PATHS["de"][pid]}"/>'
    robots = "noindex, follow" if meta.get("noindex") else "index, follow"
    og_img = f"{SITE_URL}/assets/og-image.jpg"
    ld = ""
    for obj in (extra_ld or []):
        ld += '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"
    return f'''<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><title>{esc(meta["title"])}</title><meta name="description" content="{esc(meta["description"])}"/><meta name="author" content="{esc(C.LEGAL_NAME)}"/><meta name="robots" content="{robots}"/><link rel="canonical" href="{canon}"/>{alt}<meta property="og:type" content="website"/><meta property="og:site_name" content="Kadirsells"/><meta property="og:locale" content="{t["og_locale"]}"/><meta property="og:url" content="{canon}"/><meta property="og:title" content="{esc(meta["title"])}"/><meta property="og:description" content="{esc(meta["description"])}"/><meta property="og:image" content="{og_img}"/><meta property="og:image:width" content="1200"/><meta property="og:image:height" content="630"/><meta property="og:image:alt" content="{esc(t["og_image_alt"])}"/><meta name="twitter:card" content="summary_large_image"/><meta name="twitter:title" content="{esc(meta["title"])}"/><meta name="twitter:description" content="{esc(meta["description"])}"/><meta name="twitter:image" content="{og_img}"/><meta name="theme-color" content="#111114"/><link rel="icon" type="image/png" href="{rel(p, "favicon.png")}"/><link rel="stylesheet" href="{rel(p, "assets/styles.css")}"/><link rel="stylesheet" href="{rel(p, "assets/extra.css")}"/>{ld}<script defer src="{rel(p, "assets/site.js")}"></script></head><body><a class="ks-skip" href="#inhalt">{t["skip"]}</a>'''


def page(lang, pid, main_html, ld=None):
    return (
        head(lang, pid, ld)
        + header(lang, pid)
        + f'<main id="inhalt" class="{C.MAIN_CLASS.get(pid, "")}">{main_html}</main>'
        + footer(lang, pid)
        + "</body></html>\n"
    )


def write(lang, pid, doc):
    path = os.path.join(OUT, C.PATHS[lang][pid], "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(doc)


# ---------------------------------------------------------------- Startseite

def stack(lang, p, guide_first=True):
    t = C.T[lang]
    return f'''<div class="hero-rise-2" data-stack><div class="relative w-full" style="perspective:1200px;padding-bottom:62%"><div class="absolute inset-0"><button type="button" data-card="lieferant" aria-label="{esc(t["hero_switch_supplier"])}" class="ks-card absolute left-[2%] top-[12%] block w-[78%] overflow-hidden rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring is-back"><span class="block hero-float-back"><img src="{rel(p, "assets/lieferant.webp")}" alt="{esc(t["img_supplier_alt"])}" loading="eager" decoding="async" width="1400" height="990" class="block h-auto w-full"/></span></button><button type="button" data-card="guide" aria-label="{esc(t["hero_switch_guide"])}" class="ks-card absolute left-[2%] top-[12%] block w-[78%] overflow-hidden rounded-2xl focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring is-front"><span class="block hero-float-front"><img src="{rel(p, "assets/praxis-guide.webp")}" alt="{esc(t["img_guide_alt"])}" loading="eager" decoding="async" width="1400" height="990" class="block h-auto w-full"/></span></button></div><span data-counter class="absolute bottom-0 right-0 z-30 font-mono text-[11px] tracking-widest text-muted-foreground">1 / 2</span></div><div role="tablist" aria-label="{esc(t["hero_tablist"])}" class="mt-5 flex w-full items-center gap-2 rounded-full border border-accent/40 p-1"><button type="button" role="tab" data-tab="guide" aria-selected="true" class="ks-tab h-11 flex-1 rounded-full px-4 font-display text-xs uppercase tracking-wide transition-colors focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring">{t["tab_guide"]}</button><button type="button" role="tab" data-tab="lieferant" aria-selected="false" class="ks-tab h-11 flex-1 rounded-full px-4 font-display text-xs uppercase tracking-wide transition-colors focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring">{t["tab_supplier"]}</button></div></div>'''


def home(lang):
    t = C.T[lang]
    H = C.HOME[lang]
    p = C.PATHS[lang]["home"]
    buy = rel(p, C.PATHS[lang]["buy"])
    buysup = rel(p, C.PATHS[lang]["buysup"])
    hero_data = {
        "guide": {**H["hero"]["guide"], "href": buy},
        "lieferant": {**H["hero"]["lieferant"], "href": buysup},
    }
    g = H["hero"]["guide"]
    hero = f'''<section class="px-5 pb-14 pt-10 sm:pt-16" data-hero='{esc(json.dumps(hero_data, ensure_ascii=False))}'><div class="mx-auto grid max-w-6xl items-center gap-10 lg:grid-cols-2"><div class="hero-rise-1"><div data-hero-text class="ks-fade"><p data-f="eyebrow" class="text-[11px] font-semibold uppercase tracking-[0.28em] text-gold">{g["eyebrow"]}</p><h1 class="mt-4 flex min-h-[2lh] flex-col justify-start font-display text-[clamp(1.9rem,8.8vw,4.5rem)] uppercase leading-[0.85] tracking-tight text-foreground"><span data-f="h1a" class="whitespace-nowrap">{g["h1a"]}</span><span data-f="h1b" class="whitespace-nowrap">{g["h1b"]}</span></h1><p data-f="tagline" class="mt-5 font-display text-[clamp(0.9rem,3.7vw,1.35rem)] uppercase leading-tight tracking-tight text-muted-foreground">{g["tagline"]}</p></div><div class="mt-8 lg:hidden">{stack(lang, p)}</div><div data-hero-buy class="mt-8 ks-fade"><p class="font-display text-[clamp(2rem,9vw,3rem)] leading-none tracking-tight text-foreground"><span data-f="price">{g["price"]}</span> <span class="ks-vat">{t["incl_vat"]}</span></p><a id="hero-cta" data-f="cta" href="{buy}" class="mt-4 flex h-14 w-full items-center justify-center rounded-xl bg-accent px-7 font-display text-base uppercase tracking-wide text-accent-foreground transition-colors hover:bg-accent/85 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring lg:w-auto lg:px-10">{g["cta"]}</a><p class="mt-3 text-sm text-muted-foreground">{t["digital_note"]}</p></div></div><div class="hidden lg:block"><div class="mx-auto w-full max-w-[560px]">{stack(lang, p)}</div></div></div></section>'''

    def text_section(title, paras, extra=""):
        ps = "".join(f"<p>{x}</p>" for x in paras)
        return f'<section class="border-t border-border px-5 py-16"><div class="mx-auto max-w-3xl"><h2 class="font-display text-[clamp(2rem,10vw,3.5rem)] uppercase leading-[0.9] tracking-tight text-foreground">{title}</h2><div class="mt-6 space-y-4 text-lg leading-relaxed text-muted-foreground">{ps}</div>{extra}</div></section>'

    problem = text_section(H["problem_title"], H["problem"])
    note = f'<p class="ks-note mt-6">{H["google_note"]}</p>'
    loesung = text_section(H["solution_title"], H["solution"], note)

    icons = C.ICONS
    tiles = "".join(
        f'<div class="rounded-xl border border-border bg-card p-4 text-center">{icons[i].format(cls="mx-auto h-7 w-7 " + ("text-gold" if i == "star" else "text-accent"))}<p class="mt-3 font-display text-xs uppercase leading-tight tracking-wide text-foreground">{txt}</p></div>'
        for i, txt in H["tiles"]
    )
    tiles = f'<section class="border-t border-border px-5 py-12"><div class="mx-auto grid max-w-3xl grid-cols-2 gap-3 sm:grid-cols-4">{tiles}</div></section>'

    chapters = "".join(
        f'<li class="rounded-xl border border-border bg-card p-4"><span class="font-display text-sm tracking-wide text-accent">{i + 1:02d}</span><p class="mt-1 text-base leading-snug text-foreground">{c}</p></li>'
        for i, c in enumerate(H["chapters"])
    )
    inhalt = f'''<section class="border-t border-border px-5 py-16"><div class="mx-auto max-w-3xl"><h2 class="font-display text-[clamp(2rem,10vw,3.5rem)] uppercase leading-[0.9] tracking-tight text-foreground">{H["content_title"]}</h2><p class="mt-4 text-muted-foreground">{H["content_sub"]}</p><ol class="mt-8 grid gap-3 sm:grid-cols-2">{chapters}</ol><div class="mt-6 rounded-xl border-2 border-gold/60 bg-card p-5"><p class="font-display text-xs uppercase tracking-[0.22em] text-gold">Bonus</p><p class="mt-2 text-lg leading-snug text-foreground">{H["bonus"]}</p></div></div></section>'''

    about_p = "".join(f"<p>{x}</p>" for x in H["about"])
    about = f'''<section class="border-t border-border px-5 py-16"><div class="mx-auto grid max-w-3xl gap-8 md:grid-cols-[200px_1fr] md:items-center"><div class="mx-auto w-full max-w-[200px] rounded-2xl border border-accent bg-card p-2 shadow-lg"><img src="{rel(p, "assets/kadir.webp")}" alt="{esc(H["about_img_alt"])}" loading="lazy" width="480" height="480" class="aspect-square w-full rounded-xl object-cover"/></div><div class="min-w-0"><h2 class="font-display text-[clamp(2rem,10vw,3.5rem)] uppercase leading-[0.9] tracking-tight text-foreground">{H["about_title"]}</h2><p class="mt-4 text-lg text-foreground">Kadir</p><p class="text-muted-foreground">@kadirsells</p><div class="mt-4 space-y-4 text-lg leading-relaxed text-muted-foreground">{about_p}</div><a href="{C.INSTAGRAM}" target="_blank" rel="noreferrer" class="mt-6 inline-flex items-center justify-center rounded-xl border border-accent px-6 py-3 font-display text-sm uppercase tracking-wide text-foreground transition-colors hover:bg-accent focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring">{H["about_cta"]}</a></div></div></section>'''

    faq_items = "".join(
        f'<details class="ks-faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in H["faq"]
    )
    faq = f'<section class="border-t border-border px-5 py-16"><div class="mx-auto max-w-3xl"><h2 class="font-display text-[clamp(2rem,10vw,3.5rem)] uppercase leading-[0.9] tracking-tight text-foreground">{H["faq_title"]}</h2><div class="mt-8 space-y-3">{faq_items}</div></div></section>'

    sticky = f'''<div data-sticky class="fixed inset-x-0 bottom-0 z-50 border-t border-border bg-card/95 px-4 py-3 backdrop-blur transition-transform duration-200 motion-reduce:transition-none sm:hidden translate-y-full" aria-hidden="true"><div class="flex items-center gap-3"><span class="shrink-0 font-display text-lg tracking-tight text-foreground">29,99 €</span><a href="{buy}" tabindex="-1" class="inline-flex w-full items-center justify-center rounded-xl bg-accent font-display uppercase tracking-wide text-accent-foreground transition-colors hover:bg-accent/85 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring flex-1 px-4 py-3 text-base">{g["cta"]}</a></div></div>'''

    url = f"{SITE_URL}/{p}"
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": C.META[lang]["home"]["product_name"],
            "description": C.META[lang]["home"]["description"],
            "image": f"{SITE_URL}/assets/og-image.jpg",
            "brand": {"@type": "Brand", "name": "Kadirsells"},
            "inLanguage": "de",
            "offers": {
                "@type": "Offer",
                "url": f"{SITE_URL}/{C.PATHS[lang]['buy']}",
                "price": "29.99",
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "seller": {"@type": "Organization", "name": "Digistore24 GmbH"},
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": C.LEGAL_NAME,
            "alternateName": "Kadir",
            "url": url,
            "sameAs": [C.INSTAGRAM],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in H["faq"]
            ],
        },
    ]
    main = hero + problem + loesung + tiles + inhalt + faq + about + sticky
    write(lang, "home", page(lang, "home", main, ld))


# ---------------------------------------------------------------- Kaufseiten

def buy_page(lang, pid):
    t = C.T[lang]
    B = C.BUY[lang][pid]
    p = C.PATHS[lang][pid]
    items = "".join(
        f'<li class="flex gap-3 text-foreground"><span aria-hidden="true" class="shrink-0 text-gold">✓</span><span>{x}</span></li>'
        for x in B["items"]
    )
    extra = ""
    if B.get("handover"):
        extra = "".join(f'<p class="mt-3 text-sm text-muted-foreground">{x}</p>' for x in B["handover"])
    main = f'''<div class="mx-auto w-full max-w-[640px]"><a href="{rel(p, C.PATHS[lang]["home"])}" class="mb-8 inline-flex items-center gap-2 text-sm font-medium text-muted-foreground transition-colors hover:text-foreground focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring">{ICON_CHEVRON}{t["back_home"]}</a><h1 class="font-display text-[clamp(2rem,9vw,3.25rem)] uppercase leading-[0.9] tracking-tight text-foreground">{t["order_title"]}</h1><section class="mt-8 overflow-hidden rounded-2xl border border-border bg-card"><div class="border-b border-border bg-[#0a0a0c] p-4 sm:p-6"><img src="{rel(p, "assets/" + B["img"])}" alt="{esc(B["img_alt"])}" width="1400" height="990" class="mx-auto w-full max-w-md rounded-xl object-contain" loading="eager"/></div><div class="p-5 sm:p-8"><h2 class="font-display text-2xl uppercase leading-tight tracking-tight text-foreground">{B["name"]}</h2><p class="mt-3 text-muted-foreground">{B["sub"]}</p><ul class="mt-6 space-y-3">{items}</ul>{extra}<div class="mt-8 flex flex-wrap items-baseline gap-3 border-t border-border pt-6"><span class="font-display text-4xl tracking-tight text-foreground">{B["price"]}</span><span class="text-sm text-muted-foreground">{t["incl_vat"]} · {t["one_time"]}</span></div><a href="{B["checkout"]}" class="mt-6 inline-flex min-h-[56px] w-full items-center justify-center rounded-xl bg-accent px-8 py-4 font-display text-lg uppercase tracking-wide text-accent-foreground transition-colors hover:bg-accent/85 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring">{t["buy_now"]}</a><p class="ks-prose mt-4 text-sm text-muted-foreground">{t["seller_note"]}</p><p class="mt-3 text-xs text-muted-foreground">{t["buy_footer"]}</p></div></section></div>'''
    write(lang, pid, page(lang, pid, main))


# ---------------------------------------------------------------- Kontakt

def contact(lang):
    t = C.T[lang]
    K = C.CONTACT[lang]
    main = f'''<div class="mx-auto max-w-3xl text-center"><p class="text-sm font-semibold uppercase tracking-widest text-accent">{K["eyebrow"]}</p><h1 class="mt-3 font-display text-[clamp(2.5rem,10vw,4rem)] uppercase leading-[0.9] tracking-tight text-foreground">{K["title"]}</h1><p class="mt-4 text-lg text-muted-foreground">{K["sub"]}</p></div><div class="mx-auto mt-12 grid max-w-2xl gap-4 sm:grid-cols-2">{contact_card(f"mailto:{C.EMAIL}", C.ICONS["mail"], K["mail_title"], C.EMAIL, "")}{contact_card(C.INSTAGRAM, C.ICONS["instagram"], K["ig_title"], K["ig_sub"], ' target="_blank" rel="noreferrer"')}</div>'''
    write(lang, "contact", page(lang, "contact", main))


def contact_card(href, icon, title, sub, extra):
    return f'''<a href="{href}"{extra} class="group flex flex-col items-center justify-center gap-4 rounded-2xl border border-border bg-card p-8 text-center transition-colors hover:border-accent hover:bg-card/80 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ring"><div class="flex h-16 w-16 items-center justify-center rounded-full bg-accent/10 text-accent">{icon.format(cls="h-8 w-8")}</div><span class="font-display text-xl uppercase tracking-tight text-foreground">{title}</span><span class="text-sm text-muted-foreground">{sub}</span></a>'''


# ---------------------------------------------------------------- Rechtstexte

def legal(lang, pid):
    t = C.T[lang]
    L = C.LEGAL[lang][pid]
    p = C.PATHS[lang][pid]
    secs = ""
    for i, (title, blocks) in enumerate(L["sections"], 1):
        body = "".join(blocks)
        hl = " ks-highlight" if title.startswith("!") else ""
        title = title.lstrip("!")
        secs += f'<section class="scroll-mt-24{hl}"><h2 class="mb-4 flex items-baseline gap-3 font-display text-2xl leading-tight tracking-tight text-foreground"><span class="text-gold">{i}.</span>{title}</h2><div class="ks-prose space-y-4 border-l-2 border-accent/30 pl-5 text-sm leading-relaxed text-muted-foreground sm:text-base">{body}</div></section>'
    note = f'<p class="ks-note mt-6">{L["note"]}</p>' if L.get("note") else ""
    main = f'''<a href="{rel(p, C.PATHS[lang]["home"])}" class="mb-10 inline-flex items-center gap-2 text-sm font-medium text-muted-foreground transition-colors hover:text-foreground focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ring">{ICON_CHEVRON}{t["back_home"]}</a><header class="mb-12 border-b border-border pb-8"><p class="mb-3 text-sm font-semibold uppercase tracking-widest text-gold">{t["legal_eyebrow"]}</p><h1 class="font-display text-4xl uppercase leading-none tracking-tight text-foreground sm:text-5xl">{L["title"]}</h1><p class="mt-4 text-base text-muted-foreground">{L["sub"]}</p>{note}</header><article class="space-y-10">{secs}</article><p class="mt-12 text-sm text-muted-foreground">{L["stand"]}</p>'''
    write(lang, pid, page(lang, pid, main))


# ---------------------------------------------------------------- 404, Sitemap, robots

def not_found():
    # GitHub Pages liefert 404.html für jede unbekannte Adresse aus, daher absolute Pfade
    # über ein <base>, das sowohl unter kadirsells.de als auch unter /NFC-Guide-/ stimmt.
    base_js = "<script>(function(){var m=location.pathname.match(/^\\/NFC-Guide-\\//i);document.write('<base href=\"'+(m?m[0]:'/')+'\">')})()</script>"
    t = C.T["de"]
    doc = f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>{base_js}<title>Seite nicht gefunden – Kadirsells</title><meta name="robots" content="noindex"/><link rel="icon" type="image/png" href="favicon.png"/><link rel="stylesheet" href="assets/styles.css"/><link rel="stylesheet" href="assets/extra.css"/></head><body><main class="mx-auto flex min-h-screen max-w-3xl flex-col items-center justify-center px-5 py-16 text-center"><img src="assets/logo.png" alt="{esc(t["logo_alt"])}" width="80" height="80" class="h-20 w-auto"/><h1 class="mt-8 font-display text-[clamp(2.5rem,10vw,4rem)] uppercase leading-[0.9] tracking-tight text-foreground">Seite nicht gefunden</h1><p class="mt-4 text-lg text-muted-foreground">Diese Adresse gibt es nicht (mehr). <span lang="en">This page does not exist.</span></p><div class="mt-8 flex flex-wrap justify-center gap-3"><a href="./" class="inline-flex h-14 items-center justify-center rounded-xl bg-accent px-7 font-display text-base uppercase tracking-wide text-accent-foreground hover:bg-accent/85">Zur Startseite</a><a href="en/" lang="en" class="inline-flex h-14 items-center justify-center rounded-xl border border-accent px-7 font-display text-base uppercase tracking-wide text-foreground hover:bg-accent">English</a></div></main></body></html>
'''
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(doc)


def sitemap():
    urls = ""
    for pid in C.PATHS["de"]:
        if C.META["de"][pid].get("noindex"):
            continue
        alts = "".join(
            f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE_URL}/{C.PATHS[l][pid]}"/>' for l in ("de", "en")
        ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}/{C.PATHS["de"][pid]}"/>'
        for l in ("de", "en"):
            urls += f"  <url><loc>{SITE_URL}/{C.PATHS[l][pid]}</loc><lastmod>{C.LASTMOD}</lastmod>{alts}</url>\n"
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n'
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    )


def main():
    build_assets()
    for lang in ("de", "en"):
        home(lang)
        buy_page(lang, "buy")
        buy_page(lang, "buysup")
        contact(lang)
        for pid in ("imprint", "privacy", "withdrawal"):
            legal(lang, pid)
    not_found()
    sitemap()
    print("Fertig:", OUT)


if __name__ == "__main__":
    main()
