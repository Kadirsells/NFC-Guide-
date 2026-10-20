# Alle Texte der Website, Deutsch (de) und Englisch (en).
# Nach einer Änderung:  python3 tools/build_site.py

LEGAL_NAME = "Elyesa Kadir Yildirim"
EMAIL = "elyesakadiryildirim@gmail.com"
INSTAGRAM = "https://instagram.com/kadirsells"
LASTMOD = "2026-10-20"

CHECKOUT_GUIDE = "https://www.checkout-ds24.com/product/721214"
CHECKOUT_SUPPLIER = "https://www.checkout-ds24.com/product/728685"
DS24 = {
    "de": {
        "terms": "https://www.digistore24.com/extern/cms/page/popup/legal/terms/1/de/42",
        "withdrawal": "https://www.digistore24.com/extern/cms/page/popup/legal/cancellation/1/de/42",
        "contact": "https://www.digistore24.com/extern/cms/page/popup/legal/contact/1/de",
        "privacy": "https://www.digistore24.com/page/privacy",
    },
    "en": {
        "terms": "https://www.digistore24.com/extern/cms/page/popup/legal/terms/1/en/42",
        "withdrawal": "https://www.digistore24.com/extern/cms/page/popup/legal/cancellation/1/en/42",
        "contact": "https://www.digistore24.com/extern/cms/page/popup/legal/contact/1/en",
        "privacy": "https://www.digistore24.com/page/privacy",
    },
}

PATHS = {
    "de": {
        "home": "",
        "buy": "kaufen/",
        "buysup": "kaufen-kontakt/",
        "contact": "kontakt/",
        "imprint": "impressum/",
        "privacy": "datenschutz/",
        "withdrawal": "widerruf/",
    },
    "en": {
        "home": "en/",
        "buy": "en/buy/",
        "buysup": "en/buy-supplier/",
        "contact": "en/contact/",
        "imprint": "en/legal-notice/",
        "privacy": "en/privacy/",
        "withdrawal": "en/withdrawal/",
    },
}

MAIN_CLASS = {
    "home": "min-h-screen bg-background",
    "buy": "px-5 py-10 sm:py-16",
    "buysup": "px-5 py-10 sm:py-16",
    "contact": "px-5 py-16 sm:py-24",
    "imprint": "mx-auto min-h-screen max-w-3xl px-5 py-16 sm:py-24",
    "privacy": "mx-auto min-h-screen max-w-3xl px-5 py-16 sm:py-24",
    "withdrawal": "mx-auto min-h-screen max-w-3xl px-5 py-16 sm:py-24",
}

_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" class="{cls}" aria-hidden="true">'
ICONS = {
    "nfc": _SVG + '<path d="M6 8.32a7.43 7.43 0 0 1 0 7.36"></path><path d="M9.46 6.21a11.76 11.76 0 0 1 0 11.58"></path><path d="M12.91 4.1a15.91 15.91 0 0 1 .01 15.8"></path><path d="M16.37 2a20.16 20.16 0 0 1 0 20"></path></svg>',
    "star": _SVG + '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path></svg>',
    "trend": _SVG + '<path d="M16 7h6v6"></path><path d="m22 7-8.5 8.5-5-5L2 17"></path></svg>',
    "tag": _SVG + '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"></path><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"></circle></svg>',
    "mail": _SVG + '<path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"></path><rect x="2" y="4" width="20" height="16" rx="2"></rect></svg>',
    "instagram": _SVG + '<rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>',
}
_GLOBE = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>'


def _a(href, text, ext=True):
    x = ' target="_blank" rel="noreferrer"' if ext else ""
    return f'<a href="{href}"{x}>{text}</a>'


def _p(*xs):
    return [f"<p>{x}</p>" for x in xs]


def _ul(*xs):
    return ["<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"]


_ADDR = f"{LEGAL_NAME}<br/>Kadirsells<br/>Scheckerstraße 12<br/>97299 Zell am Main<br/>"

# ======================================================================= Allgemein

T = {
    "de": {
        "to_home": "Zur Startseite",
        "logo_alt": "Kadir Sells – Logo",
        "nav_label": "Hauptnavigation",
        "nav_home": "Startseite",
        "nav_contact": "Kontakt",
        "lang_switch": "EN",
        "lang_switch_flag": _GLOBE,
        "lang_switch_label": "Switch to English",
        "f_imprint": "Impressum",
        "f_privacy": "Datenschutz",
        "f_withdrawal": "Widerruf",
        "f_contact": "Kontakt",
        "f_mail": "Mail",
        "footer_label": "Rechtliches und Kontakt",
        "rights": "Alle Rechte vorbehalten.",
        "og_locale": "de_DE",
        "og_image_alt": "Mockup des Praxis-Guides „NFC Bewertungskarten verkaufen“",
        "skip": "Zum Inhalt springen",
        "hero_switch_supplier": "Zum Lieferanten-Produkt wechseln",
        "hero_switch_guide": "Zum Praxis-Guide wechseln",
        "img_supplier_alt": "NFC-Bewertungskarten Lieferantenkontakt – Produktbild",
        "img_guide_alt": "NFC Bewertungskarten System – Der komplette Praxis-Guide",
        "hero_tablist": "Produkt wählen",
        "tab_guide": "Praxis-Guide",
        "tab_supplier": "Nur der Lieferant",
        "incl_vat": "inkl. MwSt.",
        "digital_note": "Digitales Produkt, sofort nach dem Kauf verfügbar.",
        "back_home": "Zurück zur Startseite",
        "order_title": "Deine Bestellung",
        "one_time": "Einmalzahlung, kein Abo",
        "buy_now": "Weiter zur Kasse",
        "seller_note": (
            "Verkäufer und Vertragspartner ist die Digistore24 GmbH. Es gelten die "
            + _a(DS24["de"]["terms"], "AGB")
            + " und die "
            + _a(DS24["de"]["withdrawal"], "Widerrufsbelehrung")
            + " von Digistore24. Den Download-Link bekommst du direkt nach dem Kauf per E-Mail."
        ),
        "buy_footer": "Zahlung per Kreditkarte, Lastschrift, PayPal oder Vorkasse · Fragen? Instagram-DM an @kadirsells oder E-Mail",
        "legal_eyebrow": "Rechtliches",
    },
    "en": {
        "to_home": "Go to homepage",
        "logo_alt": "Kadir Sells – logo",
        "nav_label": "Main navigation",
        "nav_home": "Home",
        "nav_contact": "Contact",
        "lang_switch": "DE",
        "lang_switch_flag": _GLOBE,
        "lang_switch_label": "Auf Deutsch lesen",
        "f_imprint": "Legal notice",
        "f_privacy": "Privacy",
        "f_withdrawal": "Withdrawal",
        "f_contact": "Contact",
        "f_mail": "Email",
        "footer_label": "Legal and contact",
        "rights": "All rights reserved.",
        "og_locale": "en_US",
        "og_image_alt": "Mockup of the practical guide “Selling NFC review cards”",
        "skip": "Skip to content",
        "hero_switch_supplier": "Switch to the supplier product",
        "hero_switch_guide": "Switch to the practical guide",
        "img_supplier_alt": "NFC review cards supplier contact – product image",
        "img_guide_alt": "NFC review card system – the complete practical guide",
        "hero_tablist": "Choose a product",
        "tab_guide": "Practical guide",
        "tab_supplier": "Supplier only",
        "incl_vat": "incl. VAT",
        "digital_note": "Digital product, available right after purchase. The guide itself is written in German.",
        "back_home": "Back to homepage",
        "order_title": "Your order",
        "one_time": "one-time payment, no subscription",
        "buy_now": "Go to checkout",
        "seller_note": (
            "The seller and your contractual partner is Digistore24 GmbH. Digistore24’s "
            + _a(DS24["en"]["terms"], "terms and conditions")
            + " and "
            + _a(DS24["en"]["withdrawal"], "cancellation policy")
            + " apply. You receive the download link by email right after your purchase."
        ),
        "buy_footer": "Pay by credit card, direct debit, PayPal or bank transfer · Questions? DM @kadirsells on Instagram or send an email",
        "legal_eyebrow": "Legal",
    },
}

