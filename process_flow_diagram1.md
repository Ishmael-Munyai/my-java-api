```mermaid
flowchart TD
    A[CIF creation] -->|Get customer data| B(Open fcr)
    B --> C{Let me think}
    C -->|One| D[Entity]
    C -->|Two| E[Related_party]
    C -->|Three| F[Not entity or related party]
    D --> G{Search customer}
    G -->|Found| H[7111]
    G -->|Not Found| I[8053]
