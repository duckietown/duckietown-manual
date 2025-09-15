```{seo}
:description: Learn about the general layout of Duckietown documentation and how to contribute.  
:keywords: duckietown, documentation, overview, markdown, html, sphinx
```


(duckumentation-intro)=
# Overview

(where_documentation_is)=
## Where the Documentation is Stored and Hosted

The documentation is all stored in a [Github repository](https://github.com/duckietown/duckietown-manual).
When a change is pushed to the repository, it automatically triggers the book to be rebuilt and updated. 

(documentation_format)=
## Documentation Format

The documentation is written as a series of small files in Markedly Structured Text (MyST), a Markdown format inspired by Sphinx and reStructuredText (RST).

It is then processed by a series of scripts to create publication-quality PDF and an online HTML version.

You can find all these artifacts produced at the site [`https://docs.duckietown.com`](https://docs.duckietown.com).

(documentation_branches_and_more)=
## Previous Version of the Documentation

Previously, in the `daffy` version, the documentation was split amongst several books. With the `ente` version
and beyond, the documentation is merged into one monolithic book that can be searched and indexed more 
easily. 

The "version" of the documentation corresponds to the branch in the repository. 
`Daffy` documentation can be found at [`https://docs.duckietown.com/daffy`](https://docs.duckietown.com/daffy), and the respective content available 
on the [Duckietown GitHub](https://github.com/duckietown), in repositories named `docs-[book name]`, e.g., the [Old Duckiebot operation manual](https://github.com/duckietown/docs-opmanual_duckiebot). 

`Ente` documentation can be found at [`https://docs.duckietown.com/ente`](https://docs.duckietown.com/ente).

Future versions of the documentation will be new branches of this repository. 

### Deprecated Documentation System

The even older, now deprecated, Duckietown documentation system is 
available at: [https://docs-old.duckietown.org/daffy/](https://docs-old.duckietown.org/daffy/). 
