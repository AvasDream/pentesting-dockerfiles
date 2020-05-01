## Subjack 

Tool to check list of URLs for Subdomain Takeovers. 

```
Examples:

./subjack -w subdomains.txt -t 100 -timeout 30 -o results.txt -ssl
Options:

-w domains.txt is your list of subdomains.
-t is the number of threads (Default: 10 threads).
-timeout is the seconds to wait before timeout connection (Default: 10 seconds).
-o results.txt where to save results to. For JSON: -o results.json
-ssl enforces HTTPS requests which may return a different set of results and increase accuracy.
-a skips CNAME check and sends requests to every URL. (Recommended)
-m flag the presence of a dead record, but valid CNAME entry.
-v verbose. Display more information per each request.
-c Path to configuration file.

```