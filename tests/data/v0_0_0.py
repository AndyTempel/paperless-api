"""Raw data constants for all Paperless versions."""

# mypy: ignore-errors

from tests.const import PAPERLESS_TEST_TOKEN, PAPERLESS_TEST_URL

V0_0_0_REMOTE_VERSION = {"version": "v2.15.3", "update_available": True}

V0_0_0_TOKEN = {"token": PAPERLESS_TEST_TOKEN}

V0_0_0_PATHS = {
    "correspondents": f"{PAPERLESS_TEST_URL}/api/correspondents/",
    "document_types": f"{PAPERLESS_TEST_URL}/api/document_types/",
    "documents": f"{PAPERLESS_TEST_URL}/api/documents/",
    "logs": f"{PAPERLESS_TEST_URL}/api/logs/",
    "tags": f"{PAPERLESS_TEST_URL}/api/tags/",
    "saved_views": f"{PAPERLESS_TEST_URL}/api/saved_views/",
    "tasks": f"{PAPERLESS_TEST_URL}/api/tasks/",
    "users": f"{PAPERLESS_TEST_URL}/api/users/",
    "groups": f"{PAPERLESS_TEST_URL}/api/groups/",
    "mail_accounts": f"{PAPERLESS_TEST_URL}/api/mail_accounts/",
    "mail_rules": f"{PAPERLESS_TEST_URL}/api/mail_rules/",
}

V0_0_0_OBJECT_PERMISSIONS = {
    "view": {
        "users": [1, 2],
        "groups": [],
    },
    "change": {
        "users": [],
        "groups": [1],
    },
}

V0_0_0_CORRESPONDENTS = {
    "count": 5,
    "next": None,
    "previous": None,
    "all": [1, 2, 3, 4, 5],
    "results": [
        {
            "id": 1,
            "slug": "sample-correspondent",
            "name": "Sample Correspondent",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 12,
            "last_correspondence": "2022-10-18",
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 2,
            "slug": "burger-fastfood-delivery-billing",
            "name": "Burger FastFood Delivery Billing",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 6,
            "last_correspondence": "2006-03-07",
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 3,
            "slug": "example-company",
            "name": "Example Company",
            "match": "",
            "matching_algorithm": 6,
            "is_insensitive": True,
            "document_count": 3,
            "last_correspondence": "2022-03-11",
            "owner": 3,
            "user_can_change": True,
        },
        {
            "id": 4,
            "slug": "no-illness-more-money-health-insurance",
            "name": "No Illness More Money Health Insurance",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 6,
            "last_correspondence": "2000-07-18",
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 5,
            "slug": "your-cash-is-my-cash-bank",
            "name": "Your Cash is my Cash Bank",
            "match": "Your Cash My Bank",
            "matching_algorithm": 2,
            "is_insensitive": True,
            "document_count": 20,
            "last_correspondence": "2023-08-28",
            "owner": None,
            "user_can_change": True,
        },
    ],
}

V0_0_0_DOCUMENTS = {
    "count": 2,
    "next": None,
    "previous": "",
    "all": [1, 2],
    "results": [
        {
            "id": 1,
            "correspondent": 1,
            "document_type": 2,
            "storage_path": None,
            "title": "Crazy Document",
            "content": "some OCRd text",
            "tags": [],
            "created": "2011-06-22",
            "modified": "2023-08-08T06:06:35.495972+00:00",
            "added": "2023-06-30T05:44:14.317925+00:00",
            "archive_serial_number": None,
            "original_file_name": "Scan_2023-06-29_113857.pdf",
            "archived_file_name": "2011-06-22 filename.pdf",
            "owner": 2,
            "user_can_change": True,
            "notes": [],
            "custom_fields": [],
        },
        {
            "id": 2,
            "correspondent": 2,
            "document_type": 1,
            "storage_path": 1,
            "title": "Salty Document",
            "content": "OCRd text from document",
            "tags": [1],
            "created": "2022-01-07",
            "modified": "2023-12-13T16:15:02.148852+00:00",
            "added": "2022-02-12T11:34:50.072000+00:00",
            "archive_serial_number": 1,
            "original_file_name": None,
            "archived_file_name": "2022-01-07.pdf",
            "owner": 1,
            "user_can_change": True,
            "notes": [
                {
                    "id": 1,
                    "note": "Sample note 1.",
                    "created": "2023-12-21T18:08:11.481206+00:00",
                    "document": 2,
                    "user": 1,
                },
                {
                    "id": 2,
                    "note": "Sample note 2.",
                    "created": "2023-12-21T08:26:33.260968+00:00",
                    "document": 2,
                    "user": 2,
                },
                {
                    "id": 3,
                    "note": "Sample note 3.",
                    "created": "2023-12-21T08:26:31.782811+00:00",
                    "document": 2,
                    "user": 3,
                },
            ],
            "custom_fields": [
                {"value": [1094, 944], "field": 8},
                {"value": "https://www.example.com", "field": 7},
                {"value": "This is a text", "field": 6},
                {"value": 1000.0, "field": 5},
                {"value": 13.37, "field": 4},
                {"value": 42, "field": 3},
                {"value": "2099-12-31", "field": 2},
                {"value": True, "field": 1},
            ],
        },
    ],
}

