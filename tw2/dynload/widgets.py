import tw2.core as twc
import tw2.jquery as jq
import base
import urllib
from uuid import uuid4

class DynLoaderWidget(twc.Widget):
    template = "mako:tw2.dynload.templates.dynload"
    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        jq.jquery_js,
        base.js_loader
    ]

    hash = twc.Param("(str) unique hash code for the loader", default=None)

    def prepare(self):
        super(DynLoaderWidget, self).prepare()

        if self.hash is None:
            # User does not want a custom hash, set it randomly
            self.attrs['hash'] = self.hash = str(uuid4())

        if not hasattr(self, 'id') or 'id' not in self.attrs:
            self.attrs['id'] = self.id = "dynload-%s" % self.hash

        self._js_resources = []
        self._css_resources = []
        self._widgets = {}

        # put code here to run just before the widget is displayed
        for c in self.children:
            for res in c.resources:
                if issubclass(res, twc.JSLink):
                    self._js_resources.append("/resources/%s/%s" % (res.modname, res.req().filename))
                elif issubclass(res, twc.CSSLink):
                    self._css_resources.append("/resources/%s/%s"%(res.modname, res.req().filename))
                else:
                    pass

            self._widgets[c.id.encode()] = urllib.quote(c.display().encode())

        self.selector = self.attrs['id'].replace(':', '\\:')

        self.add_call(base.js_loader.load_widget(
            self.selector,
            twc.js_symbol(self._js_resources),
            twc.js_symbol(self._css_resources),
            twc.js_symbol(self._widgets)))
