# AGENT Guidelines

## Repository Guidelines

### Overview
This repository is a helper tool for inventory management, price calculation, contact management, and bookkeeping for an anime goods booth at Comiket.

### Coding Style Guidelines
- **Python**: Follow PEP 8.
- **Type Hinting**: Use type hints for all function arguments and return values.
- **Documentation**: Document all classes and functions with docstrings.
- **Naming**: Use snake_case for functions/variables, PascalCase for classes.

### Security Considerations
- **Input Validation**: Validate all user inputs in the Streamlit UI before processing.
- **Data Safety**: Ensure JSON writes are atomic or safe to prevent data corruption.

### Build & Test
- **Setup**: `mise install`
- **Run**: `mise run shop`
- **Test**: `pytest` (future implementation)

### Knowledge & Library
- Before implementation, check documentation for libraries if unsure.
- Use `grep` or similar tools to scan for files when necessary.
- Use recursive patterns or multi-threading for compute-intensive tasks if applicable.

### Maintenance Policy
- Reflect repeated instructions from conversation in this file.
- Consider compressing redundant parts.
- Keep documents concise but dense.

## SOLID Principles
This project should adhere to SOLID principles:
- **S**ingle Responsibility Principle: Each class/module should have one job.
- **O**pen/Closed Principle: Open for extension, closed for modification.
- **L**iskov Substitution Principle: Subtypes must be substitutable for their base types.
- **I**nterface Segregation Principle: Clients should not be forced to depend on interfaces they don't use.
- **D**ependency Inversion Principle: Depend on abstractions, not concretions.
