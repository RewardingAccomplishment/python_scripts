#!/usr/bin/env python3
"""
Script for Test Driven Development
script make in loop ceedling test, it allows TDD with ceedling
for make compatible with python 3.x
"""
import os
import queue
import sys
import tdd_cmd
import urwid
import subprocess
import re

"""--------------------------------------------------------------------------"""
""" TUI - Text User Interface """
"""--------------------------------------------------------------------------"""
global current_cmd
global str_cmd

def menu_button(caption, callback):
    button = urwid.Button(caption)
    urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, u'...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button):
    global current_cmd
    current_cmd = button
    try:
        details = action_cmd[ button.label ][2]
    except:
        details = u'\n'
    response = urwid.Text([u'You choose ', button.label, u': \n', details])
    done = menu_button(u'Ok', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, done])))

global edit
def item_question(button):
    global current_cmd
    global edit

    current_cmd = button
    try:
        details = action_cmd[ button.label ][2]
    except:
        details = u'\n'

    edit = urwid.Edit([u'You choose ', button.label, u': \n', details, "\n"])
    done = menu_button(u'Ok', answer)
    top.open_box(urwid.Filler(urwid.Pile([edit, done])))

def answer(name):
    global edit
    global str_cmd

    str_cmd = edit.get_edit_text()
    raise urwid.ExitMainLoop()

def exit_program(button):
    raise urwid.ExitMainLoop()

top_instruction = u'..::Ceedling Test Drive Development Automation::..'
menu_top = menu(top_instruction, [
    sub_menu(u'Test', [
        menu_button(u'TDD', item_chosen),
        menu_button(u'TDD Delta', item_chosen),
        menu_button(u'Delta', item_chosen),
        menu_button(u'Single Module', item_chosen),
        ]),
    sub_menu(u'Build', [
        menu_button(u'All', item_chosen),
        menu_button(u'Release', item_chosen),
        menu_button(u'Environment', item_chosen),
        menu_button(u'Clean', item_chosen),
        menu_button(u'Clean hard', item_chosen),
    ]),
    sub_menu(u'Files', [
        menu_button(u'New Project', item_question),
        menu_button(u'New Module', item_question),
        menu_button(u'Assembly', item_chosen),
        menu_button(u'Header', item_chosen),
        menu_button(u'Source', item_chosen),
        menu_button(u'Test', item_chosen),
    ]),
    menu_button(u'Summary', item_chosen),
    sub_menu(u'Information', [
        menu_button(u'About', item_chosen),
        menu_button(u'TODO 2', item_chosen),
    ]),
])

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level * 3,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

class TestSingleModule():
    def __init__(self, title, choices):
        self.choices = choices
        self.title = title
        main_padding = urwid.Padding(self.menu(), left=2, right=2)
        self.top = urwid.Overlay(main_padding, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                            align='center', width=('relative', 60),
                            valign='middle', height=('relative', 60),
                            min_width=20, min_height=9)
        self.run_cmd = 'ceedling test:all'

    def menu(self):
        body = [urwid.Text(self.title), urwid.Divider()]
        for c in self.choices:
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', self.exit_program, c)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

    def exit_program(self, button, tmp):
        self.cmd = 'ceedling test:{}'.format(button.label)
        raise urwid.ExitMainLoop()

    def main(self):
        urwid.MainLoop(self.top, palette=[('reversed', 'standout', '')]).run()
        print("Command line: {}".format(self.cmd))
        os.system(self.run_cmd)

"""--------------------------------------------------------------------------"""
""" MAIN """
"""--------------------------------------------------------------------------"""
command = queue.Queue()
top = CascadingBoxes(menu_top)

def tdd_loop(*args):
    data = action_cmd[ args[0] ]
    t1 = tdd_cmd.thread_tdd(1, data[1], 10, command)
    try:
        t1.start()
    except:
        print("Error: unable to start thread")

    print('wait for boost or exit')

    while ( 'q' != sys.stdin.read(1) ):
        sys.stdin.flush()
        command.put(1)                  # 1 boost

    command.put(0)                      # 0 exit thread before quit
    t1.stop()

def os_cmd(*args):
    data = action_cmd[ args[0] ]
    os.system( data[1] )
    return False

def os_new(*args):
    global str_cmd

    data = action_cmd[ args[0] ]
    if args[0] == 'New Project':
        os.system("{} {}".format(data[1], str_cmd))
    elif args[0] == 'New Module':
        print("{}[{}]".format(data[1], str_cmd))
        os.system("{}[{}]".format(data[1], str_cmd))
    else:
        os.system( data[1] )

    return False

