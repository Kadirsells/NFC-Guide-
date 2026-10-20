# NFC Guide – kadirsells.de

## Neue Website (`docs/`)

Statischer Nachbau der Lovable-Seite mit gleichem Design, korrigierten Rechtstexten, Deutsch und Englisch, Sitemap und SEO.
Vorschau: https://eliyah-kernseite.github.io/NFC-Guide-/ (nach dem Einschalten von GitHub Pages, siehe [ANLEITUNG.md](ANLEITUNG.md)).

| Ordner | Inhalt |
| --- | --- |
| `docs/` | Fertige Website, wird von GitHub Pages ausgeliefert |
| `tools/content.py` | Alle Texte, Deutsch und Englisch |
| `tools/build_site.py` | Baut `docs/` neu: `python3 tools/build_site.py` |
| `tools/static/` | Zusatz-CSS und JavaScript |
| `live-2026-10-20/` | Unveränderte Kopie der Live-Seite vom 20.10.2026 |
| `bestand-2026-10-20/` | PDF-Export der Live-Seite vom 20.10.2026 |


Website zum Verkauf des Praxis-Guides „NFC Bewertungskarten verkaufen“ (gebaut und gehostet mit Lovable, Verkauf über Digistore24).

## bestand-2026-10-20/

Unveränderter Stand der Live-Seite vom 20.10.2026, als PDF aus Safari exportiert, plus der daraus extrahierte Text. Der Quellcode der Lovable-Seite liegt noch nicht vor.

| Seite | PDF | Text |
| --- | --- | --- |
| Startseite | pdf/startseite.pdf | text/startseite.txt |
| Guide kaufen | pdf/guide-kaufen.pdf | text/guide-kaufen.txt |
| Kontakt | pdf/kontakt.pdf | text/kontakt.txt |
| Impressum | pdf/impressum.pdf | text/impressum.txt |
| Datenschutz | pdf/datenschutz.pdf | text/datenschutz.txt |

Die Prüfung (Recht und SEO) liegt als separates Dokument vor.

### bilder-aus-pdf/

Bilder, die aus den PDFs extrahiert wurden (Übergangslösung, bis die Originaldateien von der Live-Seite vorliegen): Logo (160 px, transparent), Mockup Praxis-Guide (1920 px), Mockup Lieferantenkontakt (864 px), Foto Kadir (364 px). Die Auflösung entspricht dem, was Safari ins PDF geschrieben hat, nicht zwingend dem Original.
