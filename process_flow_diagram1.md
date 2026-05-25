```mermaid
flowchart TD
    A[Login to fcr] -->|Get customer data| B(Open a batch)
    B --> C{Type}
    C -->|One| D[Entity]
    C -->|Two| E[Related_party]
    C -->|Three| F[Not entity or related party]
    D --> G{1000 - Search customer}
    G -->|Found| H(7111 - Attach photo & signature images)
    G -->|Not Found| I(8053 - Create new cif_id)
    H --> J[Process completed]
