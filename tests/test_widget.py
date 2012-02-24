from tw2.core.testbase import  WidgetTest
import tw2.dynload
import tw2.forms
import tw2.jqplugins.ui

class DynLoaderNoResourcesTestWidget(tw2.dynload.DynLoaderWidget):
    class TestTextArea(tw2.forms.TextArea):
        id = "test_textarea"

class DynLoaderResourcesTestWidget(tw2.dynload.DynLoaderWidget):
    class TestJQUIButtonWidget(tw2.jqplugins.ui.ButtonWidget):
        id = "testbuttonwidget"

class TestDynLoaderNoResourcesWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = DynLoaderNoResourcesTestWidget

    params = {'hash' : "bangin_seven_gram_rocks"}

    expected = """<div id="dynload-bangin_seven_gram_rocks"></div>"""

class TestDynLoaderResourcesWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = DynLoaderResourcesTestWidget

    params = {'hash' : 'sheening_too_hard'}

    expected = """<div id="dynload-sheening_too_hard"></div>"""
