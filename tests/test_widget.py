from tw2.core.testbase import  WidgetTest
import tw2.dynload
import tw2.forms

class DynLoaderTestWidget(tw2.dynload.DynLoaderWidget):
    class TestTextArea(tw2.forms.TextArea):
        id = "test_textarea"

class TestDemoWidget(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = DynLoaderTestWidget

    params = {'hash' : "bangin_seven_gram_rocks"}

    expected = """<div id="dynload-bangin_seven_gram_rocks"></div>"""
