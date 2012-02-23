import tw2.core as twc

js_loader = twc.JSLink(modname=__name__, filename='static/dynloader.js',
            load_js=twc.js_function("loadjs"),
            load_css=twc.js_function("loadcss"),
            #load_widget=twc.js_function('loadwidget'),
            load_widget=twc.js_function("load_widget"))
