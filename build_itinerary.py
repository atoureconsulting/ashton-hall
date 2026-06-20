#!/usr/bin/env python3
# Builds the Ashton Hall Africa Tour itinerary with a toggle between
# Foundation (10 nights) and With Benin (12 nights).
#
# SETUP: Before running, make sure the source file exists:
#   cp /home/user/website/ashton-hall-itinerary.html /home/user/itinerary_v4.html
# (used only to extract the embedded Atoure logo)
#
# OUTPUT: /home/user/itinerary_v5.html
# DEPLOY: cp /home/user/itinerary_v5.html /home/user/website/ashton-hall-itinerary.html
#         then git add/commit/push from /home/user/website
import re, datetime

SRC = "/home/user/itinerary_v4.html"
OUT = "/home/user/itinerary_v5.html"

v4 = open(SRC, encoding="utf-8").read()
m = re.search(r'class="logo-mono" src="(data:image/png;base64,[^"]+)"', v4)
LOGO = m.group(1)

FLAGS = {
 "Nigeria":'<rect width="20" height="40" fill="#008751"/><rect x="20" width="20" height="40" fill="#fff"/><rect x="40" width="20" height="40" fill="#008751"/>',
 "Ghana":'<rect width="60" height="13.33" fill="#ce1126"/><rect y="13.33" width="60" height="13.34" fill="#fcd116"/><rect y="26.67" width="60" height="13.33" fill="#006b3f"/><polygon points="30.00,14.00 31.47,17.98 35.71,18.15 32.38,20.77 33.53,24.85 30.00,22.50 26.47,24.85 27.62,20.77 24.29,18.15 28.53,17.98" fill="#000"/>',
 "Ivory Coast":'<rect width="20" height="40" fill="#f77f00"/><rect x="20" width="20" height="40" fill="#fff"/><rect x="40" width="20" height="40" fill="#009e60"/>',
 "Morocco":'<rect width="60" height="40" fill="#c1272d"/><polygon points="30,12 33.53,22.85 24.29,16.15 35.71,16.15 26.47,22.85" fill="none" stroke="#006233" stroke-width="1.4"/>',
 "Cameroon":'<rect width="20" height="40" fill="#007a5e"/><rect x="20" width="20" height="40" fill="#ce1126"/><rect x="40" width="20" height="40" fill="#fcd116"/><polygon points="30.00,14.00 31.47,17.98 35.71,18.15 32.38,20.77 33.53,24.85 30.00,22.50 26.47,24.85 27.62,20.77 24.29,18.15 28.53,17.98" fill="#fcd116"/>',
 "Senegal":'<rect width="20" height="40" fill="#00853f"/><rect x="20" width="20" height="40" fill="#fdef42"/><rect x="40" width="20" height="40" fill="#e31b23"/><polygon points="30.00,14.00 31.47,17.98 35.71,18.15 32.38,20.77 33.53,24.85 30.00,22.50 26.47,24.85 27.62,20.77 24.29,18.15 28.53,17.98" fill="#00853f"/>',
 "Benin":'<rect width="24" height="40" fill="#008751"/><rect x="24" width="36" height="20" fill="#fcd116"/><rect x="24" y="20" width="36" height="20" fill="#e8112d"/>',
 "Ethiopia":'<rect width="60" height="13.33" fill="#078930"/><rect y="13.33" width="60" height="13.34" fill="#fcdd09"/><rect y="26.67" width="60" height="13.33" fill="#da121a"/><circle cx="30" cy="20" r="9" fill="#0f47af"/><polygon points="30.00,13.50 31.59,17.82 36.18,17.99 32.57,20.83 33.82,25.26 30.00,22.70 26.18,25.26 27.43,20.83 23.82,17.99 28.41,17.82" fill="#fcdd09"/>',
}
BORDER='<rect x="0.5" y="0.5" width="59" height="39" fill="none" stroke="rgba(0,0,0,.18)"/>'

