```{seo}
:description: Guidelines for writing Duckietown technical documentation.
:keywords: duckietown, documentation, style, technical writing
```

(documentation-style-guide)=
# Style guide

This chapter defines the conventions for writing Duckietown technical documentation.

## Organization

The documentation is divided into **books**, **parts** (labeled `part:`), **chapters** (labeled `chapter:`), and **sections** (labeled `sec:`).

The structure of each book is defined in `src/_toc.yml`.

## General guidelines for technical writing

The following guidelines apply to all technical writing.

- Write the documentation in correct English.

- Use "should" and "must" deliberately; each has a distinct meaning.[^rfc2119]

[^rfc2119]: The meanings of these terms are defined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

- Omit "please"; it is unnecessary in technical documentation:

  ```{admonition} Wrong
  :class: danger

  "Please remove the SD card."
  ```

  ```{admonition} Better
  :class: success

  "Remove the SD card."
  ```

- Avoid colloquialisms and unexplained abbreviations:

  ```{admonition} Wrong
  :class: danger

  "The pwd is `ubuntu`."
  ```

  ```{admonition} Better
  :class: success

  "The password is `ubuntu`."
  ```

- Capitalize `Python` when referring to the programming language:

  ```{admonition} Wrong
  :class: danger

  "If you are using python, follow these instructions."
  ```

  ```{admonition} Better
  :class: success

  "If you are using Python, follow these instructions."
  ```

- Do not use contractions:

  ```{admonition} Wrong
  :class: danger

  "It's ready."
  ```

  ```{admonition} Better
  :class: success

  "It is ready."
  ```

- Avoid emojis.

- Avoid **ALL CAPS** for emphasis; retain established acronyms, commands, and identifiers.

- Use **bold text** sparingly.

- Avoid exclamation points.

## Style guide for the Duckietown documentation

- Use American English in English-language documentation:

  ```{admonition} Incorrect
  :class: danger

  behaviour
  ```

  ```{admonition} Correct
  :class: success

  behavior
  ```

- Format filenames and commands as inline code using Markdown backticks:

  ```{admonition} Incorrect
  :class: danger

  "Edit the ~/.ssh/config file using nano."
  ```

  ```{admonition} Correct
  :class: success

  "Edit the `~/.ssh/config` file using `nano`."
  ```

- Do not use keyboard shortcuts or command names as verbs:

  ```{admonition} Incorrect
  :class: danger

  "<kbd>Ctrl</kbd>-<kbd>C</kbd> the command."
  ```

  ```{admonition} Correct
  :class: success

  "Press <kbd>Ctrl</kbd>-<kbd>C</kbd> in the terminal."
  ```

- Subtle humor and puns about duckies are encouraged.

Use only the complexity needed to convey your message, and do not use overly complex language to disguise flaws. A useful test is whether you can explain the topic clearly to a non-specialist.

```{admonition} Prefer concise wording
:class: tip

Use simpler wording when it does not change the meaning:

- `provide` -> `give`

- `in order to` -> `to`

- `utilize` -> `use`
```

(frequently-misspelled-words)=
## Naming and spelling

- Capitalize product names in prose, headings, link labels, captions, alternative text, and SEO descriptions: "Duckietown", "Duckiebot", "Duckiedrone", "Duckiebox", "Duckiebattery", and "Duckiematrix".

- Use "Duckietown Shell", "Duckietown Viewer", "Duckietown Workspace", "Duckietown Dashboard", and "Dev Container" when referring to named tools and environments. Use lowercase forms in commands, package and repository names, URLs, filenames, anchors, configuration values, and SEO keywords.

- Capitalize "Engine", "Renderer", and "Entity" when referring to Duckiematrix components and simulated objects. Use lowercase forms in command subcommands and flags.

- Use "Raspberry Pi", not "PI" or "raspi".

## Other conventions

- Place the `seo` directive immediately after any YAML front matter, before page labels, headings, and other content.

- Every non-decorative `{figure}` and `{image}` directive must include a concise `:alt:` description. Add a figure caption to standalone diagrams, maps, screenshots, overview and reference figures, and completed assemblies. Omit captions for routine procedural-step images when adjacent instructions already identify the image.

- Every `{figure}` directive must include a unique `:name:` label so that it can be referenced.

When instructing a user to edit a file, write `edit /this/file`.

Do not include an editing command such as the following unless the task requires a feature available only in a particular editor:

```shell
vi /this/file
```

## Troubleshooting sections

Write the main procedure assuming that every step succeeds.

Add a "Troubleshooting" section at the end.

Organize the section as a list of symptom-and-resolution pairs.

The following is an example of a troubleshooting section.

### Troubleshooting

Use the [`{trouble}` directive](language-format-troubleshooting) to define troubleshooting
entries. For example:

```{trouble}
The camera image is blank.
---
Check that the camera cable is fully inserted. Disconnect and reconnect it if necessary.
```