# ======================================================================= Meta-Daten

META = {
    "de": {
        "home": {
            "title": "NFC Bewertungskarten verkaufen – Praxis-Guide (PDF)",
            "description": "Der Praxis-Guide für dein NFC-Bewertungskarten-Business: Einkauf, Programmierung, Preise, Verkaufsgespräch. 80 Seiten, 9 Kapitel, inkl. Lieferantenkontakt.",
            "product_name": "NFC Bewertungskarten verkaufen – Praxis-Guide (PDF)",
        },
        "buy": {
            "title": "Guide kaufen – NFC Bewertungskarten verkaufen",
            "description": "Bestellübersicht: Praxis-Guide als PDF, 80 Seiten, für 29,99 € inkl. MwSt. Kauf über Digistore24, sofortiger Download.",
            "noindex": True,
        },
        "buysup": {
            "title": "Nur der Lieferant – NFC-Bewertungskarten Supplier-Kontakt",
            "description": "Kontakt zu meinem Lieferanten für NFC-Google-Bewertungskarten inkl. Anfrage-Vorlage, 13,99 € inkl. MwSt. Kauf über Digistore24.",
            "noindex": True,
        },
        "contact": {
            "title": "Kontakt – Kadir von Kadirsells",
            "description": "Fragen zum NFC-Bewertungskarten-Guide? Schreib mir per E-Mail oder per Instagram-DM an @kadirsells.",
        },
        "imprint": {
            "title": "Impressum – Kadirsells",
            "description": "Impressum von Kadirsells (Elyesa Kadir Yildirim), Anbieter des Praxis-Guides „NFC Bewertungskarten verkaufen“.",
        },
        "privacy": {
            "title": "Datenschutzerklärung – Kadirsells",
            "description": "Wie kadirsells.de mit personenbezogenen Daten umgeht: Hosting, Kontakt, Kauf über Digistore24, Ihre Rechte.",
        },
        "withdrawal": {
            "title": "Widerrufsrecht – Kadirsells",
            "description": "Widerruf beim Kauf des NFC-Bewertungskarten-Guides: Vertragspartner ist Digistore24, es gilt deren Widerrufsbelehrung.",
        },
    },
    "en": {
        "home": {
            "title": "Selling NFC Review Cards – Practical Guide (PDF)",
            "description": "The practical guide to starting an NFC review card business: sourcing, programming, pricing, sales talk. 80 pages, 9 chapters, incl. supplier contact.",
            "product_name": "Selling NFC Review Cards – Practical Guide (PDF, German)",
        },
        "buy": {
            "title": "Buy the guide – Selling NFC Review Cards",
            "description": "Order summary: practical guide as a PDF, 80 pages, €29.99 incl. VAT. Purchase via Digistore24, instant download.",
            "noindex": True,
        },
        "buysup": {
            "title": "Supplier only – NFC review cards supplier contact",
            "description": "Contact to my supplier for NFC Google review cards incl. inquiry template, €13.99 incl. VAT. Purchase via Digistore24.",
            "noindex": True,
        },
        "contact": {
            "title": "Contact – Kadir from Kadirsells",
            "description": "Questions about the NFC review card guide? Email me or send a DM to @kadirsells on Instagram.",
        },
        "imprint": {
            "title": "Legal notice – Kadirsells",
            "description": "Legal notice of Kadirsells (Elyesa Kadir Yildirim), publisher of the practical guide “Selling NFC review cards”.",
        },
        "privacy": {
            "title": "Privacy policy – Kadirsells",
            "description": "How kadirsells.de handles personal data: hosting, contact, purchase via Digistore24, your rights.",
        },
        "withdrawal": {
            "title": "Right of withdrawal – Kadirsells",
            "description": "Withdrawal when buying the NFC review card guide: Digistore24 is the seller, its cancellation policy applies.",
        },
    },
}

# ======================================================================= Startseite

