from urllib.request import urlopen, Request
import re
import click


@click.command(help=f"{'[Scrapr v0.0.1]':<68}{'Author: @xSplayd':<68}"
                    f"{'--------------------------------------------------------------------------':<80}"
                    f"{'This cli tool will automatically scrape email addresses from any webpage.':<75}"
                    f"{'Instructions: Simply type scrapr <url> into your command line!':<75}"
                    "--------------------------------------------------------------------------")
@click.argument("url", type=str, nargs=1)
def scrapr(url):
    print("Scraping...")
    try:
        req = Request(url, headers=
        {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    except ValueError:
        print("ERROR: Please use a valid URL link that has a protocol (https://) and a tld")
        print("Refer to 'scrapr --help' for more information")
        exit(1)
    data = urlopen(req).read().decode()
    emails(data)


def emails(data):
    match_pattern = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)
    if not match_pattern:
        print("ERROR: No email addresses were found on this website")
    else:
        find = set(match_pattern)
        deduped = list(find)
        print("Finished!")
        print()
        for i in range(len(deduped)):
            print(deduped[i])