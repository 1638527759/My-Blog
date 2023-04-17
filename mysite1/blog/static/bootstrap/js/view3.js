$(document).ready(function() {
    $("#pen").click(function() {
        $(".box2").animate({
            width: "toggle"
        }, 350);
    });

    $("#person").click(function() {
        $(".box1").animate({
            width: "toggle"
        }, 350);
    });

    // var testEditor;
    // $(function() {
    //     $.get("{% static 'bootstrap/plugins/editor/examples/test.md' %}", function(md) {
    //         testEditor = editormd("test-editormd", {
    //             width: "730px",
    //             height: 730,
    //             path: "{% static 'bootstrap/plugins/editor/lib/' %}",
    //             markdown: md,
    //             codeFold: true,
    //             saveHTMLToTextarea: true,
    //             searchReplace: true,
    //             htmlDecode: "style,script,iframe|on*",
    //             emoji: true,
    //             taskList: true,
    //             tocm: true, // Using [TOCM]
    //             tex: true, // 开启科学公式TeX语言支持，默认关闭
    //             flowChart: true, // 开启流程图支持，默认关闭
    //             sequenceDiagram: true, // 开启时序/序列图支持，默认关闭,
    //             imageUpload: true,
    //             editorTheme: "pastel-on-dark",
    //             theme: "dark",
    //             previewTheme: "dark"

    //         });
    //     });
    // });



    // var testEditor;
    // $(function() {
    //     $.get("{% static 'bootstrap/plugins/editor/examples/test.md' %}", function(md) {
    //         testEditor = editormd("test-editormd", {
    //             width: "730px",
    //             height: 730,
    //             path: "{% static 'bootstrap/plugins/editor/lib/' %}",
    //             // markdown: md,
    //             codeFold: true,
    //             saveHTMLToTextarea: true,
    //             searchReplace: true,
    //             htmlDecode: "style,script,iframe|on*",
    //             emoji: true,
    //             taskList: true,
    //             tocm: true, // Using [TOCM]
    //             tex: true, // 开启科学公式TeX语言支持，默认关闭
    //             flowChart: true, // 开启流程图支持，默认关闭
    //             sequenceDiagram: true, // 开启时序/序列图支持，默认关闭,
    //             imageUpload: true,
    //             editorTheme: "pastel-on-dark",
    //             theme: "dark",
    //             previewTheme: "dark"
    //         });
    //     });
    // });





});