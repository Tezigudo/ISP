"""Example use of link scanner."""
from link_scanner import *


if __name__ == "__main__":
    url = find_link("https://cpske.github.io/ISP/", "Topics")
    print("ISP Topics page is", url)

    links = find_links(url)1
    print(f"All links on page:")
    for link in sorted(links):
        print(link)
