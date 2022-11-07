#!/bin/bash

pdoc ad_leavers --output-dir=docs

pydoc-markdown -I ad_leavers --render-toc > README-docs.md  