def single_module(*arg):
    # take the list of test file in workspace
    proc = subprocess.Popen(["ceedling files:test"], stdout=subprocess.PIPE,
                            shell=True )
    (out, err) = proc.communicate()

    pattern = 'test_.*?\.c'
    test_module_list = re.findall(pattern, str(out))

    TestSingleModule(r'Test single module', test_module_list).main()


#TODO logging, verbosity, create:module
action_cmd = {
    'TDD'        : [tdd_loop, "test:all",
                            "Run all unit tests (rebuilding anything that\'s"
                            "changed along the way). Running in the loop"],
    'All'        : [os_cmd, 'ceedling test:all',
                            "Run all unit tests (rebuilding anything that\'s"
                            "changed along the way)."],
    'Delta'      : [os_cmd, 'ceedling test:delta',
                            "Run only those unit tests for which the source or "
                            "test files have changed (i.e. incremental build)."],
    'TDD Delta'  : [tdd_loop, 'test:delta',
                            "Run only those unit tests for which the source or "
                            "test files have changed (i.e. incremental build)."],
    'Single Module': [single_module, "none",
                            "Execute the named test file or the named source "
                            "file that has an accompanying test. No path. "],
    'Summary'    : [os_cmd, 'ceedling summary',
                            "If plugins are enabled, this task will execute the "
                            "summary method of any plugins supporting it. This "
                            "task is intended to provide a quick roundup of "
                            "build artifact metrics without re-running any part"
                            " of the build."],
    'Environment': [os_cmd, 'ceedling environment',
                            "List all configured environment variable names "
                            "and string values. This task is helpful in "
                            "verifying the evaluatio of any Ruby expressions "
                            "in the [:environment] section of your config file."],
    'Clean'      : [os_cmd, 'ceedling clean',
                            "Deletes all toolchain binary artifacts (object "
                            "files, executables), test results, and any "
                            "temporary files. Clean produces no output at the "
                            "command line unless verbosity has been set to an "
                            "appreciable level."],
    'Clean hard' : [os_cmd, 'ceedling clobber',
                            "Extends clean task's behavior to also remove "
                            "generated files: test runners, mocks, preprocessor "
                            "output. Clobber produces no output at the command "
                            "line unless verbosity has been set to an "
                            "appreciable level."],
    'Release'    : [os_cmd, 'ceedling release',
                            "Build all source into a release"
                            " artifact (if the release build option is "
                            "configured)."],
    'Assembly'   : [os_cmd, 'ceedling files:assembly',
                            "List all files and file counts collected from the "
                            "relevant search paths specified by the [:paths] "
                            "entries of your YAML config file. The files:assembly"
                            " task will only be available if assembly support is"
                            " enabled in the [:release_build] section of your "
                            "configuration file."],
    'Header'     : [os_cmd, 'ceedling files:header',
                            "List all files and file counts collected from the "
                            "relevant search paths specified by the [:paths] "
                            "entries of your YAML config file. The files:assembly"
                            " task will only be available if assembly support is"
                            " enabled in the [:release_build] section of your "
                            "configuration file."],
    'Source'     : [os_cmd, 'ceedling files:source',
                            "List all files and file counts collected from the "
                            "relevant search paths specified by the [:paths] "
                            "entries of your YAML config file. The files:assembly"
                            " task will only be available if assembly support is"
                            " enabled in the [:release_build] section of your "
                            "configuration file."],
    'Test'       : [os_cmd, 'ceedling files:test',
                            "List all files and file counts collected from the "
                            "relevant search paths specified by the [:paths] "
                            "entries of your YAML config file. The files:assembly"
                            " task will only be available if assembly support is"
                            " enabled in the [:release_build] section of your "
                            "configuration file."],
    'New Project': [os_new, 'ceedling new',
                            "Allows you to generate the skeleton for starting a "
                            "new project. Please type the project name..."],
    'New Module' : [os_new, 'ceedling module:create',
                            "Allows you to generate the module (source, header and test files) for starting a "
                            "new module in the current project. Please type the module name..."],
    'About'      : [os_cmd, "echo \" Best regards\"",
                            "Script for support Test-Driven-Development based on"
                            " ceedling. Text user interface based on Urwid library."
                            "\n \n TDD cycle: \n 1. Add a test \n 2. Run one of TDD option \n"
                            " 3. Write code (test fail) \n 4. Write code (test pass)\n"
                            " 5. Refactor code and go to step 1.\n \n"
                            "All code is copyright © 2018 M. Sosnowski"]
}

def do_action(action):
    """
    @brief Call the action from action dictionary.
    """
    try:
        action_cmd[action][0](action) == 0
    except KeyError:
        print('Incorrect action name; action not found')

def main():
    """
    main function
    """
    global current_cmd
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
    do_action(current_cmd.label)

if '__main__'==__name__:
     main()