def flag(country, w, h):
    return (f'<svg class="flag" width="{w}" height="{h}" viewBox="0 0 60 40" '
            f'xmlns="http://www.w3.org/2000/svg">{FLAGS[country]}{BORDER}</svg>')

AIRPORTS = {
 "Nigeria":("Lagos","Murtala Muhammed International Airport","LOS"),
 "Ghana":("Accra","Kotoka International Airport","ACC"),
 "Ivory Coast":("Abidjan","F&eacute;lix-Houphou&euml;t-Boigny International Airport","ABJ"),
 "Morocco":("Marrakech","Marrakesh Menara Airport","RAK"),
 "Cameroon":("Douala","Douala International Airport","DLA"),
 "Senegal":("Dakar","Blaise Diagne International Airport","DSS"),
 "Benin":("Cotonou","Cadjehoun Airport","COO"),
 "Ethiopia":("Addis Ababa","Bole International Airport","ADD"),
}

DOW = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def dlabel(d): return f"{d.day} {d.strftime('%b')} &middot; {DOW[d.weekday()]}"
def daterange_label(start, end):
    if start.month == end.month: return f"{start.day} to {end.day} {end.strftime('%b')}"
    return f"{start.day} {start.strftime('%b')} to {end.day} {end.strftime('%b')}"

TBC = '<span class="tbc">TBC</span>'

def arrival_day(daynum, date, country, prev, first, tbc):
    city, airport, code = AIRPORTS[country]
    if first:
        fl = (f'<li><b>20:00&ndash;21:00</b> &mdash; International arrival at {airport} ({code}), {city}, {country}. Airline and flight number {TBC}.</li>')
    else:
        fl = (f'<li><b>20:00</b> &mdash; Flight {prev} to {city}, {country}. Arriving at {airport} ({code}). Airline and flight number {TBC}. Estimated arrival 20:00 local.</li>')
    chip = '<span class="chip chip-arrival">&#9992; Arrival</span>'
    if tbc: chip += ' <span class="chip chip-tbc">&#9711; Pending</span>'
    return (f'<div class="day arrival"><div class="dot"></div><div class="day-body">'
            f'<div class="day-top"><span class="day-label">Day {daynum} &middot; {dlabel(date)}</span>{chip}</div>'
            f'<div class="day-title">Travel and arrival</div><ul class="day-items">'
            f'{fl}'
            f'<li><b>21:00</b> &mdash; Airport pickup. Transfer to hotel (approx. 45 min).</li>'
            f'<li><b>22:00</b> &mdash; Hotel check-in. SIM cards distributed. Hotel {TBC}.</li>'
            f'<li><b>22:30</b> &mdash; Full team debrief and security handover with local ground team. Local contact {TBC}.</li>'
            f'<li><b>23:30</b> &mdash; Rest.</li></ul></div></div>')

def stream_day(daynum, date):
    return (f'<div class="day stream"><div class="dot"></div><div class="day-body">'
            f'<div class="day-top"><span class="day-label">Day {daynum} &middot; {dlabel(date)}</span>'
            f'<span class="chip chip-stream">&#9679; Stream</span></div>'
            f'<div class="day-title">Experience and stream</div><ul class="day-items">'
            f'<li><b>06:00</b> &mdash; Wake up, morning routine and prep.</li>'
            f'<li><b>07:30</b> &mdash; Breakfast at the hotel.</li>'
            f'<li><b>10:00</b> &mdash; Morning logistics, location recce and team briefing.</li>'
            f'<li><b>14:00</b> &mdash; Depart for stream location.</li>'
            f'<li><b>15:00</b> &mdash; Experience and live stream begins. Content {TBC}. Approximately 3 to 5 hours.</li>'
            f'<li><b>20:00</b> &mdash; Stream ends. Return to hotel, team debrief.</li>'
            f'<li><b>22:00</b> &mdash; Rest.</li></ul></div></div>')

