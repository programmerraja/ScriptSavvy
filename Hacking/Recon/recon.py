import os
import subprocess

target_domain = "gcash.com"
recon_dir = f"{target_domain}/recon/targets/{target_domain}"

os.makedirs(f"{recon_dir}/subdomains", exist_ok=True)
os.makedirs(f"{recon_dir}/endpoints", exist_ok=True)
os.makedirs(f"{recon_dir}/aws", exist_ok=True)
os.makedirs(f"{recon_dir}/dns", exist_ok=True)

# Subdomain enumeration
subfinder_cmd = f"subfinder -d {target_domain} -o {recon_dir}/subdomains/subfinder.txt"
assetfinder_cmd = (
    f"assetfinder --subs-only {target_domain} >> {recon_dir}/subdomains/assetfinder.txt"
)
alterx_dynamic_cmd = f"echo {target_domain} | alterx -enrich | dnsx > {recon_dir}/subdomains/alterx-dynamic.txt"
alterx_permutation_cmd = f"echo {target_domain} | alterx -pp 'word=subdomains-top1million-50000.txt' | dnsx > {recon_dir}/subdomains/alterx-permutation.txt"
asnmap_cmd = f"asnmap -d {target_domain} | dnsx -silent -resp-only -ptr > {recon_dir}/subdomains/dnsx.txt"
ffuf_cmd = f"cat subdomains-top1million-50000.txt | ffuf -w -:FUZZ -u http://{target_domain}/ -H 'Host: FUZZ.{target_domain}' -ac"

subprocess.run(subfinder_cmd, shell=True)
subprocess.run(assetfinder_cmd, shell=True)
subprocess.run(alterx_dynamic_cmd, shell=True)
subprocess.run(alterx_permutation_cmd, shell=True)
subprocess.run(asnmap_cmd, shell=True)
subprocess.run(ffuf_cmd, shell=True)

# Merge subdomains
merge_cmd = (
    f"cat {recon_dir}/subdomains/*.txt | anew {recon_dir}/subdomains/subdomains.txt"
)
subprocess.run(merge_cmd, shell=True)

# Filter live subdomains

httpx_cmd = f"cat {recon_dir}/subdomains/subdomains.txt | httpx -o {recon_dir}/subdomains/httpx.txt"

subprocess.run(httpx_cmd, shell=True)

# Information gathering
httpx_info_cmd = f"cat {recon_dir}/subdomains/httpx.txt | httpx -tech -o {recon_dir}/endpoints/tech.txt"
subprocess.run(httpx_info_cmd, shell=True)

# Automated testing
nuclei_cmd = f"cat {recon_dir}/subdomains/httpx.txt | nuclei -t {recon_dir}/nuclei-templates/ -o {recon_dir}/nuclei-results.txt"
subprocess.run(nuclei_cmd, shell=True)