V0_0_0_DOCUMENTS_SEARCH = {
    "count": 1,
    "next": None,
    "previous": None,
    "all": [1],
    "results": [
        {
            "id": 1,
            "correspondent": 1,
            "document_type": 2,
            "storage_path": None,
            "title": "Crazy Document",
            "content": "some OCRd text",
            "tags": [],
            "created": "2011-06-22T00:00:00+00:00",
            "created_date": "2011-06-22",
            "modified": "2023-08-08T06:06:35.495972+00:00",
            "added": "2023-06-30T05:44:14.317925+00:00",
            "archive_serial_number": None,
            "original_file_name": "Scan_2023-06-29_113857.pdf",
            "archived_file_name": "2011-06-22 filename.pdf",
            "owner": 2,
            "user_can_change": True,
            "notes": [],
            "custom_fields": [],
            "__search_hit__": {
                "score": 1.0,
                "highlights": "some neat hint",
                "note_highlights": "",
                "rank": 0,
            },
        },
    ],
}

V0_0_0_DOCUMENTS_METADATA = {
    "original_checksum": "18e2352cc13379d19bd9ce329428bb99",
    "original_size": 190348,
    "original_mime_type": "application/pdf",
    "media_filename": "xxx.pdf",
    "has_archive_version": True,
    "original_metadata": [],
    "archive_checksum": "8a69542583571337dd263f8bb3cf23bd",
    "archive_media_filename": "0000226.pdf",
    "original_filename": None,
    "lang": "de",
    "archive_size": 161371,
    "archive_metadata": [
        {
            "namespace": "http://ns.adobe.com/pdf/1.3/",
            "prefix": "pdf",
            "key": "Producer",
            "value": "pikepdf 2.16.1",
        },
        {
            "namespace": "http://ns.adobe.com/xap/1.0/",
            "prefix": "xmp",
            "key": "ModifyDate",
            "value": "2022-02-12T11:34:40+00:00",
        },
        {
            "namespace": "http://ns.adobe.com/xap/1.0/",
            "prefix": "xmp",
            "key": "CreateDate",
            "value": "2022-01-07T13:40:49",
        },
        {
            "namespace": "http://ns.adobe.com/xap/1.0/",
            "prefix": "xmp",
            "key": "CreatorTool",
            "value": "ocrmypdf 12.3.2 / Tesseract OCR-PDF 4.1.1",
        },
        {
            "namespace": "http://ns.adobe.com/xap/1.0/mm/",
            "prefix": "xmpMM",
            "key": "DocumentID",
            "value": "uuid:13371337-2342-1337-4242-133723426665",
        },
        {
            "namespace": "http://purl.org/dc/elements/1.1/",
            "prefix": "dc",
            "key": "format",
            "value": "application/pdf",
        },
        {
            "namespace": "http://purl.org/dc/elements/1.1/",
            "prefix": "dc",
            "key": "title",
            "value": "Octopus Energy updated",
        },
        {
            "namespace": "http://www.aiim.org/pdfa/ns/id/",
            "prefix": "pdfaid",
            "key": "part",
            "value": "2",
        },
        {
            "namespace": "http://www.aiim.org/pdfa/ns/id/",
            "prefix": "pdfaid",
            "key": "conformance",
            "value": "B",
        },
        {
            "namespace": "http://purl.org/dc/elements/1.1/",
            "prefix": "dc",
            "key": "creator",
            "value": "None",
        },
        {
            "namespace": "http://ns.adobe.com/xap/1.0/",
            "prefix": "xmp",
            "key": "MetadataDate",
            "value": "2022-02-12T11:34:40.383718+00:00",
        },
    ],
}

