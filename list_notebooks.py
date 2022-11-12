#!/usr/bin/env python
import os

from evernote.api.client import EvernoteClient
from dotenv import load_dotenv

    
if __name__ == '__main__':
    load_dotenv()
    client = EvernoteClient(
        token=os.getenv('EVERNOTE_PERSONAL_TOKEN'),
        sandbox=False
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
