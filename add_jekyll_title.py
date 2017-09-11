import sublime, sublime_plugin
import datetime
from string import Template

class AddJekyllTitleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = Template( "\n".join(["---", 
            "title:  \"title\"", 
            "date:   $timestamp", 
            "categories: ", 
            "---", 
            ""]) 
        ).safe_substitute(dict(timestamp=timestamp))
        self.view.run_command("insert_snippet", { "contents": "%s" %  title } )