V0_0_0_DOCUMENT_SUGGESTIONS = {
    "correspondents": [26],
    "tags": [
        1,
        2,
        3,
    ],
    "document_types": [4],
    "storage_paths": [
        3,
        5,
    ],
    "dates": [
        "2022-01-07",
        "2023-01-07",
    ],
}

V0_0_0_DOCUMENT_TYPES = {
    "count": 5,
    "next": None,
    "previous": None,
    "all": [1, 2, 3, 4, 5],
    "results": [
        {
            "id": 1,
            "slug": "bescheid",
            "name": "Bescheid",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 42,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 2,
            "slug": "document",
            "name": "Document",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 218,
            "owner": None,
            "user_can_change": None,
        },
        {
            "id": 3,
            "slug": "kontoauszug",
            "name": "Kontoauszug",
            "match": "",
            "matching_algorithm": 6,
            "is_insensitive": True,
            "document_count": 227,
            "owner": None,
            "user_can_change": None,
        },
        {
            "id": 4,
            "slug": "kundigung",
            "name": "Kuendigung",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "document_count": 24,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 5,
            "slug": "rechnung",
            "name": "Rechnung",
            "match": "",
            "matching_algorithm": 6,
            "is_insensitive": True,
            "document_count": 246,
            "owner": None,
            "user_can_change": True,
        },
    ],
}

V0_0_0_GROUPS = {
    "count": 1,
    "next": None,
    "previous": None,
    "all": [1],
    "results": [
        {
            "id": 1,
            "name": "Sample Group",
            "permissions": [
                "add_consumptiontemplate",
                "change_consumptiontemplate",
                "delete_consumptiontemplate",
                "view_consumptiontemplate",
                "view_correspondent",
                "add_customfield",
                "change_customfield",
                "delete_customfield",
                "view_customfield",
                "add_customfieldinstance",
                "change_customfieldinstance",
                "delete_customfieldinstance",
                "view_customfieldinstance",
                "add_document",
                "change_document",
                "delete_document",
                "view_document",
                "view_documenttype",
                "add_note",
                "change_note",
                "delete_note",
                "view_note",
                "add_savedview",
                "change_savedview",
                "delete_savedview",
                "view_savedview",
                "add_sharelink",
                "change_sharelink",
                "delete_sharelink",
                "view_sharelink",
                "view_tag",
                "add_uisettings",
                "change_uisettings",
                "delete_uisettings",
                "view_uisettings",
            ],
        },
    ],
}

V0_0_0_MAIL_ACCOUNTS = {
    "count": 1,
    "next": None,
    "previous": None,
    "all": [1],
    "results": [
        {
            "id": 1,
            "name": "Test Account",
            "imap_server": "imap.omega.net",
            "imap_port": 1337,
            "imap_security": 2,
            "username": "omega-weapon",
            "password": "********************",
            "character_set": "UTF-8",
            "is_token": False,
            "owner": 1,
            "user_can_change": True,
        }
    ],
}

V0_0_0_MAIL_RULES = {
    "count": 1,
    "next": None,
    "previous": None,
    "all": [1],
    "results": [
        {
            "id": 1,
            "name": "Test",
            "account": 1,
            "folder": "INBOX",
            "filter_from": None,
            "filter_to": None,
            "filter_subject": None,
            "filter_body": None,
            "filter_attachment_filename_include": None,
            "filter_attachment_filename_exclude": None,
            "maximum_age": 3,
            "action": 3,
            "action_parameter": None,
            "assign_title_from": 1,
            "assign_tags": [],
            "assign_correspondent_from": 1,
            "assign_correspondent": None,
            "assign_document_type": None,
            "assign_owner_from_rule": True,
            "order": 1,
            "attachment_type": 1,
            "consumption_scope": 1,
            "owner": 1,
            "user_can_change": True,
        }
    ],
}

