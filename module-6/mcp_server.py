from fastmcp import FastMCP

mcp = FastMCP("Employee Server")

@mcp.tool()
def get_employees() -> list:
    return [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Designer"},
        {"id": 3, "name": "Charlie", "role": "Manager"},
        {"id": 4, "name": "Diana", "role": "Analyst"},
        {"id": 5, "name": "Eve", "role": "Intern"},
    ]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")