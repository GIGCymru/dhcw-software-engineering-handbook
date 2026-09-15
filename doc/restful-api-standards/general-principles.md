# General principles

The following principles guide these standards:

- Prioritise user needs.

- Treat APIs as products, with dedicated teams, lifecycles, and
    roadmaps.

- Make APIs the primary interface for system interactions.

- Build APIs that are easy to learn, use, reuse, and integrate.

- Enable portability with container technologies like Docker.

- Adopt DevOps practices to deliver continuous value.

- Build APIs that conform to HL7 FHIR as a foundational interoperability standard.

- Use REST as the default design style, although you **MAY** choose alternatives when justified.

!!! tip "Practical tips"
    Appoint a dedicated API Product Owner to prioritise user needs.

!!! info "Further reading and information"
    The API Strategy & Roadmap

    [HL7 FHIR as a foundational standard in all NHS Wales Bodies \| GOV.WALES](https://www.gov.wales/introduction-hl7-fhir-foundational-standard-all-nhs-wales-bodies-whc2023018)

    [Fielding Dissertation: CHAPTER 5: Representational State Transfer (REST) (uci.edu)](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

    [The API Product Mindset (google.com)](https://cloud.google.com/files/apigee/apigee-api-product-mindset-ebook.pdf)

    [The principles --- Good Services ](https://good.services/15-principles-of-good-service-design)

## FHIR (Fast Healthcare Interoperability Standards)

APIs **MUST** conform to the FHIR R4 specification when a relevant FHIR
profile exists. Where no suitable profile is available, you may need to
model custom resources following FHIR principles.

FHIR R4 already addresses many fundamental aspects of RESTful API
design. If your API implementation is based on FHIR, you can jump
directly to the [API security](api-security.md) section.

!!! info "Further reading and information"
    [Wales FHIR Implementation Guide](https://simplifier.net/guide/fhir-standards-wales-implementation-guide?version=1.0.0)