V0_0_0_SAVED_VIEWS = {
    "count": 5,
    "next": None,
    "previous": None,
    "all": [1, 2, 3, 4, 5],
    "results": [
        {
            "id": 1,
            "name": "New Items",
            "show_on_dashboard": False,
            "show_in_sidebar": False,
            "sort_field": None,
            "sort_reverse": False,
            "filter_rules": [{"rule_type": 6, "value": "1"}],
            "owner": 1,
            "user_can_change": True,
        },
        {
            "id": 2,
            "name": "New Items Alpha",
            "show_on_dashboard": True,
            "show_in_sidebar": False,
            "sort_field": "title",
            "sort_reverse": False,
            "filter_rules": [
                {"rule_type": 6, "value": "1"},
                {"rule_type": 33, "value": "7"},
            ],
            "owner": 1,
            "user_can_change": True,
        },
        {
            "id": 3,
            "name": "New Items Omega",
            "show_on_dashboard": True,
            "show_in_sidebar": False,
            "sort_field": None,
            "sort_reverse": False,
            "filter_rules": [
                {"rule_type": 6, "value": "1"},
                {"rule_type": 35, "value": "7"},
            ],
            "owner": 1,
            "user_can_change": True,
        },
        {
            "id": 4,
            "name": "Tax",
            "show_on_dashboard": False,
            "show_in_sidebar": True,
            "sort_field": "created",
            "sort_reverse": True,
            "filter_rules": [{"rule_type": 6, "value": "3"}],
            "owner": 1,
            "user_can_change": True,
        },
        {
            "id": 5,
            "name": "Todo",
            "show_on_dashboard": False,
            "show_in_sidebar": True,
            "sort_field": "created",
            "sort_reverse": True,
            "filter_rules": [{"rule_type": 6, "value": "4"}],
            "owner": 1,
            "user_can_change": True,
        },
    ],
}

V0_0_0_TAGS = {
    "count": 2,
    "next": None,
    "previous": None,
    "all": [
        1,
        2,
        3,
        4,
        5,
    ],
    "results": [
        {
            "id": 1,
            "slug": "important",
            "name": "Important",
            "color": "#ff0000",
            "text_color": "#00ff00",
            "match": "",
            "matching_algorithm": 0,
            "is_insensitive": True,
            "is_inbox_tag": False,
            "document_count": 20,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 2,
            "slug": "inbox",
            "name": "Inbox",
            "color": "#ff0000",
            "text_color": "#00ff00",
            "match": "",
            "matching_algorithm": 1,
            "is_insensitive": True,
            "is_inbox_tag": True,
            "document_count": 20,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 3,
            "slug": "test-3",
            "name": "Test 3",
            "color": "#ff0000",
            "text_color": "#00ff00",
            "match": "",
            "matching_algorithm": 2,
            "is_insensitive": True,
            "is_inbox_tag": False,
            "document_count": 20,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 4,
            "slug": "test-4",
            "name": "Test 4",
            "color": "#ff0000",
            "text_color": "#00ff00",
            "match": "",
            "matching_algorithm": 3,
            "is_insensitive": True,
            "is_inbox_tag": False,
            "document_count": 20,
            "owner": None,
            "user_can_change": True,
        },
        {
            "id": 5,
            "slug": "test-5",
            "name": "Test 5",
            "color": "#ff0000",
            "text_color": "#00ff00",
            "match": "",
            "matching_algorithm": 4,
            "is_insensitive": True,
            "is_inbox_tag": False,
            "document_count": 20,
            "owner": None,
            "user_can_change": True,
        },
    ],
}

V0_0_0_TASKS = [
    {
        "id": 1,
        "task_id": "11112222-aaaa-bbbb-cccc-333344445555",
        "task_file_name": "a.png",
        "date_created": "2023-12-16T13:06:29.107815+00:00",
        "date_done": None,
        "type": "file",
        "status": "STARTED",
        "result": None,
        "acknowledged": False,
        "related_document": None,
    },
    {
        "id": 2,
        "task_id": "ffffeeee-9999-8888-7777-ddddccccbbbb",
        "task_file_name": "b.png",
        "date_created": "2023-12-16T13:06:26.117158+00:00",
        "date_done": "2023-12-16T13:06:29.859669+00:00",
        "type": "file",
        "status": "SUCCESS",
        "result": "Success. New document id 1780 created",
        "acknowledged": False,
        "related_document": "1780",
    },
    {
        "id": 3,
        "task_id": "abcdef12-3456-7890-abcd-ef1234567890",
        "task_file_name": "c.png",
        "date_created": "2023-12-16T13:04:28.175624+00:00",
        "date_done": "2023-12-16T13:04:32.318797+00:00",
        "type": "file",
        "status": "SUCCESS",
        "result": "Success. New document id 1779 created",
        "acknowledged": False,
        "related_document": "1779",
    },
]