HOME = {
    "de": {
        "hero": {
            "guide": {
                "eyebrow": "DER KOMPLETTE PRAXIS-GUIDE",
                "h1a": "NFC BEWERTUNGS-",
                "h1b": "KARTEN VERKAUFEN",
                "tagline": "BESTELLEN. PROGRAMMIEREN. VERKAUFEN.",
                "price": "29,99 €",
                "cta": "Guide kaufen",
                "counter": "1 / 2",
            },
            "lieferant": {
                "eyebrow": "KEIN GUIDE. KEIN KURS.",
                "h1a": "DER KONTAKT",
                "h1b": "ZUM LIEFERANTEN",
                "tagline": "ANFRAGEN. BESTELLEN. LOSLEGEN.",
                "price": "13,99 €",
                "cta": "Kontakt kaufen",
                "counter": "2 / 2",
            },
        },
        "problem_title": "Das Problem",
        "problem": [
            "Läden brauchen Google-Bewertungen und bekommen kaum welche.",
            "Zufriedene Kunden schreiben fast nie eine.",
            "Unzufriedene viel häufiger.",
        ],
        "solution_title": "Die Lösung",
        "solution": [
            "Der Kunde legt das Handy auf die Karte, das Bewertungsfenster öffnet sich, fertig in unter 30 Sekunden.",
            "Keine App nötig – weder für den Laden noch für den Kunden. Das klappt mit allen aktuellen iPhones und Android-Handys mit NFC.",
            "Einmalzahlung, kein Abo.",
        ],
        "google_note": "Die Karten sind für echte, freiwillige Bewertungen gedacht. Bewertungen gegen Rabatt oder Geschenk sind bei Google nicht erlaubt – im Guide zeige ich, wie Läden trotzdem mehr Bewertungen bekommen.",
        "tiles": [
            ("nfc", "Antippen.<br/>Keine App nötig."),
            ("star", "Bewerten in<br/>30 Sekunden."),
            ("trend", "Mehr Bewertungen,<br/>mehr Sichtbarkeit."),
            ("tag", "Ab 50 €<br/>Startkapital."),
        ],
        "content_title": "Inhalt",
        "content_sub": "80 Seiten, 9 Kapitel.",
        "chapters": [
            "Das Produkt verstehen.",
            "Gewerbe anmelden.",
            "Karten beschaffen.",
            "Setup und Programmierung.",
            "Preise und Pakete.",
            "Zielkunden und Tagesplanung.",
            "Das Verkaufsgespräch mit Einwandbehandlung.",
            "Übergabe und Troubleshooting.",
            "Startcheckliste und Links.",
        ],
        "bonus": "Nach dem Kauf bekommst du meinen Supplier-Kontakt per Instagram-DM (alternativ per E-Mail).",
        "faq_title": "Häufige Fragen",
        "faq": [
            ("Brauche ich Vorkenntnisse?", "Nein. Der Guide erklärt Schritt für Schritt, wie du Karten einkaufst, programmierst und an Läden verkaufst."),
            ("Was kostet der Start?", "Neben dem Guide brauchst du rund 50 € für die ersten Karten und eine Gewerbeanmeldung (je nach Gemeinde etwa 20–60 €)."),
            ("Funktionieren die Karten mit jedem Handy?", "Mit allen aktuellen iPhones und Android-Geräten mit NFC. Für ältere Handys kann ein QR-Code auf die Karte."),
            ("Brauche ich ein Gewerbe?", "Wenn du Karten regelmäßig verkaufst, ja. Kapitel 2 zeigt, wie die Anmeldung abläuft. Keine Steuer- oder Rechtsberatung."),
            ("Wie bekomme ich den Guide?", "Direkt nach dem Kauf über Digistore24 per Download-Link und E-Mail."),
            ("Kann ich den Kauf widerrufen?", "Bei digitalen Inhalten erlischt das Widerrufsrecht, sobald du im Checkout zustimmst und der Download startet. Details stehen in der Widerrufsbelehrung von Digistore24."),
            ("Ist das ein Abo?", "Nein, du zahlst einmalig 29,99 € inkl. MwSt."),
            ("Verdiene ich damit garantiert Geld?", "Nein. Wie viel du verkaufst, hängt von deinem Einsatz ab. Der Guide zeigt dir, wie ich vorgehe – inklusive meiner Fehler."),
        ],
        "about_title": "Über mich",
        "about_img_alt": "Kadir arbeitet mit dem Laptop vor einer Fensterfront mit Blick über die Stadt",
        "about": [
            "Ich bin Kadir, mit vollem Namen Elyesa Kadir Yildirim. Ich verkaufe NFC-Bewertungskarten an Läden — zu Fuß, von Tür zu Tür.",
            "Angefangen habe ich ohne Startkapital, ohne Lager, ohne Verkaufserfahrung. Ein Karton Karten und die Bereitschaft, an fremden Türen zu gehen. Mehr war da nicht.",
            "Im Guide steht alles, was ich seitdem gelernt habe. Auch die Fehler.",
        ],
        "about_cta": "Auf Instagram folgen",
    },
    "en": {
        "hero": {
            "guide": {
                "eyebrow": "THE COMPLETE PRACTICAL GUIDE",
                "h1a": "SELLING NFC",
                "h1b": "REVIEW CARDS",
                "tagline": "ORDER. PROGRAM. SELL.",
                "price": "€29.99",
                "cta": "Buy the guide",
                "counter": "1 / 2",
            },
            "lieferant": {
                "eyebrow": "NO GUIDE. NO COURSE.",
                "h1a": "THE CONTACT",
                "h1b": "TO MY SUPPLIER",
                "tagline": "ASK. ORDER. GET STARTED.",
                "price": "€13.99",
                "cta": "Buy the contact",
                "counter": "2 / 2",
            },
        },
        "problem_title": "The problem",
        "problem": [
            "Local shops need Google reviews and hardly get any.",
            "Happy customers almost never write one.",
            "Unhappy ones do much more often.",
        ],
        "solution_title": "The solution",
        "solution": [
            "The customer holds their phone to the card, the review window opens, done in under 30 seconds.",
            "No app needed – neither for the shop nor for the customer. Works with all current iPhones and Android phones with NFC.",
            "One-time payment, no subscription.",
        ],
        "google_note": "The cards are meant for genuine, voluntary reviews. Google does not allow reviews in exchange for discounts or gifts – the guide shows how shops still get more reviews.",
        "tiles": [
            ("nfc", "Tap.<br/>No app needed."),
            ("star", "Review in<br/>30 seconds."),
            ("trend", "More reviews,<br/>more visibility."),
            ("tag", "Start with<br/>about €50."),
        ],
        "content_title": "Contents",
        "content_sub": "80 pages, 9 chapters. The guide is written in German.",
        "chapters": [
            "Understanding the product.",
            "Registering a business.",
            "Sourcing the cards.",
            "Setup and programming.",
            "Prices and packages.",
            "Target customers and daily planning.",
            "The sales conversation and handling objections.",
            "Handover and troubleshooting.",
            "Starter checklist and links.",
        ],
        "bonus": "After your purchase you get my supplier contact via Instagram DM (or by email).",
        "faq_title": "FAQ",
        "faq": [
            ("Do I need any prior knowledge?", "No. The guide explains step by step how to buy, program and sell the cards to shops."),
            ("What does it cost to get started?", "Besides the guide you need about €50 for your first cards and a business registration (in Germany roughly €20–60, depending on the municipality)."),
            ("Do the cards work with every phone?", "With all current iPhones and Android phones with NFC. For older phones you can add a QR code to the card."),
            ("Do I need a registered business?", "If you sell cards regularly, yes. Chapter 2 explains the registration in Germany. This is not tax or legal advice."),
            ("How do I receive the guide?", "Right after your purchase via Digistore24, as a download link and by email."),
            ("Can I cancel my purchase?", "For digital content, the right of withdrawal expires once you agree in the checkout and the download starts. Details are in Digistore24’s cancellation policy."),
            ("Is this a subscription?", "No, you pay once: €29.99 incl. VAT."),
            ("Am I guaranteed to make money?", "No. How much you sell depends on your effort. The guide shows you how I do it – including my mistakes."),
        ],
        "about_title": "About me",
        "about_img_alt": "Kadir working on a laptop in front of a window overlooking the city",
        "about": [
            "I’m Kadir, full name Elyesa Kadir Yildirim. I sell NFC review cards to shops — on foot, door to door.",
            "I started with no starting capital, no stock and no sales experience. A box of cards and the willingness to knock on strangers’ doors. That was it.",
            "The guide contains everything I have learned since. Including the mistakes.",
        ],
        "about_cta": "Follow on Instagram",
    },
}

