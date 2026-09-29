from fastmcp import FastMCP

mcp = FastMCP("My Tools")


@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool
def reverse_text(text: str) -> str:
    """Reverse a piece of text."""
    return text[::-1]


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8001)