def depart_day(daynum, date):
    return (f'<div class="day depart"><div class="dot"></div><div class="day-body">'
            f'<div class="day-top"><span class="day-label">Day {daynum} &middot; {dlabel(date)}</span>'
            f'<span class="chip chip-depart">&#8962; Departure</span></div>'
            f'<div class="day-title">Final stream and departure</div><ul class="day-items">'
            f'<li><b>06:00</b> &mdash; Wake up, morning routine and prep.</li>'
            f'<li><b>07:30</b> &mdash; Breakfast at the hotel.</li>'
            f'<li><b>10:00</b> &mdash; Final logistics and pack down.</li>'
            f'<li><b>14:00</b> &mdash; Depart for final stream location.</li>'
            f'<li><b>15:00</b> &mdash; Final experience and live stream. Content {TBC}. Approximately 3 to 5 hours.</li>'
            f'<li><b>20:00</b> &mdash; Stream ends. Return to hotel.</li>'
            f'<li><b>22:00+</b> &mdash; Departure: return flight home. Timing and airline {TBC}.</li>'
            f'</ul></div></div>')

def render_leg(legid, country, dates, kinds, prev, first, nxt, nights_label, tbc):
    head_flag = f'<span class="leg-flag">{flag(country,36,24)}</span>'
    start, end = dates[0], dates[-1]
    days_html = ""
    dn = 1
    for date, kind in zip(dates, kinds):
        if kind == "arr":    days_html += arrival_day(dn, date, country, prev, first, tbc)
        elif kind == "stream": days_html += stream_day(dn, date)
        elif kind == "depart": days_html += depart_day(dn, date)
        dn += 1
    foot = f'&#8594; Travel to {nxt}, arriving in the evening' if nxt else '&#9873; Tour ends &middot; return flight home'
    return (f'<section class="leg"><div class="leg-head"><div class="leg-id">{legid}</div>'
            f'<div class="leg-title">{head_flag}{country}</div>'
            f'<div class="leg-meta"><div class="leg-dates">{daterange_label(start,end)}</div>'
            f'<div class="leg-days">{nights_label}</div></div></div>'
            f'<div class="timeline">{days_html}</div>'
            f'<div class="leg-foot">{foot}</div></section>')

def route_strip(stops):
    parts = []
    for i,(c,n) in enumerate(stops):
        if i: parts.append('<div class="stop-arr">&#8594;</div>')
        parts.append(f'<div class="stop"><div class="stop-flag">{flag(c,33,22)}</div>'
                     f'<div class="stop-name">{c}</div><div class="stop-days">{n}</div></div>')
    return '<div class="route">'+''.join(parts)+'</div>'

def D(m,d): return datetime.date(2026,m,d)

# FOUNDATION: 10 nights, 28 Jun-7 Jul
foundation = [
 ("Nigeria",    [D(6,28),D(6,29)], ["arr","stream"],  "2 nights", False),
 ("Ghana",      [D(6,30),D(7,1)],  ["arr","stream"],  "2 nights", False),
 ("Ivory Coast",[D(7,2), D(7,3)],  ["arr","stream"],  "2 nights", False),
 ("Morocco",    [D(7,4), D(7,5)],  ["arr","stream"],  "2 nights", False),
 ("Nigeria",    [D(7,6), D(7,7)],  ["arr","depart"],  "2 nights", False),
]

# WITH BENIN: 12 nights, 28 Jun-9 Jul
benin_it = [
 ("Nigeria",    [D(6,28),D(6,29)], ["arr","stream"],  "2 nights", False),
 ("Ghana",      [D(6,30),D(7,1)],  ["arr","stream"],  "2 nights", False),
 ("Ivory Coast",[D(7,2), D(7,3)],  ["arr","stream"],  "2 nights", False),
 ("Benin",      [D(7,4), D(7,5)],  ["arr","stream"],  "2 nights", False),
 ("Morocco",    [D(7,6), D(7,7)],  ["arr","stream"],  "2 nights", False),
 ("Nigeria",    [D(7,8), D(7,9)],  ["arr","depart"],  "2 nights", False),
]