# ======================================================================= Kaufseiten

BUY = {
    "de": {
        "buy": {
            "img": "praxis-guide.webp",
            "img_alt": "NFC Bewertungskarten System – Produkt-Mockup",
            "name": "NFC Bewertungskarten verkaufen — Praxis-Guide",
            "sub": "PDF, 80 Seiten, 9 Kapitel. Sofort nach dem Kauf verfügbar.",
            "items": [
                "Sofortiger Download als PDF",
                "Dauerhaft nutzbar, spätere Updates des Guides inklusive",
                "Bonus: mein Supplier-Kontakt nach dem Kauf per Instagram-DM oder E-Mail",
            ],
            "price": "29,99 €",
            "checkout": CHECKOUT_GUIDE,
        },
        "buysup": {
            "img": "lieferant.webp",
            "img_alt": "NFC Bewertungskarten Supplier – Produkt-Mockup",
            "name": "Nur der Lieferant — Supplier-Kontakt",
            "sub": "Kein Guide, kein Kurs, direkter Einkauf. Anfragen. Bestellen. Loslegen.",
            "items": [
                "PDF (2 Seiten) mit dem genauen Ablauf: Kontakt, Anfrage, worauf du bei der Bestellung achtest",
                "Fertige englische Anfrage-Vorlage für den Lieferanten (Preise pro 100/200 Stück, Mindestmenge, Lieferzeit)",
                "Telefonnummer und E-Mail des Lieferanten, in der Regel innerhalb weniger Stunden, spätestens am nächsten Tag",
            ],
            "handover": [
                "<strong>So läuft die Übergabe:</strong> Die Kontaktdaten stehen aus Schutzgründen nicht im PDF. Nach dem Kauf schickst du mir einen Screenshot deiner Bestellbestätigung per Instagram-DM an @kadirsells oder per E-Mail.",
                "Der Kontakt ist zur persönlichen Nutzung bestimmt und darf nicht weitergegeben werden.",
            ],
            "price": "13,99 €",
            "checkout": CHECKOUT_SUPPLIER,
        },
    },
    "en": {
        "buy": {
            "img": "praxis-guide.webp",
            "img_alt": "NFC review card system – product mockup",
            "name": "Selling NFC review cards — practical guide",
            "sub": "PDF in German, 80 pages, 9 chapters. Available right after purchase.",
            "items": [
                "Instant PDF download",
                "Yours to keep, future updates of the guide included",
                "Bonus: my supplier contact after purchase via Instagram DM or email",
            ],
            "price": "€29.99",
            "checkout": CHECKOUT_GUIDE,
        },
        "buysup": {
            "img": "lieferant.webp",
            "img_alt": "NFC review cards supplier – product mockup",
            "name": "Supplier only — supplier contact",
            "sub": "No guide, no course, just direct purchasing. Ask. Order. Get started.",
            "items": [
                "PDF (2 pages, German) with the exact process: contact, inquiry, what to watch out for when ordering",
                "Ready-made English inquiry template for the supplier (prices per 100/200 pieces, minimum order, delivery time)",
                "The supplier’s phone number and email, usually within a few hours, at the latest the next day",
            ],
            "handover": [
                "<strong>How the handover works:</strong> For protection, the contact details are not in the PDF. After your purchase, send me a screenshot of your order confirmation via Instagram DM to @kadirsells or by email.",
                "The contact is for your personal use only and must not be passed on.",
            ],
            "price": "€13.99",
            "checkout": CHECKOUT_SUPPLIER,
        },
    },
}

# ======================================================================= Kontakt

CONTACT = {
    "de": {
        "eyebrow": "KONTAKT",
        "title": "Schreib mir.",
        "sub": "Ich antworte so schnell ich kann.",
        "mail_title": "Schreib mir per Mail",
        "ig_title": "Schreib mir auf Instagram",
        "ig_sub": "Per DM auf @kadirsells",
    },
    "en": {
        "eyebrow": "CONTACT",
        "title": "Write to me.",
        "sub": "I’ll reply as fast as I can. German or English is fine.",
        "mail_title": "Send me an email",
        "ig_title": "Message me on Instagram",
        "ig_sub": "DM @kadirsells",
    },
}

# ======================================================================= Rechtstexte
# Ein Abschnittstitel mit "!" am Anfang wird hervorgehoben dargestellt.

_IMPRINT_DE = [
    ("Angaben gemäß § 5 DDG", _p(_ADDR + "Deutschland")),
    (
        "Kontakt",
        _p(
            "E-Mail: " + _a(f"mailto:{EMAIL}", EMAIL, False),
            "Instagram: " + _a(INSTAGRAM, "@kadirsells") + " (Direktnachricht)",
        ),
    ),
    (
        "Umsatzsteuer",
        _p(
            "Kleinunternehmer gemäß § 19 UStG. Eine Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG liegt nicht vor.",
            "Die Produkte auf dieser Website verkauft die Digistore24 GmbH als Wiederverkäufer. Digistore24 berechnet die gesetzliche Umsatzsteuer. Alle angegebenen Preise sind Endpreise inklusive Mehrwertsteuer.",
        ),
    ),
    (
        "Verbraucherstreitbeilegung",
        _p("Ich bin nicht verpflichtet und nicht bereit, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen."),
    ),
    (
        "Haftung für Inhalte",
        _p(
            "Als Diensteanbieter bin ich gemäß § 7 Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG bin ich als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.",
            "Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werde ich diese Inhalte umgehend entfernen.",
        ),
    ),
    (
        "Haftung für Links",
        _p(
            "Mein Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Deshalb kann ich für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar.",
            "Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werde ich derartige Links umgehend entfernen.",
        ),
    ),
    (
        "Urheberrecht",
        _p(
            "Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.",
            "Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitte ich um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werde ich derartige Inhalte umgehend entfernen.",
        ),
    ),
]

