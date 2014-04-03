# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_file_object import WinFile
from cybox.test.objects import ObjectTestCase


class TestWinFile(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsFileObjectType"
    klass = WinFile

    _full_dict = {
        # File fields (only a few are included)
        'file_name': u"example.doc",
        'full_path': u"C:\\Temp\\example.doc",
        'file_extension': u"doc",
        'size_in_bytes': 1024L,
        'magic_number': u"D0CF11E0",

        # WinFile-specific fields
        'filename_accessed_time': "2012-05-12T07:14:02+07:00",
        'filename_created_time': "2012-05-17T09:28:04+07:00",
        'filename_modified_time': "2012-06-12T11:15:12+07:00",
        'drive': u"C:",
        'security_id': u"S-1-5-21-3623958015-3361044348-30300820-1013",
        'security_type': u"SidTypeFile",
        #TODO: add stream_list
        #'stream_list': [{'name': u"StreamA"}],

        # WinFile-specific implementations of abstract types.
        'file_attributes_list': [u"Hidden", u"System", u"Temporary"],
        'permissions': {
            'full_control': False,
            'modify': True,
            'read': True,
            'read_and_execute': False,
            'write': False,
        },

        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