def build_legs(itin):
    out = ""
    for i, leg in enumerate(itin):
        country, dates, kinds, nights_label, tbc = leg
        prev = itin[i-1][0] if i>0 else None
        nxt = itin[i+1][0] if i<len(itin)-1 else None
        out += render_leg(f"{i+1:02d}", country, dates, kinds, prev, i==0, nxt, nights_label, tbc)
    return out

def stats_block(trav, countries, nights, drange):
    return ('<div class="stats">'
            f'<div class="stat"><div class="v">{trav}</div><div class="l">Travellers</div></div>'
            f'<div class="stat"><div class="v">{countries}</div><div class="l">Countries</div></div>'
            f'<div class="stat"><div class="v">{nights}</div><div class="l">Nights</div></div>'
            f'<div class="stat"><div class="v" style="font-family:\'Cormorant Garamond\',serif">{drange}</div><div class="l">2026</div></div>'
            '</div>')

TBC_S = TBC
CALLOUT = ('<div class="seclabel">How Each Day Runs</div>'
 '<div class="callout"><ul>'
 '<li>Arrival is always in the evening. Day 1 of each country is a travel and arrival day.</li>'
 '<li>Arrival routine: airport pickup, direct transfer to the hotel, check in, full team debrief, and the security handover.</li>'
 '<li>A new ground security team in every country, so the protocol meeting happens at each arrival before the next day.</li>'
 '<li>SIM cards are arranged by the ground partner the night before each country, ready on arrival.</li>'
 '<li>Experience and live stream run in the afternoon, to overlap the US morning with the local afternoon and evening.</li>'
 '<li>Each stream runs approximately 3 to 5 hours.</li>'
 '<li>Experience and stream content is '+TBC_S+' while curation is finalised.</li>'
 '<li>Flights are shown for planning. Nothing is booked yet, so all flight details are '+TBC_S+'.</li>'
 '</ul></div>')

f_route = route_strip([("Nigeria","2n"),("Ghana","2n"),("Ivory Coast","2n"),("Morocco","2n"),("Nigeria","2n")])
f_note = ('<div class="note"><b>Foundation itinerary &mdash; 10 nights, 28 Jun &ndash; 7 Jul.</b> '
 'Nigeria &rarr; Ghana &rarr; Ivory Coast &rarr; Morocco (Marrakech) &rarr; Nigeria. '
 'Starts and ends in Lagos. 2 nights per country.</div>')
f_open = ('<div class="seclabel">Open Items to Confirm</div><div class="open"><ol>'
 '<li>Hotel per country.</li><li>Ground security team and contact per country.</li>'
 '<li>Experience and stream content per country.</li><li>Flight legs: airlines, flight numbers and exact times.</li>'
 '<li>Morocco ground partner to confirm details (Marrakech).</li>'
 '<li>Final Nigeria departure timing (evening of 7 Jul).</li></ol></div>')

foundation_view = ('<div class="view view-foundation">'
 + stats_block(12, 4, 10, "28 Jun &ndash; 7 Jul")
 + '<div class="wrap">'
 + f_note
 + '<div class="seclabel">The Route</div>' + f_route
 + CALLOUT
 + '<div class="seclabel">Day by Day</div>'
 + build_legs(foundation)
 + f_open
 + '</div></div>')

b_route = route_strip([("Nigeria","2n"),("Ghana","2n"),("Ivory Coast","2n"),("Benin","2n"),("Morocco","2n"),("Nigeria","2n")])
b_note = ('<div class="note"><b>With Benin &mdash; 12 nights, 28 Jun &ndash; 9 Jul.</b> '
 'Nigeria &rarr; Ghana &rarr; Ivory Coast &rarr; Benin &rarr; Morocco (Marrakech) &rarr; Nigeria. '
 'Adds a Benin stop between Ivory Coast and Morocco. 2 nights per country.</div>')
