#!/usr/bin/env python

# Copyright (c) 2017
#
# This project is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.


SYSEX_START = 0xf0
SYSEX_REALTIME = 0x7f
SYSEX_NONREALTIME = 0x7e
SYSEX_NONREALTIME_GENERALINFO = 0x06
SYSEX_NONREALTIME_IDREQUEST = 0x01
SYSEX_NONREALTIME_IDREPLY = 0x02
SYSEX_STOP = 0xf7

ZOOM_00 = 0x00
ZOOM_MIDI_ID = 0x52
ZOOM_DEVICE_ID_G1ON = 0x63
ZOOM_EDITOR_MODE_ON = 0x50
ZOOM_EDITOR_MODE_OFF = 0x51
ZOOM_REQUEST_CURRENT_PATCH_NUMBER = 0x33
ZOOM_REQUEST_CURRENT_PATCH = 0x29
ZOOM_REQUEST_PATCH_BY_NUMBER = 0x09

ZOOM_G1ON_PATCH_CHANGE_REQUEST = [0xc0]

ZOOM_G1ON_REQUEST_ID = [SYSEX_START, SYSEX_NONREALTIME, ZOOM_00, SYSEX_NONREALTIME_GENERALINFO, SYSEX_NONREALTIME_IDREQUEST, SYSEX_STOP]
ZOOM_G1ON_ID = [SYSEX_START, SYSEX_NONREALTIME, ZOOM_00, SYSEX_NONREALTIME_GENERALINFO, SYSEX_NONREALTIME_IDREPLY, ZOOM_MIDI_ID, ZOOM_DEVICE_ID_G1ON, 0x00, 0x00, 0x00]

ZOOM_G1ON_REQUEST_CURRENT_PATCH_NUMBER = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, ZOOM_REQUEST_CURRENT_PATCH_NUMBER, SYSEX_STOP]
ZOOM_G1ON_REQUEST_CURRENT_PATCH = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, ZOOM_REQUEST_CURRENT_PATCH, SYSEX_STOP]
ZOOM_G1ON_REQUEST_PATCH_BY_NUMBER_PREFIX = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, ZOOM_REQUEST_PATCH_BY_NUMBER]
ZOOM_G1ON_REQUEST_EDITOR_MODE_ON = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, ZOOM_EDITOR_MODE_ON, SYSEX_STOP]
ZOOM_G1ON_REQUEST_EDITOR_MODE_OFF = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, ZOOM_EDITOR_MODE_OFF, SYSEX_STOP]

ZOOM_G1ON_CURRENT_PATCH_ID = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, 0x28]
ZOOM_G1ON_PATCH_CHANGE_ID  = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, 0x31]
ZOOM_G1ON_PATCH_ID = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, 0x08, 0x00, 0x00]

ZOOM_G1ON_PATCH  = [SYSEX_START, ZOOM_MIDI_ID, ZOOM_00, ZOOM_DEVICE_ID_G1ON, 0x30]


ZOOM_G1ON_EFFECT_LOCATIONS = [
	[0, 20],
	[20, 41],
	[41, 61],
	[61, 82],
	[82, 102],
]

