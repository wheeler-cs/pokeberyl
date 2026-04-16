#!/bin/python3

try:
    import tkinter as tk
except:
    print("Please install the python3-tk")
    exit(1)
from typing import List


# === Configuration file handling ===

CONFIG_BEGIN_STR = "// GUI_CONFIG BEGIN"
CONFIG_END_STR = "// GUI_CONFIG END"
CONFIG_SECTION_STR = "// GUI_CONFIG SECTION "

class Flag():
    ''' Single instance of a feature flag in the project.

    Attributes:
        _flag(str): Name of flag inside code.
        _comment(str): Descriptor comment for what flag enables.
        _enabled(bool): Indicator for if flag is enabled or disabled.
    '''

    def __init__(self, flag: str, comment: str, enabled: bool) -> None:
        ''' Initialize for Flag class.

        Args:
            flag(str): Name of flag inside code.
            comment(str): Descriptor comment for what flag enables.
            enabled(bool): Indicator for if flag is enabled or disabled.
        '''
        self._flag = flag
        self._comment = comment
        self._enabled = enabled

    def __str__(self) -> str:
        ''' String overload for Flag class.
        
        Returns:
            Formatted string with all data associated with Flag instance.
        '''
        return (f"({self._enabled}) {self._flag}: {self._comment}")


class ConfigSection():
    ''' Block of related flags within the code.

    Attributes:
        _section_name(str): Text name for section.
        _section_flags(List[Flag]): List of Flags associated with section.
    '''

    def __init__(self, section_name: str) -> None:
        ''' Initializer for ConfigSection class.

        Args:
            section_name(str): Name of section.
        '''
        self._section_name: str = section_name
        self._section_flags: List[Flag] = []


class Config():
    ''' Config class containing configuration data.

    Attributes:
        _config_info(List[ConfigSection]): List of sections inside the configuration file.
    '''

    def __init__(self, file_name: str | None = None) -> None:
        ''' Initializer for Config class.

        Args:
            file_name(str | None): Path to configuration file.
        '''
        self._config_info: List[ConfigSection] = []
        if (file_name is not None):
            self.load_config(file_name)

    def load_config(self, file_name: str) -> None:
        ''' Load and parse configuration data and organize into data structures.

        Args:
            file_name(str): Path to target configuration file to parse.
        '''
        # Function variables
        config_text_list = []
        config_start = -1
        config_end = -1
        # Load text data from config file
        with open(file_name, "r") as config:
            config_text_list = config.read().split('\n')
        # Locate start and end of configuration section
        for i, text in enumerate(config_text_list):
            if text == CONFIG_BEGIN_STR:
                config_start = i
                continue
            if text == CONFIG_END_STR:
                config_end = i
                break
        # Check to make sure configuration tags exist
        if ((config_start > -1) and (config_end > -1)):
            # Iterate through text lines
            for i in range(config_start, config_end):
                # Found new section
                if (CONFIG_SECTION_STR in config_text_list[i]):
                    self._config_info.append(ConfigSection(
                        config_text_list[i][len(CONFIG_SECTION_STR):]))
                # Load flag from section
                elif ("#define" in config_text_list[i]):
                    # Determine if feature is enabled based on commenting
                    enabled = True
                    if (config_text_list[i][:2] == "//"):
                        config_text_list[i] = config_text_list[i][2:]
                        enabled = False
                    # Separate the comment from the flag name
                    split_text = config_text_list[i].split("//<")
                    comment = split_text[1][1:]
                    flag = split_text[0][len("#define "):].replace(' ', '')
                    # Add new flag
                    self._config_info[-1]._section_flags.append(
                        Flag(flag, comment, enabled))


# === GUI handling code ===

def gui_main(config: Config) -> None:
    '''
    
    '''
    window = init_window()
    populate_sections(window, config)
    window.mainloop()


def init_window() -> tk.Tk:
    '''
    
    '''
    window = tk.Tk()
    window.title("pokeberyl Configuration")
    window.geometry("1080x720")
    return window


def populate_sections(window: tk.Tk, config: Config) -> None:
    '''
    
    '''
    # Populate information
    for i, info in enumerate(config._config_info):
        # Add label to top of column
        tk.Label(window,
                 text=info._section_name,
                 relief="raised",
                 width=30,
                 anchor="w",
                 justify="left").grid(row=0,
                                      column=i)
        # Add entries to subsequent rows
        for j, flag in enumerate(info._section_flags):
            tk.Label(window,
                     text=flag._flag,
                     width=30,
                     anchor="w",
                     justify="left").grid(row=j + 1,
                                          column=i)

# === Main ===

if __name__ == "__main__":
    config = Config("./include/config.h")
    gui_main(config)
