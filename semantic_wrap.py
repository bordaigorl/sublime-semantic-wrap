import sublime
from sublime import Region
import sublime_plugin


def is_semantic_wrap_enabled(view):
    return view and view.settings().get("semantic_wrap", False)


def semantic_wrap_set(view, x):
    if view:
        view.settings().set("semantic_wrap", x)


class SetSemanticWrapCommand(sublime_plugin.TextCommand):

    def is_enabled(self, wrap=True):
        return wrap != is_semantic_wrap_enabled(self.view)

    def run(self, edit, wrap=True):
        semantic_wrap_set(self.view, wrap)


class ToggleSemanticWrapCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        view = sublime.active_window().active_view()
        t = is_semantic_wrap_enabled(view)
        semantic_wrap_set(view, not t)

    def is_checked(self):
        view = sublime.active_window().active_view()
        return is_semantic_wrap_enabled(view)

    def description(self):
        view = sublime.active_window().active_view()
        if is_semantic_wrap_enabled(view):
            return "Semantic Wrap: Turn Off"
        else:
            return "Semantic Wrap: Turn On"


class SemanticWrapCommand(sublime_plugin.EventListener):

    def on_query_context(self, view, key, operator, operand, match_all):
        if key == "semantic_wrap":
            mw = view.settings().get("semantic_wrap_min_words", 3)
            if mw > 0:
                pt = view.sel()[0].a
                line = view.substr(Region(view.line(pt).begin(), pt))
                return len(line.split()) > mw
        if key == "semantic_wrap_words":
            mw = view.settings().get("semantic_wrap_max_words", 0)
            if mw > 0:
                pt = view.sel()[0].a
                line = view.substr(Region(view.line(pt).begin(), pt))
                return len(line.split()) > mw
        return False