ZOOM_G1ON_EFFECTS = {
	(0x00, 0x00, 0x00, 0x00): 'bypass',
	(0x00, 0x10, 0x00, 0x02): 'comp',
	(0x00, 0x60, 0x00, 0x02): 'optcomp',
	(0x00, 0x6a, 0x00, 0x02): '160comp',
	(0x40, 0x00, 0x00, 0x02): 'slowattck',
	(0x40, 0x20, 0x00, 0x02): 'znr',
	(0x40, 0x40, 0x00, 0x02): 'noisegate',
	(0x00, 0x20, 0x00, 0x04): 'graphiceq',
	(0x00, 0x40, 0x00, 0x04): 'paraeq',
	(0x00, 0x60, 0x00, 0x04): 'exciter',
	(0x40, 0x20, 0x00, 0x04): 'autowah',
	(0x40, 0x60, 0x00, 0x04): 'cry',
	(0x00, 0x20, 0x01, 0x04): 'mfilter',
	(0x00, 0x40, 0x01, 0x04): 'step',
	(0x00, 0x60, 0x01, 0x04): 'seqfilter',
	(0x40, 0x00, 0x01, 0x04): 'randomfilter',
	(0x40, 0x20, 0x01, 0x04): 'fcycle',
	(0x00, 0x10, 0x00, 0x06): 'booster',
	(0x00, 0x20, 0x00, 0x06): 'overdrive',
	(0x00, 0x40, 0x00, 0x06): 'tscream',
	(0x00, 0x60, 0x00, 0x06): 'governor',
	(0x40, 0x00, 0x00, 0x06): 'distplus',
	(0x40, 0x20, 0x00, 0x06): 'dist1',
	(0x40, 0x40, 0x00, 0x06): 'squeak',
	(0x40, 0x60, 0x00, 0x06): 'fuzzsmile',
	(0x00, 0x00, 0x01, 0x06): 'greatmuff',
	(0x00, 0x20, 0x01, 0x06): 'metalwrld',
	(0x00, 0x40, 0x01, 0x06): 'hotbox',
	(0x00, 0x60, 0x01, 0x06): 'zclean',
	(0x40, 0x00, 0x01, 0x06): 'zmp1',
	(0x40, 0x60, 0x01, 0x06): 'zscream',
	(0x00, 0x20, 0x02, 0x06): 'zwild',
	(0x00, 0x40, 0x02, 0x06): 'leadzoom9002',
	(0x00, 0x60, 0x02, 0x06): 'extremedistortion',
	(0x40, 0x00, 0x02, 0x06): 'acoustic',
	(0x00, 0x10, 0x00, 0x08): 'fdcombo',
	(0x00, 0x20, 0x00, 0x08): 'deluxer',
	(0x00, 0x40, 0x00, 0x08): 'fdvibro',
	(0x00, 0x60, 0x00, 0x08): 'usblues',
	(0x40, 0x00, 0x00, 0x08): 'vxcombo',
	(0x40, 0x20, 0x00, 0x08): 'vxjmi',
	(0x40, 0x40, 0x00, 0x08): 'bgcrunch',
	(0x40, 0x60, 0x00, 0x08): 'match30',
	(0x00, 0x00, 0x01, 0x08): 'cardrive',
	(0x00, 0x20, 0x01, 0x08): 'twrock',
	(0x00, 0x40, 0x01, 0x08): 'tonecity',
	(0x00, 0x60, 0x01, 0x08): 'hwstack',
	(0x40, 0x00, 0x01, 0x08): 'tangerine',
	(0x40, 0x20, 0x01, 0x08): 'bbreaker',
	(0x40, 0x40, 0x01, 0x08): 'mscrunch',
	(0x40, 0x60, 0x01, 0x08): 'ms1959',
	(0x00, 0x00, 0x02, 0x08): 'msdrive',
	(0x00, 0x20, 0x02, 0x08): 'bgndrv',
	(0x00, 0x40, 0x02, 0x08): 'bgdrive',
	(0x00, 0x60, 0x02, 0x08): 'dzdrive',
	(0x40, 0x00, 0x02, 0x08): 'alien',
	(0x40, 0x20, 0x02, 0x08): 'revo1',
	(0x00, 0x10, 0x00, 0x0c): 'tremelo',
	(0x00, 0x40, 0x00, 0x0c): 'slicer',
	(0x00, 0x60, 0x00, 0x0c): 'phaser',
	(0x00, 0x6a, 0x00, 0x0c): 'duophase',
	(0x00, 0x00, 0x02, 0x0c): 'vibrato',
	(0x40, 0x00, 0x00, 0x0c): 'thevibe',
	(0x00, 0x00, 0x01, 0x0c): 'detune',
	(0x40, 0x60, 0x00, 0x0c): 'chorus',
	(0x00, 0x40, 0x01, 0x0c): 'stereocho',
	(0x00, 0x60, 0x01, 0x0c): 'ensemble',
	(0x40, 0x20, 0x01, 0x0c): 'supercho',
	(0x00, 0x00, 0x04, 0x0c): 'coronatri',
	(0x40, 0x40, 0x01, 0x0c): 'flanger',
	(0x40, 0x30, 0x01, 0x0c): 'vinflngr',
	(0x00, 0x20, 0x02, 0x0c): 'octave',
	(0x00, 0x40, 0x02, 0x0c): 'pitchshft',
	(0x00, 0x60, 0x02, 0x0c): 'monopitch',
	(0x40, 0x00, 0x02, 0x0c): 'hps',
	(0x40, 0x20, 0x02, 0x0c): 'bendcho',
	(0x40, 0x60, 0x02, 0x0c): 'ringmod',
	(0x40, 0x40, 0x00, 0x0e): 'rotocloset',
	(0x00, 0x20, 0x00, 0x0e): 'bitcrush',
	(0x00, 0x40, 0x00, 0x0e): 'bomber',
	(0x40, 0x00, 0x00, 0x0e): 'zorgan',
	(0x00, 0x10, 0x00, 0x10): 'delay',
	(0x40, 0x60, 0x01, 0x10): 'carbondelay',
	(0x40, 0x00, 0x01, 0x10): 'stompdly',
	(0x00, 0x20, 0x00, 0x10): 'tapeecho',
	(0x40, 0x00, 0x00, 0x10): 'reversedelay',
	(0x40, 0x20, 0x00, 0x10): 'multitapdelay',
	(0x40, 0x60, 0x00, 0x10): 'filterdly',
	(0x00, 0x00, 0x01, 0x10): 'pitchdelay',
	(0x00, 0x20, 0x01, 0x10): 'stereodelay',
	(0x00, 0x10, 0x00, 0x12): 'hdhall',
	(0x00, 0x20, 0x00, 0x12): 'hall',
	(0x00, 0x40, 0x00, 0x12): 'room',
	(0x00, 0x60, 0x00, 0x12): 'tiledrm',
	(0x40, 0x20, 0x00, 0x12): 'arenareverb',
	(0x00, 0x20, 0x01, 0x12): 'plate',
	(0x40, 0x00, 0x01, 0x12): 'spring63',
	(0x40, 0x60, 0x00, 0x12): 'air',
	(0x40, 0x40, 0x00, 0x12): 'earlyreflection',
	(0x00, 0x40, 0x01, 0x12): 'modreverb',
	(0x00, 0x20, 0x03, 0x12): 'particlereverb',
}

ZOOM_G1ON_AMP_NAMES = [
	'fdcombo',
	'deluxer',
	'fdvibro',
	'usblues',
	'vxcombo',
	'vxjmi',
	'bgcrunch',
	'match30',
	'cardrive',
	'twrock',
	'tonecity',
	'hwstack',
	'tangerine',
	'bbreaker',
	'mscrunch',
	'ms1959',
	'msdrive',
	'bgndrv',
	'bgdrive',
	'dzdrive',
	'alien',
	'revo1',
]
