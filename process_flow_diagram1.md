```mermaid
flowchart TD
    A[Open fcr] -->|Get customer data| B(Login to fcr)
    B --> C{Type}
    C -->|One| D[Entity]
    C -->|Two| E[Related_party]
    C -->|Three| F[Not entity or related party]
    D --> G{1000 - Search customer}
    G -->|Found| H[7111 - Attach photo & signature images]
    G -->|Not Found| I[8053 - Create new cif_id]
    H --> J[Process completed]
