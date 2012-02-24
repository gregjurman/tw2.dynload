import tw2.core as twc
import tw2.dynload
import tw2.jqplugins.ui
from nose.tools import eq_

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_js_call():
    class DynLoaderTestWidget(tw2.dynload.DynLoaderWidget):
        class TestJQUIButtonWidget(tw2.jqplugins.ui.ButtonWidget):
            id = "testbuttonwidget"
            options = {'label': 'I am a button!'}

    w = DynLoaderTestWidget
    w_obj = w.req()
 
    w_obj.display()

    js_calls = w_obj._js_calls

    assert(len(w_obj._js_calls) == 1)

    for js_call in w_obj._js_calls:
        eq_(js_call[0],
        """load_widget("dynload-""" + w_obj.hash + """", [\'/resources/tw2.jqplugins.ui/static/jquery/ui/1.8.17/js/jquery-ui.js\'], [\'/resources/tw2.jqplugins.ui/static/jquery/ui/1.8.17/css/smoothness/jquery-ui.css\'], {\'testbuttonwidget\': \'%0A%3Cdiv%20id%3D%22testbuttonwidget%3Awrapper%22%3E%0A%09%09%3Cbutton%20id%3D%22testbuttonwidget%22%3E%3C/button%3E%0A%3Cscript%20type%3D%22text/javascript%22%3E%0A%24%28document%29.ready%28function%28%29%20%7B%0A%20%20%20%20%24%28%22%23testbuttonwidget%22%29.button%28%7B%22label%22%3A%20%22I%20am%20a%20button%21%22%7D%29%3B%0A%7D%29%3B%0A%3C/script%3E%0A%0A%3C/div%3E%0A\'})""")
