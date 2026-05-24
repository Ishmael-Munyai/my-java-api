```mermaid
flowchart TD
    A([ Event: Claim Received]) --> B[ Process Start: RPA Bot Triggered]
    B --> C[ Extract Claim Data]
    C --> D[ Validate Against Business Rules]
    D --> E{Data Complete?}
    E -->|No| F[ Flag for Manual Review]
    E -->|Yes| G[ Register Claim in System]
    F --> H[ Notify Claims Officer]
    G --> I[ Claim Registered Successfully]
