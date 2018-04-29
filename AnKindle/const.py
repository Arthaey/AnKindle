# -*- coding: utf-8 -*-
# Created: 3/27/2018
# Project : AnKindle
import os

from .libs import six

__version__ = "0.5.10"
HAS_SET_UP = False
ADDON_CD = 1016931132
DEBUG = False
ONLINE_DOC_URL = "https://github.com/upday7/AnKindle/tree/master/AnKindle/docs/DOC.md"
DEFAULT_TEMPLATE = six.ensure_str(os.path.join(os.path.dirname(__file__), u"resource", u"AnKindle.apkg"))
SQL_SELECT_WORDS = """
SELECT
  ws.id,
  ws.word,
  ws.stem,
  ws.lang,
  datetime(ws.timestamp * 0.001, 'unixepoch', 'localtime') added_tm,
  lus.usage,
  bi.title,
  bi.authors
FROM words AS ws LEFT JOIN lookups AS lus ON ws.id = lus.word_key
  LEFT JOIN book_info AS bi ON lus.book_key = bi.id
"""

MUST_IMPLEMENT_FIELDS = (
    "STEM", "WORD", "LANG", "CREATION_TM", "USAGE", "TITLE", "AUTHORS", "ID"
)
