#!/bin/python3

import tkinter

from typing import Dict, List

CONFIG_BEGIN_STR = "// GUI_CONFIG BEGIN"
CONFIG_END_STR = "// GUI_CONFIG END"
CONFIG_SECTION_STR = "// GUI_CONFIG SECTION "

# === Configuration file handling ===


class Flag():
    '''

    '''

    def __init__(self, flag: str, comment: str, enabled: bool) -> None:
        '''

        '''
        self._flag = flag
        self._comment = comment
        self._enabled = enabled

    def __str__(self) -> str:
        return (f"({self._enabled}) {self._flag}: {self._comment}")


class ConfigSection():
    '''

    '''

    def __init__(self, section_name: str):
        '''

        '''
        self._section_name: str = section_name
        self._section_flags: List[Flag] = []


class Config():
    '''

    '''

    def __init__(self, file_name: str | None = None) -> None:
        '''

        '''
        self._config_info: List[ConfigSection] = []
        if (file_name is not None):
            self.load_config(file_name)

    def load_config(self, file_name: str) -> None:
        '''

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
                    self._config_info[-1]._section_flags.append(
                        Flag(flag, comment, enabled))
        for i in self._config_info:
            for j in i._section_flags:
                print(j)


if __name__ == "__main__":
    config = Config("./include/config.h")