b_open = ('<div class="seclabel">Open Items to Confirm</div><div class="open"><ol>'
 '<li>Benin leg confirmation: hotel and ground contact in Cotonou.</li>'
 '<li>Hotel per country (all TBC).</li><li>Ground security team and contact per country.</li>'
 '<li>Experience and stream content per country.</li><li>Flight legs: airlines, flight numbers and exact times.</li>'
 '<li>Morocco ground partner to confirm details (Marrakech).</li>'
 '<li>Final Nigeria departure timing (evening of 9 Jul).</li></ol></div>')

benin_view = ('<div class="view view-benin">'
 + stats_block(12, 5, 12, "28 Jun &ndash; 9 Jul")
 + '<div class="wrap">'
 + b_note
 + '<div class="seclabel">The Route</div>' + b_route
 + CALLOUT
 + '<div class="seclabel">Day by Day</div>'
 + build_legs(benin_it)
 + b_open
 + '</div></div>')

EXTRA_CSS = (
 '.viewtoggle{display:flex;gap:0;background:#16130c;padding:0;}'
 '.viewtoggle .tg{flex:1 1 50%;text-align:center;padding:14px 10px;cursor:pointer;'
 'font-family:\'Jost\',sans-serif;font-size:clamp(10px,2.3vw,12px);letter-spacing:.18em;'
 'text-transform:uppercase;color:#8a7d5f;background:#16130c;border:none;'
 'border-bottom:2px solid transparent;transition:all .2s;user-select:none;}'
 '.viewtoggle .tg small{display:block;letter-spacing:.06em;font-size:9.5px;color:#6b6048;margin-top:3px;text-transform:none;}'
 '#vf:checked~.viewtoggle .tg-f,#vs:checked~.viewtoggle .tg-s{color:var(--paper);background:#0d0c0a;border-bottom-color:var(--gold);}'
 '#vf:checked~.viewtoggle .tg-f small,#vs:checked~.viewtoggle .tg-s small{color:var(--gold-lt);}'
 '.view{display:none;}'
 '#vf:checked~.view-foundation{display:block;}'
 '#vs:checked~.view-benin{display:block;}'
)

CSS = re.search(r'<style>(.*?)</style>', v4, re.S).group(1) + EXTRA_CSS

HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width, initial-scale=1">'
 '<meta name="robots" content="noindex, nofollow">'
 '<title>Ashton Hall Africa Tour &middot; Itinerary</title>'
 '<meta name="description" content="Day by day itinerary for the Ashton Hall Africa Tour by Atoure Consulting.">'
 '<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">'
 '<style>'+CSS+'</style></head><body>')

HEADER = ('<header>'
 f'<img class="logo-mono" src="{LOGO}" alt="Atoure">'
 '<div class="eyebrow">Atoure Consulting</div>'
 '<h1>Itinerary</h1>'
 '<div class="sub">Day by Day &middot; Ashton Hall Africa Tour</div>'
 '<div class="rule"></div></header>')

TOGGLE = ('<div class="viewtoggle">'
 '<label class="tg tg-f" for="vf">Foundation<small>10 nights &middot; 28 Jun&ndash;7 Jul</small></label>'
 '<label class="tg tg-s" for="vs">With Benin<small>12 nights &middot; 28 Jun&ndash;9 Jul</small></label>'
 '</div>')

html = (HEAD
 + '<div class="sheet">'
 + '<input type="radio" name="view" id="vf" checked hidden>'
 + '<input type="radio" name="view" id="vs" hidden>'
 + '<div class="ribbon">Internal working draft &middot; not for external distribution</div>'
 + HEADER
 + TOGGLE
 + foundation_view
 + benin_view
 + '<footer><span>Atoure Consulting</span><span class="g">Last updated 20 Jun 2026 &middot; Working draft</span></footer>'
 + '</div></body></html>')

open(OUT,"w",encoding="utf-8").write(html)
print("wrote", OUT, len(html), "bytes")
