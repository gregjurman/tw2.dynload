import tw2.core as twc

js_puncher = twc.JSLink(modname=__name__, filename='static/duckpunch.js',
            load_js=twc.js_function("loadjs"),
            load_css=twc.js_function("loadcss"),
            load_widget=twc.js_function('loadwidget'),
            punch_widget=twc.js_function("punch_widget"))
