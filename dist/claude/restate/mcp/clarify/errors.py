class ClarifyError(Exception):
    """An actionable tool failure, not a broken MCP connection."""

    def __init__(self, code, message, **details):
        super().__init__(message)
        self.code = code
        self.details = details

    def payload(self):
        return {"code": self.code, "message": str(self), **self.details}
