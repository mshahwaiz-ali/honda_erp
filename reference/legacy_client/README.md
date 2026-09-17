# Legacy Honda Client Evidence

Read-only evidence captured from the legacy Honda Oracle Forms client.

Confirmed legacy stack:

- Oracle Forms web application
- Launch configuration: `HONDA_SURJANI`
- Oracle Forms server: `ca93.att-apps.com:8889`
- Legacy application entry module:
  `D:\EZ_HONDA\MENU\LOGIN_FORM.fmx`
- Client runtime: Java 6 Update 32 (32-bit)
- Browser chain: Microsoft Edge -> IE compatibility process -> Java plugin
- Oracle runtime archives observed:
  - `frmall.jar`
  - `frmwebutil.jar`
  - `jacob.jar`

Important:

The actual Honda Forms application and business logic are server-side.
No `.fmb`, `.fmx`, `.mmb`, `.mmx`, `.pll`, `.plx`, `.rdf`, `.rep`,
database dump, or application source was recovered from the client PC.

Raw Java deployment caches are intentionally kept outside Git version
control because they are vendor/runtime artifacts rather than Honda
business application source.
