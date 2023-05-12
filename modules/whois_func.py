import whois

def whois_func(url,directory):
    file_path = f"{directory}/whois.txt"
    with open(file_path, "w") as file:
        w = whois.whois(url)
        file.write(f"{w.text}")
        print(f"{w.text}")
    
