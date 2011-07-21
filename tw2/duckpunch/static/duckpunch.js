var js_check_list = new Array();

function loadjs(files)
{
    $.each(files, function (index, filename) {
        console.log("Load JS:" + filename);
        if ($.inArray(filename, js_check_list) == -1)
        { 
            $.ajax({
                url: filename,
                dataType: "script",
                async: false,
                success: function(){   
                    console.log("Success Load JS:" + this.url);
                    js_check_list.push(this.url);
                }
            });
        }
        else { console.log("Already Loaded JS: "+filename+". Skipping.");}
    });
}


function loadcss(files)
{
    for (i in files)
    {
        console.log("Load CSS:" + files[i]);
        var fileref=document.createElement("link");
        fileref.setAttribute("rel", "stylesheet");
        fileref.setAttribute("type", "text/css");
        fileref.setAttribute("href", files[i]);
        document.getElementsByTagName("head")[0].appendChild(fileref);
    }
}


function loadwidget(hash, widgets)
{
    for (key in widgets)
    {
        console.log("Load Widget:" + key);
        var w = unescape(widgets[key]);
        var div_place = $("#duckpunch-"+hash);
        div_place.html(w);
    }
}

function punch_widget(hash, js_resources, css_resources, widgets)
{
    loadjs(js_resources);
    loadcss(css_resources);
    loadwidget(hash, widgets);
}
