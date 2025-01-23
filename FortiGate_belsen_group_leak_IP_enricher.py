import time, csv, json, urllib.request

with open("affected_IPs.txt") as IPs:

  f = [
    "IP",
    "port",
    "status",
    "continent",
    "continentCode",
    "country",
    "countryCode",
    "region",
    "regionName",
    "city",
    "district",
    "zip",
    "lat",
    "lon",
    "timezone",
    "currency",
    "isp",
    "org",
    "as",
    "asname",
    "mobile",
    "proxy",
    "hosting"
  ]

  with open("affected_IPs_enriched.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=f)
    writer.writeheader()

  for line in IPs:

    line = str.strip(line, "\r\n")

    IP = str.split(line, ":")[0]
    port = str.split(line, ":")[1]

    res = json.loads(urllib.request.urlopen(f"http://ip-api.com/json/{IP}?fields=33279999").read().decode())

    r = { "IP": IP, "port": port }
    r.update(res)

    with open("affected_IPs_enriched.csv", "a") as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=f)
      writer.writerow(r)
    
    print(f"IP: {IP} @ Port: {port}")

    time.sleep(2)