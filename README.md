# Description 
The proposed system is a web-based bibliographic reference manager that allows researchers, students, and academicians to store, manage, and organize research papers and references in a centralized manner. 

Unlike local tools (e.g., Zotero, Mendeley), this system will be accessible via a browser, ensuring collaboration, accessibility, and ease of use across devices.


## Modules:
1. Centralized Reference Database
	Maintain a structured database of research papers (title, authors, publication year, venue, DOI, abstract, PDF, tags, etc.).
	Support for importing references in common formats (.bib, .ris, .endnote).
	Duplicate detection and metadata auto-completion using DOI/ISBN lookups.

2. User Management & Collaboration
	Secure authentication (OAuth2 / SSO).
	Role-based access (individual accounts, group libraries, shared collections).
	Ability to annotate, comment, and tag references collaboratively.

3. Search & Organization
	Full-text search across metadata and uploaded PDFs.
	Filters by author, year, tags, or keywords.
	Smart collections that auto-update based on query conditions.

4. Citation Generation
	Export citations in multiple styles (APA, IEEE, ACM, Chicago, etc.).
	Integration with LaTeX (BibTeX export)

5. Web Integration
	Browser extension to directly save references while browsing.
	DOI/ArXiv/Google Scholar integration for quick reference fetching.

## Tech Stack:

### Frontend:
  React.js / Next.js for a fast, interactive web UI.
  TailwindCSS / Bootstrap for responsive design.

### Backend (API):
  Python (Django REST Framework) for handling reference management, authentication, and citation generation.
  REST/GraphQL API for extensibility.

### Database:
  PostgreSQL (primary metadata + user accounts).
  Elasticsearch for full-text search in titles/abstracts/PDFs.
  Object Storage for storing uploaded PDFs.

### Citation & Parsing Libraries:
  BibTeX parsing via bibtexparser (Python).
  Citation Style Language (CSL) integration for multiple citation formats.

### Authentication & Security:
  OAuth2 / JWT for secure login.

  
---
# Possible Extension:
Integration with university SSO for institutional use.