_IMPRINT_EN = [
    ("Information pursuant to § 5 DDG (German Digital Services Act)", _p(_ADDR + "Germany")),
    (
        "Contact",
        _p(
            "Email: " + _a(f"mailto:{EMAIL}", EMAIL, False),
            "Instagram: " + _a(INSTAGRAM, "@kadirsells") + " (direct message)",
        ),
    ),
    (
        "VAT",
        _p(
            "Small business pursuant to § 19 UStG (German VAT Act). There is no VAT identification number pursuant to § 27a UStG.",
            "The products on this website are sold by Digistore24 GmbH as a reseller. Digistore24 charges the statutory VAT. All prices shown are final prices including VAT.",
        ),
    ),
    (
        "Consumer dispute resolution",
        _p("I am neither obliged nor willing to take part in dispute resolution proceedings before a consumer arbitration board."),
    ),
    (
        "Liability for content",
        _p(
            "As a service provider I am responsible for my own content on these pages under general law pursuant to § 7 (1) DDG. Under §§ 8 to 10 DDG, however, I am not obliged to monitor third-party information transmitted or stored, or to investigate circumstances that indicate illegal activity.",
            "Obligations to remove or block the use of information under general law remain unaffected. Liability in this respect is only possible from the moment a specific infringement becomes known. If I become aware of such infringements, I will remove the content immediately.",
        ),
    ),
    (
        "Liability for links",
        _p(
            "My website contains links to external third-party websites whose content I have no influence on. I therefore cannot accept any liability for this external content. The respective provider or operator of the linked pages is always responsible for their content. The linked pages were checked for possible legal violations at the time of linking. No illegal content was apparent at that time.",
            "Permanent monitoring of the linked pages is not reasonable without concrete evidence of an infringement. If I become aware of infringements, I will remove such links immediately.",
        ),
    ),
    (
        "Copyright",
        _p(
            "The content and works created by the site operator on these pages are subject to German copyright law. Reproduction, editing, distribution and any kind of use beyond the limits of copyright law require the written consent of the respective author or creator. Downloads and copies of this site are permitted for private, non-commercial use only.",
            "Where content on this site was not created by the operator, the copyrights of third parties are respected and third-party content is marked as such. Should you nevertheless notice a copyright infringement, please let me know. If I become aware of infringements, I will remove such content immediately.",
        ),
    ),
]

