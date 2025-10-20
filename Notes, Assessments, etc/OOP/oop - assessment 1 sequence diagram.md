```

+------------------+      +------------------+      +-------------------+      +---------------------+
| Human Operator   |      | CLI              |      | Robot             |      | Assembly Queue      |
+------------------+      +------------------+      +-------------------+      +---------------------+
        |                        |                        |                           |
        |--- start_assembly() -->|                        |                           |
        |                        |                        |                           |
        |                        |--- display("Ready") -->|                           |
        |                        |                        |                           |
        |                        |<-- order_received() ---|                           |
        |                        |                        |                           |
        |                        |--- run_order() -------->|                           |
        |                        |                        |                           |
        |                        |                        |--- move_to(workstation)   |
        |                        |                        |--- pick_up(part)         |
        |                        |                        |--- place(workstation)    |
        |                        |                        |--- undo_last_action()?   |
        |                        |                        |--- start_assembly()      |
        |                        |                        |--- dequeue step          |
        |                        |                        |--- perform_step()        |
        |                        |                        |--- validate_step()       |
        |                        |                        |--- complete_assembly()   |
        |                        |                        |                           |
        |                        |<-- order_complete() ----|                           |
        |                        |                        |                           |
        |<-- display("Done") ---|                        |                           |
        |                        |                        |                           |
``` 
