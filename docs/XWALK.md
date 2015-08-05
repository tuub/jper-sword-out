# JPER Core Metadata to Dublin Core/RIOXX XML

| JPER Field | DC/RIOXX Field | Notes |
| ---------- | -------------- | ----- |
| links.url | dc:identifier | As per the recommended use by RIOXX |
| embargo.end | dcterms:available and ali:license_ref@start_date | "Date (often a range) that the resource became or will become available." from DCMI terms |
| metadata.title | dc:title | |
| metadata.version | rioxxterms:version | May not conform to required use by RIOXX because of unknown nature of the values supplied by publishers |
| metadata.publisher | dc:publisher | |
| metadata.source.name | dc:source | May not conform to required use by RIOXX because multiple dc:source elements may be present |
| metadata.source.identifier | dc:source | prefixed with appropriate namespace |
| metadata.identifier | dc:identifier AND rioxxterms:version_of_record | Always populate dc:identifier, and populate rioxxterms:version_of_record if this is a DOI (as a URL) |
| metadata.type | dc:type | Ignoring the RIOXX recommendation here, as the DC field is present, and is not so restrictive |
| metadata.author | dc:creator AND rioxxterms:author | for dc, use separate fields for creator name and any identifiers; for rioxx use orcid as id (as URL), and add other attributes as required.  See RIOXX guidelines during implenmentation for details. |
| metadata.author.affiliation | dc:contributor | Since there's nowhere else obvious to put this useful bit of information |
| metadata.language | dc:langauage | |
| metadata.publication_date | rioxxterms:publication_date AND dc:date | covering RIOXX and the more likely existing defaults in repositories |
| metadata.date_accepted | dcterms:dateAccepted | |
| metadata.date_submitted | dcterms:dateSubmitted | |
| metadata.license_ref.url | ali:license_ref AND dc:rights | Note that the @start_date should be embargo.end, but may also be any other suitable date from the metadata |
| metadata.license_ref.title | dc:rights | if no metadata.license_ref.url is present |
| metadata.project.* | rioxxterms:project | See RIOXX documentation for details in implementation |
| metadata.subject | dc:subject | |


## DSpace Notes

* dc:dateAvailable should be configured to go to your embargo field