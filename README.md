Semantic Word Wrap for Sublime Text
===================================

This Sublime Text plugin inserts new line characters
between words while typing obtaining an hard-wrapped file.
The difference with normal hard-wrapping is
that the new lines are inserted in more natural places than
what happens in a hard-wrap at a certain width:
newlines are inserted preferably near punctuation
giving to the text a natural rhythm.

## Settings

`semantic_wrap`

Enables or disables semantic hard-wrapping.
Can be toggled with the `Edit > Semantic Wrap` menu.

`semantic_wrap_min_words`

The minimum number of words on the current line to justify
a break.

`semantic_wrap_max_words`

The maximum number of words tolerated on the current line.
Some presets can be selected from the `Edit > Semantic Wrap`
menu.

## Customisation

The keymap installed by the plugin is pretty self explanatory:

```json
[
    {
        "keys": [" "],
        "args": {"characters": "\n"},
        "command": "insert",
        "context": [
            {"key": "setting.semantic_wrap"},
            {"key": "semantic_wrap"},
            {
                "key": "preceding_text",
                "operand": "[.,;!?:]$",
                "operator": "regex_contains"
            }
        ]
    },
    {
        "keys": [" "],
        "args": {"characters": "\n"},
        "command": "insert",
        "context": [{"key": "semantic_wrap_words"}]
    }
]
```

You can customise it in your user keymap in various ways:
you can change which punctuation is considered suitable for a break,
or which character has to be inserted to end a line;
if you wish to enable the binding only for certain syntaxes
you can replace `{"key": "setting.semantic_wrap"}` with
`{"key": "selector", "operator": "equal", "operand": "YOUR.SCOPE"}`.
