#ifndef GUARD_CONFIG_H
#define GUARD_CONFIG_H

// In the Generation 3 games, Asserts were used in various debug builds.
// Ruby/Sapphire and Emerald do not have these asserts while Fire Red
// still has them in the ROM. This is because the developers forgot
// to define NDEBUG before release, however this has been changed as
// Ruby's actual debug build does not use the AGBPrint features.
#define NDEBUG

// To enable printf debugging, comment out "#define NDEBUG". This allows
// the various AGBPrint functions to be used. (See include/gba/isagbprint.h).
// See below for enabling different pretty printing versions.

#ifndef NDEBUG

#define PRETTY_PRINT_MINI_PRINTF (0)
#define PRETTY_PRINT_LIBC (1)

#define LOG_HANDLER_AGB_PRINT (0)
#define LOG_HANDLER_NOCASH_PRINT (1)
#define LOG_HANDLER_MGBA_PRINT (2)

// Use this switch to choose a handler for pretty printing.
// NOTE: mini_printf supports a custom pretty printing formatter to display preproc encoded strings. (%S)
//       some libc distributions (especially dkp arm-libc) will fail to link pretty printing.
#define PRETTY_PRINT_HANDLER (PRETTY_PRINT_MINI_PRINTF)

// Use this switch to choose a handler for printf output.
// NOTE: These will only work on the respective emulators and should not be used in a productive environment.
//       Some emulators or real hardware might (and is allowed to) crash if they are used.
//       AGB_PRINT is supported on respective debug units.

#define LOG_HANDLER (LOG_HANDLER_MGBA_PRINT)
#endif

#define ENGLISH

#ifdef ENGLISH
#define UNITS_IMPERIAL
#define CHAR_DEC_SEPARATOR CHAR_PERIOD // Period is used as a decimal separator only in the UK and the US.
#else
#define UNITS_METRIC
#define CHAR_DEC_SEPARATOR CHAR_COMMA
#endif

// Uncomment to fix some identified minor bugs
#define BUGFIX

// Various undefined behavior bugs may or may not prevent compilation with
// newer compilers. So always fix them when using a modern compiler.
#if MODERN || defined(BUGFIX)
#ifndef UBFIX
#define UBFIX
#endif
#endif

/**
 * Code below this point is code that is introduced by the Pokemon Beryl ROM hack. Features can be
 * disabled by commenting out the define. This will remove all the code related to that feature
 * from the output ROM.
 * 
 * Some options are an either-or case, where you can pick to enable one or the other (e.g.
 * VSYNC_COMPATIBILITY and VSYNC_AGGRESSIVE). Options that follow this style are indicated as such
 * with comments.
 */

// Comment out defines to disable features
#define FIX_WEATHER_SNOW                //< Fix overworld snow weather
#define FIX_REDUNDANT_POPUP             //< Remove map popups if walking between same map area
#define FIX_REDUNDANT_COLOR_MAP         //< Remove expensive calls for rebuilding color maps
#define FIX_TMS_RESTORE_PP              //< TMs no longer restore PP when used

#define QOL_BETTER_DEFAULT_OPTIONS      //< Set better default options for new saves
#define QOL_NO_EXTRA_SAVE_CONFIRM       //< Remove extra confirmation for saving game
#define QOL_DISABLE_UNION_ROOM_CHECK    //< Disable Nurse Joy checking the union room
#define QOL_EASY_FISHING                //< Fishing never fails and always hooks a Pokemon
#define QOL_RENAME_TRADED_POKEMON       //< Able to rename all Pokemon, even if received in trade
#define QOL_FAST_RUN                    //< Pressing "B" in battle moves cursor to "RUN"
#define QOL_RUN_INDOORS                 //< Allows for running indoors
#define QOL_CHANGE_CLOCK_TIME           //< Change the current time by pressing SELECT when viewing the clock

#define FEATURE_PHYS_SPEC_SPLIT         //< Enable the physical-special split from gen 4
#define FEATURE_INFINITE_TMS            //< TMs are no longer consumed on use

// Choose only one of the VSYNC_ options
#define VSYNC_COMPATIBILITY             //< Optimize Vsync while maintaining linking compatibility
//#define VSYNC_AGGRESSIVE              //< Optimize Vsync aggressively, breaking vanilla compatibility

#endif // GUARD_CONFIG_H
