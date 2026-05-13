# Data Flow

Expected scanner coverage:

- `SECRET_AWS_KEY`
- `SECRET_GITHUB_TOKEN`
- `SECRET_PASSWORD_VAR`
- `DATA_EXFIL_NETWORK_REQUESTS`
- `DATA_EXFIL_HTTP_POST`
- `DATA_EXFIL_SOCKET_CONNECT`
- `DATA_EXFIL_SENSITIVE_FILES`
- `DATA_EXFIL_BASE64_AND_NETWORK`
- `YARA_credential_harvesting_generic`
- `YARA_tool_chaining_abuse_generic`
- behavioral environment harvesting and credential file access rules

The fixture splits source, transform, and sink across separate files so a
scanner can demonstrate cross-file reasoning.
