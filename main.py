def compare_links(link1, link2):
  link1 = link1.replace("!", "")
  link2 = link2.replace("!", "")
  return link1 == link2


def main():
  with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
    links1 = file1.readlines()
    links2 = file2.readlines()

  with open("Совпадающие ссылки.txt", "w") as matching_links, open("Несовпадающие ссылки.txt", "w") as non_matching_links:
    for link1 in links1:
      link1 = link1.strip()
      match = False

      for link2 in links2:
        link2 = link2.strip()
        if compare_links(link1, link2):
          matching_links.write(link1 + "\n")
          match = True
          break

      if not match:
        non_matching_links.write(link1 + "\n")

main()