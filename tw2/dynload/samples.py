"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets
import tw2.polymaps
import tw2.jqplugins.ui

class DynLoaderTestWidget(tw2.dynload.DynLoaderWidget):
    class TestJQUIButtonWidget(tw2.jqplugins.ui.ButtonWidget):
        id = "testbuttonwidget"
        options = {'label': 'I am a dynamically loaded button!'}