V0_0_0_USERS = {
    "count": 4,
    "next": None,
    "previous": None,
    "all": [1, 2, 3, 4],
    "results": [
        {
            "id": 1,
            "username": "admin",
            "email": "you@inside.me",
            "password": "**********",
            "first_name": "",
            "last_name": "",
            "date_joined": "2022-02-11T22:28:25+00:00",
            "is_staff": True,
            "is_active": False,
            "is_superuser": False,
            "groups": [],
            "user_permissions": [],
            "inherited_permissions": [],
        },
        {
            "id": 2,
            "username": "alpha",
            "email": "alpha@is-not.beta",
            "password": "**********",
            "first_name": "Alpha",
            "last_name": "Centauri",
            "date_joined": "2023-06-27T15:59:01.975496+00:00",
            "is_staff": False,
            "is_active": True,
            "is_superuser": False,
            "groups": [1],
            "user_permissions": [],
            "inherited_permissions": [
                "documents.delete_customfieldinstance",
                "documents.delete_consumptiontemplate",
                "documents.delete_customfield",
                "documents.add_uisettings",
                "documents.view_uisettings",
                "documents.view_tag",
                "documents.change_customfield",
                "documents.view_sharelink",
                "documents.change_note",
                "documents.view_correspondent",
                "documents.change_customfieldinstance",
                "documents.delete_note",
                "documents.add_consumptiontemplate",
                "documents.add_customfield",
                "documents.change_sharelink",
                "documents.view_consumptiontemplate",
                "documents.view_documenttype",
                "documents.change_document",
                "documents.view_customfieldinstance",
                "documents.add_sharelink",
                "documents.view_document",
                "documents.delete_uisettings",
                "documents.add_savedview",
                "documents.view_note",
                "documents.view_customfield",
                "documents.add_customfieldinstance",
                "documents.change_uisettings",
                "documents.change_savedview",
                "documents.add_document",
                "documents.add_note",
                "documents.change_consumptiontemplate",
                "documents.delete_sharelink",
                "documents.delete_savedview",
                "documents.view_savedview",
                "documents.delete_document",
            ],
        },
        {
            "id": 3,
            "username": "omega",
            "email": "omega.weapon@ff8.net",
            "password": "**********",
            "first_name": "Omega",
            "last_name": "Weapon",
            "date_joined": "2022-02-14T13:42:54+00:00",
            "is_staff": True,
            "is_active": True,
            "is_superuser": True,
            "groups": [1],
            "user_permissions": [],
            "inherited_permissions": [
                "documents.change_paperlesstask",
                "documents.delete_customfieldinstance",
                "django_celery_results.delete_chordcounter",
                "paperless_mail.change_processedmail",
                "django_celery_results.view_chordcounter",
                "documents.view_storagepath",
                "documents.delete_tag",
                "sessions.delete_session",
                "documents.view_log",
                "django_celery_results.change_groupresult",
                "documents.add_uisettings",
                "authtoken.delete_token",
                "admin.add_logentry",
                "django_celery_results.add_groupresult",
                "guardian.view_userobjectpermission",
                "paperless_mail.add_processedmail",
                "documents.change_customfieldinstance",
                "documents.view_correspondent",
                "auth.add_permission",
                "admin.view_logentry",
                "documents.delete_note",
                "documents.add_customfield",
                "auth.view_permission",
                "documents.add_consumptiontemplate",
                "guardian.delete_groupobjectpermission",
                "documents.change_sharelink",
                "documents.view_consumptiontemplate",
                "documents.delete_log",
                "guardian.delete_userobjectpermission",
                "paperless_mail.delete_mailrule",
                "sessions.change_session",
                "documents.add_tag",
                "documents.view_documenttype",
                "auth.view_user",
                "auth.add_group",
                "guardian.view_groupobjectpermission",
                "documents.change_document",
                "documents.change_savedviewfilterrule",
                "paperless_mail.add_mailrule",
                "documents.view_customfieldinstance",
                "guardian.add_userobjectpermission",
                "documents.add_sharelink",
                "auth.change_user",
                "documents.view_document",
                "django_celery_results.delete_taskresult",
                "documents.delete_uisettings",
                "documents.add_savedview",
                "documents.view_note",
                "authtoken.view_token",
                "authtoken.change_tokenproxy",
                "documents.change_storagepath",
                "documents.change_uisettings",
                "django_celery_results.add_chordcounter",
                "paperless_mail.change_mailrule",
                "documents.change_documenttype",
                "documents.change_savedview",
                "auth.delete_permission",
                "documents.add_storagepath",
                "django_celery_results.change_chordcounter",
                "documents.add_note",
                "documents.change_consumptiontemplate",
                "documents.delete_savedview",
                "guardian.change_userobjectpermission",
                "admin.delete_logentry",
                "authtoken.add_token",
                "documents.view_savedview",
                "documents.delete_paperlesstask",
                "sessions.view_session",
                "auth.delete_group",
                "paperless_mail.delete_mailaccount",
                "documents.add_savedviewfilterrule",
                "authtoken.delete_tokenproxy",
                "documents.delete_consumptiontemplate",
                "authtoken.view_tokenproxy",
                "authtoken.change_token",
                "documents.delete_customfield",
                "contenttypes.change_contenttype",
                "documents.change_log",
                "paperless_mail.view_mailrule",
                "documents.view_uisettings",
                "documents.view_tag",
                "documents.change_customfield",
                "admin.change_logentry",
                "documents.view_sharelink",
                "documents.change_note",
                "documents.delete_savedviewfilterrule",
                "auth.add_user",
                "django_celery_results.delete_groupresult",
                "documents.change_correspondent",
                "documents.add_documenttype",
                "django_celery_results.view_groupresult",
                "documents.add_paperlesstask",
                "contenttypes.add_contenttype",
                "auth.view_group",
                "guardian.change_groupobjectpermission",
                "django_celery_results.change_taskresult",
                "documents.change_tag",
                "paperless_mail.delete_processedmail",
                "paperless_mail.change_mailaccount",
                "documents.delete_correspondent",
                "paperless_mail.view_processedmail",
                "documents.delete_storagepath",
                "sessions.add_session",
                "paperless_mail.add_mailaccount",
                "django_celery_results.view_taskresult",
                "documents.view_customfield",
                "documents.view_paperlesstask",
                "documents.add_customfieldinstance",
                "django_celery_results.add_taskresult",
                "documents.view_savedviewfilterrule",
                "documents.add_log",
                "guardian.add_groupobjectpermission",
                "auth.delete_user",
                "auth.change_permission",
                "documents.add_document",
                "documents.delete_documenttype",
                "documents.delete_sharelink",
                "documents.add_correspondent",
                "authtoken.add_tokenproxy",
                "auth.change_group",
                "contenttypes.delete_contenttype",
                "contenttypes.view_contenttype",
                "paperless_mail.view_mailaccount",
                "documents.delete_document",
            ],
        },
        {
            "id": 4,
            "username": "zg_test",
            "email": "",
            "password": "**********",
            "first_name": "",
            "last_name": "",
            "date_joined": "2023-06-27T15:56:39.754859+00:00",
            "is_staff": False,
            "is_active": True,
            "is_superuser": False,
            "groups": [1],
            "user_permissions": [],
            "inherited_permissions": [
                "documents.delete_customfieldinstance",
                "documents.delete_consumptiontemplate",
                "documents.delete_customfield",
                "documents.add_uisettings",
                "documents.view_uisettings",
                "documents.view_tag",
                "documents.change_customfield",
                "documents.view_sharelink",
                "documents.change_note",
                "documents.view_correspondent",
                "documents.change_customfieldinstance",
                "documents.delete_note",
                "documents.add_consumptiontemplate",
                "documents.add_customfield",
                "documents.change_sharelink",
                "documents.view_consumptiontemplate",
                "documents.view_documenttype",
                "documents.change_document",
                "documents.view_customfieldinstance",
                "documents.add_sharelink",
                "documents.view_document",
                "documents.delete_uisettings",
                "documents.add_savedview",
                "documents.view_note",
                "documents.view_customfield",
                "documents.add_customfieldinstance",
                "documents.change_uisettings",
                "documents.change_savedview",
                "documents.add_document",
                "documents.add_note",
                "documents.change_consumptiontemplate",
                "documents.delete_sharelink",
                "documents.delete_savedview",
                "documents.view_savedview",
                "documents.delete_document",
            ],
        },
    ],
}
