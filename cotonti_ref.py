import webbrowser
#import sublime
import sublime_plugin
import re


class CotontiRefCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = ""
        url = "http://www.cotonti.com/reference/cotonti/package-functions.html#"
        for region in self.view.sel():
            selection += self.view.substr(region)
        try:
            m = re.match(r"(cot_\w+)", selection)
            if m:
                symbol = m.group(1)
                url = url + symbol + "()"
                webbrowser.open_new_tab(url)
        except TypeError:
            pass
