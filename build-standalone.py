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


out = inline(src)
assert 'images/web/' not in out, 'an image path survived inlining'
io.open(D + 'technobotz-site-standalone.html', 'w', encoding='utf-8').write(out)
print('  technobotz-site-standalone.html  %.1fMB' %
      (os.path.getsize(D + 'technobotz-site-standalone.html') / 1048576))
