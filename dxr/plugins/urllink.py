import re

import dxr.plugins


# From http://stackoverflow.com/a/1547940
url_re = re.compile("\[(https?://[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+\.[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+)\]"
       "|\((https?://[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+\.[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+)\)"
       "|(https?://[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+\.[A-Za-z0-9\-\._~:\/\?#[\]@!\$&'()*\+,;=%]+)")


class FileIndexer(dxr.plugins.FileIndexer):
    def line_refs(self):
        if isinstance(self.contents, unicode):
            for m in url_re.finditer(self.text):
                if m.group(1):
                    url = m.group(1)
                    start, end = m.start(1), m.end(1)
                elif m.group(2):
                    url = m.group(2)
                    start, end = m.start(2), m.end(2)
                else:
                    url = m.group(3)
                    start, end = m.start(3), m.end(3)
                yield start, end, ([{
                    'html':   "Follow link",
                    'title':  "Visit %s" % url,
                    'href':   url,
                    'icon':   'external_link'
                }], '', None)