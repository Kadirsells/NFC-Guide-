# Live-Kopie kadirsells.de – Stand 2026-10-20

Unveränderte Kopie der Live-Seite https://kadirsells.de, heruntergeladen am 2026-10-20 (ca. 19:05 UTC).
Gebaut und gehostet mit Lovable (React + TanStack Start, server-gerendert, Tailwind). Noch nichts verbessert.

## Inhalt

- `TEXTE.md` – alle sichtbaren Texte, Titel, Meta-Tags, Bilder (mit Alt-Text) und Links jeder Seite, aus dem HTML extrahiert.
- `site/` – die Seite 1:1 wie vom Server ausgeliefert (gleiche Pfade wie online):
  - `index.html` (/), `kaufen/`, `kaufen-kontakt/`, `kontakt/`, `impressum/`, `datenschutz/`, `widerruf/` – je `index.html`
  - `assets/` – JS-Bundle (`index-*.js` + eine Datei pro Seite), CSS, Schriften (Archivo, Inter, JetBrains Mono), Lieferanten-Bild (webp)
  - `__l5e/assets-v1/…` – Logo (`logo-ks-new.png`), Guide-Mockup (`der-komplette-praxis-guide-5.png`), Lieferanten-Mockup (`nfc-supplier.png`), Foto (`kadir.jpeg`), Lovable-Tracking-Skript
  - `robots.txt`, `favicon.png`, `~flock.js` (Lovable-Analytics)
- `extern/pub-…r2.dev/…png` – Social-Share-Bild (og:image / twitter:image)
- `download-log.json` – jede abgerufene URL mit HTTP-Status und Größe

## Seiten (Routen aus dem JS-Bundle)

`/`, `/kaufen`, `/kaufen-kontakt`, `/kontakt`, `/impressum`, `/datenschutz`, `/widerruf`

## Externe Ziele

- Kauf Guide (29,99 €): https://www.checkout-ds24.com/product/721214
- Kauf „Nur der Lieferant“ (13,99 €): https://www.checkout-ds24.com/product/728685
- Instagram: https://instagram.com/kadirsells · Mail: elyesakadiryildirim@gmail.com

## Beim Kopieren aufgefallen (nur notiert, nichts geändert)

- **„28 Seiten“** steht in der Startseiten-Meta-Description sowie in `og:description` und `twitter:description` (`site/index.html`) und als Standard-Description im Haupt-Bundle (`site/assets/index-*.js`). Auf der Seite selbst steht „80 Seiten“ (Startseite „Inhalt“, `/kaufen`).
- `sitemap.xml` gibt es nicht (404). `robots.txt` erlaubt alles.
- `/widerruf` existiert, ist aber im Footer nicht verlinkt.
- `/kaufen` und `/kaufen-kontakt` zeigen „Kleinunternehmer gemäß § 19 UStG“, obwohl über Digistore24 verkauft wird.
- `<html lang="en">`, obwohl die Seite deutsch ist.
- www.kadirsells.de ist nicht erreichbar, nur kadirsells.de.
