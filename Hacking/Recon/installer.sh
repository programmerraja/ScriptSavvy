#!/bin/bash

# Install necessary tools
echo "Installing necessary tools..."

# Install subfinder
echo "Installing subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Install assetfinder
echo "Installing assetfinder..."
go install -v github.com/tomnomnom/assetfinder@latest

# Install alterx
echo "Installing alterx..."
go install -v github.com/lc/alterx@latest

# Install dnsx
echo "Installing dnsx..."
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest

# Install asnmap
echo "Installing asnmap..."
go install -v github.com/projectdiscovery/asnmap/cmd/asnmap@latest

# Install ffuf
echo "Installing ffuf..."
go install -v github.com/ffuf/ffuf@latest

# Install httpx
echo "Installing httpx..."
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Install nuclei
echo "Installing nuclei..."
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Install nuclei templates
echo "Installing nuclei templates..."
git clone https://github.com/projectdiscovery/nuclei-templates.git /usr/share/nuclei-templates

# Run the reconnaissance script
echo "Running reconnaissance script..."
python reconnaissance_script.py