_PRIVACY_DE = [
    (
        "Verantwortlicher",
        _p(
            "Verantwortlich für die Datenverarbeitung auf dieser Website ist:",
            _ADDR + "Deutschland<br/>E-Mail: " + _a(f"mailto:{EMAIL}", EMAIL, False),
            "Ein Datenschutzbeauftragter ist nicht bestellt, da die gesetzlichen Voraussetzungen hierfür nicht vorliegen.",
        ),
    ),
    (
        "Allgemeines zur Datenverarbeitung",
        _p(
            "Ich verarbeite personenbezogene Daten nur, soweit dies zur Bereitstellung einer funktionsfähigen Website sowie meiner Inhalte und Leistungen erforderlich ist oder Sie eingewilligt haben.",
            "Rechtsgrundlagen sind je nach Fall:",
        )
        + _ul(
            "Art. 6 Abs. 1 lit. a DSGVO – Ihre Einwilligung",
            "Art. 6 Abs. 1 lit. b DSGVO – Vertragserfüllung oder vorvertragliche Maßnahmen",
            "Art. 6 Abs. 1 lit. f DSGVO – berechtigtes Interesse",
        ),
    ),
    (
        "Hosting",
        _p(
            "Diese Website wird über GitHub Pages bereitgestellt. Anbieter ist die GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA.",
            "Beim Aufruf der Website verarbeitet GitHub die unter Ziffer 4 genannten technischen Daten, um die Seiten auszuliefern und die Sicherheit des Dienstes zu gewährleisten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO – mein berechtigtes Interesse an einer sicheren, schnellen und zuverlässigen Bereitstellung dieser Website.",
            "Datenübermittlung in die USA: GitHub ist unter dem EU-US Data Privacy Framework zertifiziert (Angemessenheitsbeschluss der EU-Kommission nach Art. 45 DSGVO). Näheres in der Datenschutzerklärung von GitHub: "
            + _a("https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement", "GitHub General Privacy Statement"),
        ),
    ),
    (
        "Server-Logfiles",
        _p("Beim Aufruf dieser Website erhebt GitHub automatisch Informationen, die Ihr Browser übermittelt:")
        + _ul(
            "IP-Adresse",
            "Browsertyp und Browserversion",
            "verwendetes Betriebssystem",
            "Referrer-URL",
            "aufgerufene Seiten",
            "Uhrzeit der Serveranfrage",
        )
        + _p(
            "Laut GitHub wird die IP-Adresse der Besucher von GitHub-Pages-Seiten aus Sicherheitsgründen protokolliert und gespeichert. Ich selbst habe keinen Zugriff auf diese Daten und werte sie nicht aus. Sie werden nicht mit anderen Datenquellen zusammengeführt. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (technischer Betrieb und Angriffsabwehr)."
        ),
    ),
    (
        "Kontaktaufnahme",
        _p(
            "Auf dieser Website befindet sich kein Kontaktformular. Beim Aufruf der Seite werden keine Kontaktdaten von Ihnen erhoben. Wenn Sie mich erreichen möchten, stehen Ihnen zwei Wege offen:",
            "<strong>Kontakt per E-Mail</strong>",
            "Wenn Sie mir eine E-Mail schreiben, werden Ihre Angaben inklusive der von Ihnen angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall von Anschlussfragen bei mir gespeichert. Diese Daten gebe ich nicht ohne Ihre Einwilligung weiter.",
            "Die Verarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Anbahnung oder Erfüllung eines Vertrags zusammenhängt. In allen übrigen Fällen beruht die Verarbeitung auf meinem berechtigten Interesse an der effektiven Bearbeitung der an mich gerichteten Anfragen (Art. 6 Abs. 1 lit. f DSGVO).",
            "Mein E-Mail-Postfach wird betrieben von Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland. Eine Übermittlung von Daten in die USA kann dabei nicht ausgeschlossen werden.",
            "Ihre Nachrichten verbleiben bei mir, bis Sie mich zur Löschung auffordern oder der Zweck der Speicherung entfällt. Zwingende gesetzliche Aufbewahrungsfristen bleiben unberührt.",
            "<strong>Kontakt über Instagram</strong>",
            "Wenn Sie mir über Instagram eine Nachricht schreiben, erfolgt die Verarbeitung Ihrer Daten durch Meta Platforms Ireland Limited nach deren Datenschutzbestimmungen. Näheres dazu unter Ziffer 7.",
        ),
    ),
    (
        "Schriftarten und Bilder",
        _p(
            "Alle Schriftarten und Bilder dieser Website liegen auf demselben Server wie die Website selbst. Beim Aufruf der Seite wird keine Verbindung zu Google Fonts, Bilder-Speicherdiensten oder anderen Drittanbietern aufgebaut."
        ),
    ),
    (
        "Instagram",
        _p(
            "<strong>Verlinkung</strong>",
            "Auf dieser Website befinden sich Verweise auf mein Instagram-Profil (@kadirsells). Es handelt sich dabei um einfache Links, nicht um eingebettete Social-Media-Plugins. Beim bloßen Aufruf dieser Website werden daher keine Daten an Instagram übertragen.",
            "Erst wenn Sie den Link aktiv anklicken, werden Sie auf die Seiten von Instagram weitergeleitet. Ab diesem Zeitpunkt gilt die Datenschutzerklärung des Anbieters: Meta Platforms Ireland Limited, Merrion Road, Dublin 4, Irland.",
            "<strong>Mein Instagram-Profil</strong>",
            "Ich betreibe das Profil @kadirsells. Wenn Sie es besuchen, verarbeitet Meta Platforms Ireland Limited Ihre Daten auch für Statistiken, die mir in anonymisierter Form angezeigt werden („Insights“). Für diese Statistiken sind Meta und ich gemeinsam verantwortlich (Art. 26 DSGVO). Meta hat sich verpflichtet, die Hauptverantwortung für die Verarbeitung und die Erfüllung Ihrer Rechte zu übernehmen: "
            + _a("https://www.facebook.com/legal/terms/information_about_page_insights_data", "Informationen zu Seiten-Insights"),
        ),
    ),
    (
        "Bestellabwicklung über Digistore24",
        _p(
            "Der Kauf meiner digitalen Produkte (Guide und Lieferantenkontakt) findet nicht auf dieser Website statt. Beim Klick auf den Kaufen-Button werden Sie zu meinem Vertriebspartner weitergeleitet:",
            "Digistore24 GmbH, St.-Godehard-Straße 32, 31139 Hildesheim, Deutschland",
            "Digistore24 tritt als Wiederverkäufer auf und wird damit Ihr Vertragspartner. Alle im Bestellprozess eingegebenen Daten – insbesondere Name, Anschrift, E-Mail-Adresse und Zahlungsdaten – werden ausschließlich von Digistore24 erhoben und verarbeitet. Ich erhalte lediglich die zur Auslieferung und Abrechnung erforderlichen Angaben.",
            "Es gilt insoweit die Datenschutzerklärung von Digistore24: " + _a(DS24["de"]["privacy"], DS24["de"]["privacy"]),
        ),
    ),
    (
        "Übermittlung des Lieferantenkontakts nach dem Kauf",
        _p(
            "Beim Produkt „Kontakt zum Lieferanten“ und beim Bonus zum Guide erhalten Sie die Kontaktdaten des Lieferanten nicht automatisch, sondern persönlich von mir. Dazu senden Sie mir nach dem Kauf über Instagram-Direktnachricht oder per E-Mail einen Nachweis Ihres Kaufs (z. B. Screenshot der Bestellbestätigung).",
            "Dabei verarbeite ich die in diesem Nachweis enthaltenen Daten – in der Regel Ihr Instagram-Profil bzw. Ihre E-Mail-Adresse, Ihre Bestellnummer und ggf. Ihren Namen aus der Bestellbestätigung – ausschließlich zur Prüfung des Kaufs und zur Übermittlung des Lieferantenkontakts. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Vertragserfüllung).",
            "Bei einer Instagram-Nachricht gelten zusätzlich die Datenschutzbestimmungen von Meta Platforms Ireland Limited (siehe Ziffer 7), bei einer E-Mail die Hinweise unter Ziffer 5.",
            "Den Nachweis bewahre ich nur so lange auf, wie es zur Abwicklung und zum Nachweis der Erfüllung erforderlich ist. Zwingende gesetzliche Aufbewahrungsfristen bleiben unberührt.",
        ),
    ),
    (
        "Cookies und Analyse",
        _p(
            "Diese Website setzt keine Cookies und speichert nichts in Ihrem Browser. Es gibt kein Tracking, keine Analyse-Tools und keine Werbe-Pixel. Ihr Nutzungsverhalten wird nicht ausgewertet."
        ),
    ),
    (
        "Ihre Rechte",
        _p("Sie haben jederzeit das Recht:")
        + _ul(
            "Auskunft über Ihre gespeicherten Daten zu verlangen (Art. 15 DSGVO)",
            "Berichtigung unrichtiger Daten zu verlangen (Art. 16 DSGVO)",
            "Löschung Ihrer Daten zu verlangen (Art. 17 DSGVO)",
            "die Einschränkung der Verarbeitung zu verlangen (Art. 18 DSGVO)",
            "Datenübertragbarkeit zu verlangen (Art. 20 DSGVO)",
            "der Verarbeitung zu widersprechen (Art. 21 DSGVO, siehe Ziffer 12)",
            "eine erteilte Einwilligung jederzeit zu widerrufen (Art. 7 Abs. 3 DSGVO)",
        )
        + _p(
            "Wenden Sie sich dafür formlos an die oben genannte E-Mail-Adresse.",
            "<strong>Beschwerderecht bei der Aufsichtsbehörde</strong>",
            "Unabhängig davon steht Ihnen ein Beschwerderecht bei einer Datenschutz-Aufsichtsbehörde zu. Die für mich zuständige Behörde ist:",
            "Bayerisches Landesamt für Datenschutzaufsicht (BayLDA)<br/>Promenade 27<br/>91522 Ansbach<br/>" + _a("https://www.lda.bayern.de", "www.lda.bayern.de"),
        ),
    ),
    (
        "!Widerspruchsrecht nach Art. 21 DSGVO",
        _p(
            "<strong>Soweit ich Ihre Daten auf Grundlage meines berechtigten Interesses verarbeite (Art. 6 Abs. 1 lit. f DSGVO), haben Sie das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit Widerspruch einzulegen. Ich verarbeite die Daten dann nicht mehr, es sei denn, ich kann zwingende schutzwürdige Gründe nachweisen oder die Verarbeitung dient der Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen. Ein formloser Widerspruch an "
            + _a(f"mailto:{EMAIL}", EMAIL, False)
            + " genügt.</strong>"
        ),
    ),
    (
        "SSL-/TLS-Verschlüsselung",
        _p("Diese Seite nutzt aus Sicherheitsgründen eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie daran, dass die Adresszeile des Browsers mit „https://“ beginnt."),
    ),
    (
        "Keine automatisierte Entscheidungsfindung",
        _p("Eine automatisierte Entscheidungsfindung einschließlich Profiling gemäß Art. 22 DSGVO findet nicht statt."),
    ),
    (
        "Änderungen dieser Datenschutzerklärung",
        _p("Ich behalte mir vor, diese Datenschutzerklärung anzupassen, damit sie stets den aktuellen rechtlichen Anforderungen entspricht oder um Änderungen meiner Leistungen umzusetzen."),
    ),
]

