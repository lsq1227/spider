
function tacSign(e, t) {
    // signture 参数加密函数
        const jsdom = require("jsdom");
        const { JSDOM } = jsdom;
        const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
        window = dom.window;
        document = window.document;
        var n = "";
        /^http/.test(e) || (/\/toutiao\//.test(e) || (e = "/toutiao" + e),
        e = location.protocol + "//" + location.host + e);
        for (var r in t)
            n += "&" + r + "=" + encodeURIComponent(t[r]);
        e += e.indexOf("?") > -1 ? e.indexOf("&") > -1 ? n : n.slice(1) : "?" + n.slice(1);
        var o = {
            url: e
        }
          , i = window.byted_acrawler.sign ? window.byted_acrawler.sign(o) : "";
        return i
    }






function t() {
    //as cp 参数加密方式
        var e = Math.floor((new Date).getTime() / 1e3)
          , i = e.toString(16).toUpperCase()
          , t = md5(e).toString().toUpperCase();
        if (8 != i.length)
            return {
                as: "479BB4B7254C150",
                cp: "7E0AC8874BB0985"
            };
        for (var o = t.slice(0, 5), n = t.slice(-5), a = "", s = 0; 5 > s; s++)
            a += o[s] + i[s];
        for (var r = "", c = 0; 5 > c; c++)
            r += i[c + 3] + n[c];
        return {
            as: "A1" + a + i.slice(-3),
            cp: i.slice(0, 3) + r + "E1"
        }
    }