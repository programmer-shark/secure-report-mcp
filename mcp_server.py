from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
import os
from fpdf import FPDF
import pikepdf

mcp = FastMCP("SecureReport-MCP")

@mcp.tool()
def generate_encrypted_pdf(text: str, password: str) -> str:
    """Generate a password-protected PDF from input text and return the file path."""
    output_path = "/tmp/secure_report.pdf"
    encrypted_path = "/tmp/secure_report_encrypted.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path)

    try:
        with pikepdf.open(output_path) as original_pdf:
            original_pdf.save(
                encrypted_path,
                encryption=pikepdf.Encryption(owner=password, user=password, R=4)
            )
    except Exception as e:
        return f"Encryption failed: {str(e)}"

    return encrypted_path

@mcp.resource("text://sample/weekly-summary")
def provide_example_text() -> str:
    """Returns a sample weekly status report."""
    return (
        "Weekly Summary:\n"
        "- Completed feature: PDF encryption.\n"
        "- Deployed to staging.\n"
        "- Fixed critical memory bug in session manager.\n"
        "- Team velocity: 36 story points.\n"
    )

@mcp.prompt()
def suggest_pdf_password(reason: str = "weekly report") -> list[base.Message]:
    """Suggest a secure password based on a use-case (e.g., encrypting a report)."""
    return [
        base.Message(
            role="user",
            content=[
                base.TextContent(
                    text=f"Suggest a strong password for securing a {reason}. "
                         f"It should be easy to remember but hard to guess."
                )
            ]
        )
    ]

def main():
    mcp.run()

if __name__ == "__main__":
    main()
