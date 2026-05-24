```mermaid
flowchart TD
    Start([Order Placed]) --> CheckStock[Check Inventory]
    CheckStock --> ProcessOrder[Process Order]
    ProcessOrder --> End([Order Shipped])
