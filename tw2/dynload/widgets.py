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

    def prepare(self):
        super(DynLoaderWidget, self).prepare()

        self._hash = str(uuid4())
        self._js_resources = []
        self._css_resources = []
        self._widgets = {}

        # put code here to run just before the widget is displayed
        for c in self.children:
            for res in c.resources:
                if issubclass(res, twc.JSLink):
                    self._js_resources.append("/resources/%s/%s"%(res.modname, res.filename))
                elif issubclass(res, twc.CSSLink):
                    self._css_resources.append("/resources/%s/%s"%(res.modname, res.filename))
                else:
                    pass

            self._widgets[c.id.encode()] = urllib.quote(c.display().encode())

        self.add_call( base.js_loader.load_widget(
            self._hash,
            twc.js_symbol(self._js_resources),
            twc.js_symbol(self._css_resources),
            twc.js_symbol(self._widgets)) )
