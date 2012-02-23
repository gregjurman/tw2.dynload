"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets
import tw2.polymaps

class DemoDynLoader(widgets.DynLoaderWidget):
    class PolyMap(tw2.polymaps.PolyMap):
        # Provide default parameters, value, etc... here
        # default = <some-default-value>
        interact = True
        # You should get your own one of these at http://cloudmade.com/register
        cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"
        # To style the map tiles
        cloudmade_tileset = 'midnight-commander'
        # Both specify the css_class AND include your own custom css file that
        # specifies what it looks like.
        css_class = 'sample-tw2-polymaps-container-1'