_PRIVACY_EN = [
    (
        "Controller",
        _p(
            "The controller responsible for data processing on this website is:",
            _ADDR + "Germany<br/>Email: " + _a(f"mailto:{EMAIL}", EMAIL, False),
            "No data protection officer has been appointed, as the legal requirements for this are not met.",
        ),
    ),
    (
        "General information on data processing",
        _p(
            "I only process personal data to the extent necessary to provide a functioning website and my content and services, or where you have given consent.",
            "Depending on the case, the legal bases are:",
        )
        + _ul(
            "Art. 6 (1) (a) GDPR – your consent",
            "Art. 6 (1) (b) GDPR – performance of a contract or pre-contractual measures",
            "Art. 6 (1) (f) GDPR – legitimate interest",
        ),
    ),
    (
        "Hosting",
        _p(
            "This website is provided via GitHub Pages. The provider is GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA.",
            "When you visit the website, GitHub processes the technical data listed in section 4 in order to deliver the pages and keep the service secure. The legal basis is Art. 6 (1) (f) GDPR – my legitimate interest in providing this website securely, quickly and reliably.",
            "Transfer of data to the USA: GitHub is certified under the EU-US Data Privacy Framework (adequacy decision of the EU Commission under Art. 45 GDPR). More details in GitHub’s privacy statement: "
            + _a("https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement", "GitHub General Privacy Statement"),
        ),
    ),
    (
        "Server log files",
        _p("When you visit this website, GitHub automatically collects information that your browser transmits:")
        + _ul(
            "IP address",
            "browser type and version",
            "operating system",
            "referrer URL",
            "pages visited",
            "time of the server request",
        )
        + _p(
            "According to GitHub, the IP addresses of visitors to GitHub Pages sites are logged and stored for security purposes. I have no access to this data myself and do not analyse it. It is not combined with other data sources. The legal basis is Art. 6 (1) (f) GDPR (technical operation and defence against attacks)."
        ),
    ),
    (
        "Contacting me",
        _p(
            "There is no contact form on this website. No contact data is collected when you visit the site. If you want to reach me, there are two ways:",
            "<strong>Contact by email</strong>",
            "If you send me an email, your details including the contact data you provide will be stored by me for the purpose of handling your request and in case of follow-up questions. I will not pass on this data without your consent.",
            "Processing is based on Art. 6 (1) (b) GDPR if your request relates to the conclusion or performance of a contract. In all other cases, processing is based on my legitimate interest in handling requests addressed to me effectively (Art. 6 (1) (f) GDPR).",
            "My mailbox is operated by Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Ireland. A transfer of data to the USA cannot be ruled out.",
            "Your messages remain with me until you ask me to delete them or the purpose of storage no longer applies. Mandatory statutory retention periods remain unaffected.",
            "<strong>Contact via Instagram</strong>",
            "If you send me a message via Instagram, your data is processed by Meta Platforms Ireland Limited in accordance with its privacy policy. See section 7 for details.",
        ),
    ),
    (
        "Fonts and images",
        _p(
            "All fonts and images on this website are hosted on the same server as the website itself. No connection is made to Google Fonts, image storage services or any other third party when you visit the site."
        ),
    ),
    (
        "Instagram",
        _p(
            "<strong>Links</strong>",
            "This website contains links to my Instagram profile (@kadirsells). These are simple links, not embedded social media plugins. Merely visiting this website therefore does not transmit any data to Instagram.",
            "Only when you actively click the link are you forwarded to Instagram. From that point on, the provider’s privacy policy applies: Meta Platforms Ireland Limited, Merrion Road, Dublin 4, Ireland.",
            "<strong>My Instagram profile</strong>",
            "I run the profile @kadirsells. When you visit it, Meta Platforms Ireland Limited also processes your data for statistics that are shown to me in anonymised form (“Insights”). Meta and I are joint controllers for these statistics (Art. 26 GDPR). Meta has undertaken to assume primary responsibility for the processing and for fulfilling your rights: "
            + _a("https://www.facebook.com/legal/terms/information_about_page_insights_data", "Page Insights information"),
        ),
    ),
    (
        "Order processing via Digistore24",
        _p(
            "The purchase of my digital products (guide and supplier contact) does not take place on this website. When you click the buy button, you are forwarded to my sales partner:",
            "Digistore24 GmbH, St.-Godehard-Straße 32, 31139 Hildesheim, Germany",
            "Digistore24 acts as a reseller and thus becomes your contractual partner. All data entered during the ordering process – in particular name, address, email address and payment data – is collected and processed exclusively by Digistore24. I only receive the information required for delivery and accounting.",
            "Digistore24’s privacy policy applies: " + _a(DS24["en"]["privacy"], DS24["en"]["privacy"]),
        ),
    ),
    (
        "Handing over the supplier contact after purchase",
        _p(
            "For the product “Supplier contact” and for the guide’s bonus, you do not receive the supplier’s contact details automatically, but personally from me. To do so, send me proof of purchase after buying (e.g. a screenshot of the order confirmation) via Instagram direct message or by email.",
            "I process the data contained in this proof – usually your Instagram profile or email address, your order number and, if applicable, your name from the order confirmation – solely to verify the purchase and to hand over the supplier contact. The legal basis is Art. 6 (1) (b) GDPR (performance of a contract).",
            "For an Instagram message, Meta Platforms Ireland Limited’s privacy policy also applies (see section 7); for an email, see section 5.",
            "I keep the proof only as long as necessary for processing and for proving fulfilment. Mandatory statutory retention periods remain unaffected.",
        ),
    ),
    (
        "Cookies and analytics",
        _p(
            "This website does not set any cookies and does not store anything in your browser. There is no tracking, no analytics tools and no advertising pixels. Your usage behaviour is not analysed."
        ),
    ),
    (
        "Your rights",
        _p("You have the right at any time to:")
        + _ul(
            "request information about your stored data (Art. 15 GDPR)",
            "request correction of incorrect data (Art. 16 GDPR)",
            "request deletion of your data (Art. 17 GDPR)",
            "request restriction of processing (Art. 18 GDPR)",
            "request data portability (Art. 20 GDPR)",
            "object to processing (Art. 21 GDPR, see section 12)",
            "withdraw consent at any time (Art. 7 (3) GDPR)",
        )
        + _p(
            "To do so, simply contact me at the email address above.",
            "<strong>Right to lodge a complaint with a supervisory authority</strong>",
            "You also have the right to lodge a complaint with a data protection supervisory authority. The authority responsible for me is:",
            "Bayerisches Landesamt für Datenschutzaufsicht (BayLDA)<br/>Promenade 27<br/>91522 Ansbach, Germany<br/>" + _a("https://www.lda.bayern.de", "www.lda.bayern.de"),
        ),
    ),
    (
        "!Right to object under Art. 21 GDPR",
        _p(
            "<strong>Where I process your data on the basis of my legitimate interest (Art. 6 (1) (f) GDPR), you have the right to object at any time on grounds relating to your particular situation. I will then no longer process the data unless I can demonstrate compelling legitimate grounds or the processing serves the establishment, exercise or defence of legal claims. An informal objection to "
            + _a(f"mailto:{EMAIL}", EMAIL, False)
            + " is sufficient.</strong>"
        ),
    ),
    (
        "SSL/TLS encryption",
        _p("For security reasons this site uses SSL/TLS encryption. You can recognise an encrypted connection by the browser’s address bar starting with “https://”."),
    ),
    (
        "No automated decision-making",
        _p("There is no automated decision-making, including profiling, pursuant to Art. 22 GDPR."),
    ),
    (
        "Changes to this privacy policy",
        _p("I reserve the right to amend this privacy policy so that it always complies with current legal requirements or to reflect changes to my services."),
    ),
]

