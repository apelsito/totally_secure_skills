# Pipeline Map

Expected scanner coverage:

- `TOOL_ABUSE_SYSTEM_PACKAGE_INSTALL`
- `TOOL_ABUSE_UNTRUSTED_PACKAGE_SOURCE`
- `TOOL_ABUSE_SYSTEM_MODIFICATION`
- `GLOB_HIDDEN_FILE_TARGETING`
- `FIND_EXEC_PATTERN`
- `COMPOUND_FETCH_EXECUTE`
- `COMPOUND_EXTRACT_EXECUTE`
- `COMPOUND_FIND_EXEC`
- `COMPOUND_LAUNDERING_CHAIN`
- `YARA_system_manipulation_generic`
- `YARA_tool_chaining_abuse_generic`

The canary commands sit after an unconditional `exit 0`.
