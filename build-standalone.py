#!/usr/bin/env python3
"""Build technobotz-site-standalone.html: one portable file with every image
inlined as a data URI. Opens by double-click on any machine, no server and no
images/ folder needed. Good for emailing or AirDropping the site to someone.

    python3 build-standalone.py

Reads index.html and images/, writes technobotz-site-standalone.html.
Prefers the smaller images/embed/ copy of each image when one exists.
The output is generated. Never hand-edit it; edit index.html and rebuild.
"""
import io, base64, re, os, mimetypes

D = os.path.dirname(os.path.abspath(__file__)) + '/'
src = io.open(D + 'index.html', encoding='utf-8').read()


def uri(path):
    mt = mimetypes.guess_type(path)[0] or 'image/png'
    return 'data:%s;base64,%s' % (mt, base64.b64encode(io.open(path, 'rb').read()).decode())


def inline(t):
    for root in ('technobotz-mark.png', 'technobotz-pig.png'):
        if root in t:
            t = t.replace(root, uri(D + root))
    # longest first, so a name that is a prefix of another is not partly replaced
    for m in sorted(set(re.findall(r'images/web/([A-Za-z0-9_\-]+\.(?:jpg|png))', t)),
                    key=len, reverse=True):
        embed = D + 'images/embed/' + m
        if not os.path.exists(embed):
            alt = embed.rsplit('.', 1)[0] + '.jpg'
            embed = alt if os.path.exists(alt) else D + 'images/web/' + m
        t = t.replace('images/web/' + m, uri(embed))
    return t


def bundle_rosters(t):
    """Fold season-rosters.html into the build as a tenth page, p-season-rosters.

    On the live site it is its own file. Here there is only one file, so its
    <main> becomes a .pg the router can show, its page-only CSS (between the
    bundle:start and bundle:end markers) joins the main stylesheet, and every
    link to it becomes a data-go link. Links back to index.html#X become
    data-go="X".
    """
    r = io.open(D + 'season-rosters.html', encoding='utf-8').read()
    css = re.search(r'/\* bundle:start.*?\*/\n(.*?)/\* bundle:end \*/', r, re.S).group(1)
    body = re.search(r'<main>\n(.*?)</main>', r, re.S).group(1)
    body = re.sub(r'href="index\.html#([\w-]+)"', r'href="#" data-go="\1"', body)
    assert t.count('</style>\n<noscript>') == 1 and t.count('<footer class="ft2">') == 1
    t = t.replace('</style>\n<noscript>', '\n/* season rosters page, bundled by build-standalone.py */\n'
                  + css + '</style>\n<noscript>')
    t = t.replace('<footer class="ft2">', '<!-- ================= SEASON ROSTERS (bundled) ================= -->\n'
                  '<main class="pg" id="p-season-rosters">\n' + body + '</main>\n\n<footer class="ft2">')
    t = t.replace('href="season-rosters.html"', 'href="#" data-go="season-rosters"')
    return t


PDF = 'TechnoBotz-Season-Rosters.pdf'


def live_pdf(t):
    """The roster PDF is not bundled, so every link to it (the Meet the Team
    line and the rosters page's "Official PDF roster") points at the live copy.
    index.html itself keeps the relative link."""
    return t.replace('href="%s"' % PDF, 'href="https://technobotz.org/%s"' % PDF)


out = inline(live_pdf(bundle_rosters(src)))
assert 'season-rosters.html' not in out, 'a link to season-rosters.html survived bundling'
assert 'href="%s"' % PDF not in out, 'a relative link to the roster PDF survived'
assert 'index.html#' not in out, 'a link back to index.html survived bundling'
assert 'images/web/' not in out, 'an image path survived inlining'
io.open(D + 'technobotz-site-standalone.html', 'w', encoding='utf-8').write(out)
print('  technobotz-site-standalone.html  %.1fMB' %
      (os.path.getsize(D + 'technobotz-site-standalone.html') / 1048576))