_WITHDRAWAL_DE = [
    (
        "Ihr Vertragspartner ist Digistore24",
        _p(
            "Die Produkte auf dieser Website (Praxis-Guide und Lieferantenkontakt) verkaufe ich nicht selbst. Verkäufer und Ihr Vertragspartner ist die Digistore24 GmbH, St.-Godehard-Straße 32, 31139 Hildesheim, Deutschland.",
            "Für Ihren Kauf gilt deshalb ausschließlich die Widerrufsbelehrung von Digistore24. Sie wird Ihnen im Bestellprozess angezeigt und mit der Bestellbestätigung per E-Mail zugesandt.",
            _a(DS24["de"]["withdrawal"], "Widerrufsbelehrung von Digistore24 lesen") + " · " + _a(DS24["de"]["terms"], "AGB von Digistore24"),
        ),
    ),
    (
        "Digitale Inhalte",
        _p(
            "Als Verbraucher haben Sie grundsätzlich ein Widerrufsrecht von 14 Tagen. Bei digitalen Inhalten wie einer PDF erlischt es vorzeitig, wenn Sie im Checkout ausdrücklich zustimmen, dass Digistore24 vor Ablauf der Widerrufsfrist mit der Ausführung beginnt, und Sie bestätigen, dass Sie dadurch Ihr Widerrufsrecht verlieren (§ 356 Abs. 5 BGB).",
            "Diese Zusammenfassung dient nur der Orientierung. Maßgeblich ist allein die Widerrufsbelehrung von Digistore24.",
        ),
    ),
    (
        "So widerrufen Sie",
        _p(
            "Richten Sie Ihren Widerruf bitte direkt an Digistore24: " + _a(DS24["de"]["contact"], "Kontakt zu Digistore24") + ". Die Kontaktdaten stehen auch in Ihrer Bestellbestätigung.",
            "Bei Fragen helfe ich gern weiter: " + _a(f"mailto:{EMAIL}", EMAIL, False) + " oder per Instagram-DM an " + _a(INSTAGRAM, "@kadirsells") + ".",
        ),
    ),
]

_WITHDRAWAL_EN = [
    (
        "Your contractual partner is Digistore24",
        _p(
            "I do not sell the products on this website (practical guide and supplier contact) myself. The seller and your contractual partner is Digistore24 GmbH, St.-Godehard-Straße 32, 31139 Hildesheim, Germany.",
            "Only Digistore24’s cancellation policy therefore applies to your purchase. It is shown to you during checkout and sent to you by email with your order confirmation.",
            _a(DS24["en"]["withdrawal"], "Read Digistore24’s cancellation policy") + " · " + _a(DS24["en"]["terms"], "Digistore24 terms and conditions"),
        ),
    ),
    (
        "Digital content",
        _p(
            "As a consumer in the EU you generally have a 14-day right of withdrawal. For digital content such as a PDF, it expires early if you expressly agree in the checkout that Digistore24 may begin performance before the withdrawal period ends, and you acknowledge that you thereby lose your right of withdrawal (§ 356 (5) German Civil Code).",
            "This summary is for orientation only. Only Digistore24’s cancellation policy is binding.",
        ),
    ),
    (
        "How to withdraw",
        _p(
            "Please send your withdrawal directly to Digistore24: " + _a(DS24["en"]["contact"], "contact Digistore24") + ". The contact details are also in your order confirmation.",
            "If you have questions, I’m happy to help: " + _a(f"mailto:{EMAIL}", EMAIL, False) + " or via Instagram DM to " + _a(INSTAGRAM, "@kadirsells") + ".",
        ),
    ),
]

_EN_NOTE = "This is a courtesy translation. Only the German version is legally binding."

LEGAL = {
    "de": {
        "imprint": {"title": "Impressum", "sub": "Angaben gemäß § 5 DDG.", "sections": _IMPRINT_DE, "stand": "Stand: Oktober 2026"},
        "privacy": {"title": "Datenschutz", "sub": "Datenschutzerklärung nach der Datenschutz-Grundverordnung (DSGVO).", "sections": _PRIVACY_DE, "stand": "Stand: Oktober 2026"},
        "withdrawal": {"title": "Widerrufsrecht", "sub": "Was beim Widerruf Ihrer Bestellung gilt.", "sections": _WITHDRAWAL_DE, "stand": "Stand: Oktober 2026"},
    },
    "en": {
        "imprint": {"title": "Legal notice", "sub": "Information pursuant to § 5 DDG (Impressum).", "note": _EN_NOTE, "sections": _IMPRINT_EN, "stand": "Last updated: October 2026"},
        "privacy": {"title": "Privacy", "sub": "Privacy policy under the General Data Protection Regulation (GDPR).", "note": _EN_NOTE, "sections": _PRIVACY_EN, "stand": "Last updated: October 2026"},
        "withdrawal": {"title": "Right of withdrawal", "sub": "What applies if you want to cancel your order.", "note": _EN_NOTE, "sections": _WITHDRAWAL_EN, "stand": "Last updated: October 2026"},
    },
}
