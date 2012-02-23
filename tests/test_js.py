import tw2.core as twc
import tw2.dynload
import tw2.dyntext
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
        class TestTextWidget(tw2.dyntext.DynamicTextWidget):
            data_url = "herp"
            id = "derp"

    w = DynLoaderTestWidget
    w_obj = w.req()
 
    w_obj.display()

    js_calls = w_obj._js_calls

    assert(len(w_obj._js_calls) == 1)

    for js_call in w_obj._js_calls:
        print type(js_call)
        eq_(js_call[0], """load_widget("dynload-"""+w_obj.hash+"""", ['/resources/tw2.dyntext.widgets/static/dyntext.js', '/resources/tw2.jquery/static/jquery/1.7.1/jquery.js'], [], {'derp': '%0A%3Cspan%20id%3D%22derp%22%3E%3C/span%3E%0A'})""")
